#!/usr/bin/env python3
"""Apply cut zones from a retakes JSON to a video."""
import json, subprocess, sys, os

INPUT_VIDEO = sys.argv[1]
RETAKES_JSON = sys.argv[2]
OUTPUT_VIDEO = sys.argv[3]

OUT_DIR = os.path.dirname(OUTPUT_VIDEO)

with open(RETAKES_JSON) as f:
    data = json.load(f)
cuts = data["cuts"]

if not cuts:
    print("No cuts to apply. Copying input to output.")
    subprocess.run(["cp", INPUT_VIDEO, OUTPUT_VIDEO])
    sys.exit(0)

SOURCE_DUR = float(subprocess.run(
    ["ffprobe","-v","quiet","-show_entries","format=duration","-of","csv=p=0", INPUT_VIDEO],
    capture_output=True, text=True
).stdout.strip())
print(f"Source: {SOURCE_DUR:.1f}s")
print(f"Applying {len(cuts)} cut zones, total {sum(e-s for s,e in cuts):.1f}s")

# Sort and merge overlapping cut zones
cuts = sorted([(s, e) for s, e in cuts])
merged = []
for s, e in cuts:
    if merged and s <= merged[-1][1] + 0.05:
        merged[-1] = (merged[-1][0], max(merged[-1][1], e))
    else:
        merged.append((s, e))
print(f"After merging overlaps: {len(merged)} cut zones")

# Build keep segments
def subtract_zones(segs, zones):
    result = []
    for ks, ke in segs:
        parts = [(ks, ke)]
        for zs, ze in zones:
            new_parts = []
            for s, e in parts:
                if ze <= s or zs >= e: new_parts.append((s, e))
                elif zs <= s and ze >= e: pass
                elif zs > s and ze < e: new_parts.extend([(s, zs), (ze, e)])
                elif zs <= s: new_parts.append((ze, e))
                else: new_parts.append((s, zs))
            parts = new_parts
        result.extend(parts)
    return [(s, e) for s, e in result if e - s > 0.05]

keep = subtract_zones([(0, SOURCE_DUR)], merged)
total_keep = sum(e - s for s, e in keep)
print(f"Keep: {total_keep:.1f}s ({len(keep)} segments)")

segments_path = OUTPUT_VIDEO + ".segments.json"
with open(segments_path, "w") as f:
    json.dump(keep, f)

render_cuts = os.path.join(OUT_DIR, "render_cuts.py")
r = subprocess.run(["python3", render_cuts, INPUT_VIDEO, segments_path, OUTPUT_VIDEO])
if r.returncode != 0:
    sys.exit(1)

print(f"\nDone: {SOURCE_DUR:.0f}s -> {total_keep:.0f}s ({total_keep/60:.1f} min)")
