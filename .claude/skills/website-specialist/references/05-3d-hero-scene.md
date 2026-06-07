# 05 · 3D hero scene (R3F + Drei + Three)

The hero is the craft signal. Caravaggio not Vegas. Text is the LCP. 3D mounts after first paint.

## Stack (locked)

- `next@^16.0.0` App Router
- `react@^19`, `react-dom@^19`
- `three@^0.171.0`
- `@react-three/fiber@^9.3.0`
- `@react-three/drei@^10.7.0`
- `@types/three@^0.171.0`

Pin minor on `three` and `@types/three` together. Drift here breaks everything.

## Install

```bash
npm install three @react-three/fiber @react-three/drei
npm install -D @types/three
```

Lock in `package.json`:

```json
{
  "dependencies": {
    "@react-three/drei": "^10.7.0",
    "@react-three/fiber": "^9.3.0",
    "three": "^0.171.0"
  },
  "devDependencies": {
    "@types/three": "^0.171.0"
  }
}
```

## Five traps

1. **Hydration mismatch on `<Canvas>`.** Always dynamic-import with `ssr: false`.
2. **`@types/three` drift.** Pin minor to match `three` exactly.
3. **GLB path resolution.** Models go in `public/models/`. Preload with `useGLTF.preload("/models/foo.glb")` outside the component.
4. **Three.js r-version breaking changes.** Lock minor. Upgrade only when you have time to rebuild the scene.
5. **Suspense fallback layout jump.** Wrapper has explicit CSS `aspect-ratio` so the page never reflows when the canvas mounts.

## The hero concept comes from `business.md`

There is no default hero recipe. The operator's aesthetic dictates the right hero. Read `business.md`, find the aesthetic descriptor, then pick the hero concept that matches.

Common 3D hero patterns by aesthetic:

| Aesthetic in `business.md` | Hero pattern that fits |
|---|---|
| dark, painterly, cinematic | Single mesh + single key light against deep black background |
| minimal, clean, Scandinavian | Single white-on-white object, soft daylight, slow drift |
| brutalist, hard, concrete | Large geometric mass, hard shadows, raw material shaders |
| editorial, soft, warm | Photographic still + subtle parallax, no canvas required |
| retro, analog, grainy | CRT-style screen with film grain shader |
| clinical, precise, even-lit | Wireframe overlay on a clean object, no atmosphere |
| cinematic, anamorphic | Volumetric haze + slow rack focus on a focal mesh |

Pick one. Hold to one shader, one idea, one light source. Implementation target: 45 to 60 minutes from empty folder to deployed URL regardless of which pattern.

If the operator does not have an aesthetic descriptor, stop and ask. Do not guess. The wrong hero kills the brand.

## File structure

```
src/
├── app/
│   ├── page.tsx                    # server component, dynamic-imports HeroScene
│   └── layout.tsx
├── components/
│   ├── hero-scene.tsx              # client, mounts <Canvas>, single named export
│   └── hero-scene-poster.tsx       # static fallback for mobile/reduced-motion
public/
└── images/
    └── hero-poster.png             # mobile fallback PNG (1920x1080)
```

## Page wiring (`app/page.tsx`)

```tsx
import dynamic from "next/dynamic";

// Hero is client-only. SSR off prevents hydration mismatch.
const HeroScene = dynamic(() => import("@/components/hero-scene").then(m => m.HeroScene), {
  ssr: false,
  loading: () => <HeroPoster />,
});

import { HeroPoster } from "@/components/hero-scene-poster";

export default function Page() {
  return (
    <main>
      <section className="px-6 pt-24 pb-16">
        <h1 className="text-center text-[48px] md:text-[104px]">
          {/* Your headline here. Text IS the LCP. */}
        </h1>
      </section>

      <section className="relative w-full">
        <div className="relative w-full" style={{ aspectRatio: "16 / 9" }}>
          <HeroScene />
        </div>
      </section>

      {/* Rest of page */}
    </main>
  );
}
```

The wrapper's `aspectRatio: "16 / 9"` is non-negotiable. Without it, the page reflows when the canvas mounts.

## HeroScene component (skeleton)

This is the SKELETON. Fill in the focal mesh, light direction, color, and shader to match the operator's aesthetic. The structure is universal; the visuals are not.

```tsx
"use client";

import { Canvas, useFrame } from "@react-three/fiber";
import { EffectComposer } from "@react-three/postprocessing";
import { useRef } from "react";
import * as THREE from "three";

// FOCAL MESH: replace this component with whatever the operator's
// aesthetic calls for. Sphere, cube, low-poly portrait, abstract,
// imported GLB, scroll text, anything single-focal.
function FocalMesh() {
  const ref = useRef<THREE.Group>(null);

  useFrame((_, delta) => {
    if (!ref.current) return;
    ref.current.rotation.y += delta * 0.05; // slow drift
  });

  return (
    <group ref={ref}>
      <mesh>
        <sphereGeometry args={[1, 32, 32]} />
        <meshStandardMaterial color="#888888" roughness={0.9} />
      </mesh>
    </group>
  );
}

// KEY LIGHT: adjust position, color, intensity to match aesthetic.
// Dark/painterly: one warm low-intensity light from upper-left.
// Bright/clean: high ambient + soft fill from above.
// Brutalist: hard directional from a single side.
function KeyLight() {
  const ref = useRef<THREE.SpotLight>(null);

  useFrame((state) => {
    if (!ref.current) return;
    const t = state.clock.elapsedTime;
    ref.current.intensity = 5 + Math.sin(t * 0.6) * 1.0; // subtle breathing
  });

  return (
    <spotLight
      ref={ref}
      position={[3, 5, 4]}
      angle={0.4}
      penumbra={0.8}
      intensity={5}
      color="#ffffff"
      castShadow
    />
  );
}

export function HeroScene() {
  return (
    <Canvas
      camera={{ position: [0, 1, 5], fov: 38 }}
      gl={{ antialias: true, powerPreference: "high-performance" }}
      // BACKGROUND: match the aesthetic. Deep black for cinematic,
      // pure white for minimal, neutral grey for editorial, etc.
      style={{ background: "#050505" }}
    >
      <ambientLight intensity={0.1} />
      <KeyLight />
      <FocalMesh />
      <EffectComposer>
        {/* Add post-processing only if the aesthetic calls for it.
            Bloom, vignette, depth-of-field, chromatic aberration.
            pick what fits. None is also valid. */}
      </EffectComposer>
    </Canvas>
  );
}
```

The structure is universal: one focal mesh, one key light, one camera, optional post-processing. The visuals are operator-driven.

## Mobile and reduced-motion

```tsx
// components/hero-scene-poster.tsx
import Image from "next/image";

export function HeroPoster() {
  return (
    <div className="relative h-full w-full">
      <Image
        src="/images/hero-poster.png"
        alt=""
        fill
        priority
        sizes="100vw"
        className="object-cover"
      />
    </div>
  );
}
```

To detect reduced motion at runtime and swap to the poster, wrap `HeroScene`:

```tsx
"use client";
import { useEffect, useState } from "react";

export function HeroSceneOrPoster() {
  const [reduced, setReduced] = useState(false);
  useEffect(() => {
    const mq = window.matchMedia("(prefers-reduced-motion: reduce)");
    setReduced(mq.matches);
    mq.addEventListener("change", e => setReduced(e.matches));
  }, []);
  if (reduced) return <HeroPoster />;
  return <HeroScene />;
}
```

The hero poster is generated once via Higgsfield using one of the three options in `04-higgsfield-prompts.md`. Drop into `public/images/hero-poster.png`.

## Bundle budget

The hero chunk must be under **250KB gzip**. Measure with:

```bash
npm run build
# Look for the largest first-load JS chunk in the output
```

If the chunk is over budget:

- Cut Drei components you imported but do not use
- Drop the post-processing pass and replace with a CSS gradient overlay
- Lower mesh polygon count (target 1k to 2k)
- Mobile: skip 3D entirely, serve the poster always

## Anti-patterns

- **Particles for the sake of particles.** If the scene has more than one focal idea, cut.
- **Bright/airy/clean.** Caravaggio not Vegas. Dark backgrounds, single light source.
- **Spinning logos.** Slow drift only. Spinning reads as cheap.
- **OrbitControls in the hero.** The user is reading, not exploring. No camera controls in the hero.
- **HDRI environments.** Use a single ambient + one spotlight. HDRI inflates the bundle.
- **GLB models over 1MB.** Decimate before shipping.

## Override paths

If `business.md` specifies a different hero:

- **Photographic only:** drop the canvas, use a full-bleed `<Image>` with the Higgsfield hero render. Skip this whole reference.
- **Animated SVG:** use `<motion.svg>` from Framer Motion. Add framer-motion to dependencies. Skip the R3F install.
- **WebGL custom shader:** keep the canvas wrapper but replace `CrossMesh` with a `<shaderMaterial>` mesh. Bundle budget still applies.
- **Scroll-driven scene:** use `<ScrollControls>` from Drei. Costs another 30KB. Confirm with operator before adding.

## Deploy verification

After `vercel deploy --prod`:

1. Open the live URL on mobile (real device, not emulator).
2. Confirm the headline appears within 1.5 seconds (LCP).
3. Confirm the canvas mounts without the page reflowing (CLS under 0.1).
4. Run Chrome Lighthouse on the deployed URL. Target Performance score > 85 on mobile.

If LCP is over 2.5 seconds: the headline is not the LCP. Check that the canvas wrapper has `aspectRatio` set, the dynamic import is `ssr: false`, and no large image loads above the headline.
