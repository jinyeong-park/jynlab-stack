# Publish package

**When to load**: Step 5 of /youtube. Generate everything needed to publish the video.

---

## What the publish package contains

One file (`04_PUBLISH.md`) with everything ready to copy-paste:

1. Final title (1 primary + 2 alternates for A/B testing)
2. Thumbnail brief (face position, text elements, accent color, 3 alternate concepts)
3. YouTube description (hook line, CTA links, timestamps, hashtags)
4. Tags (15-20 search keywords)
5. Pinned comment (CTA + engagement ask)
6. YouTube community post (4-5 lines driving to the video)
7. Upload settings (category, end screen, cards)

---

## Title rules

- "Claude Code" in the first half of the title (natural, not forced)
- Under 58 characters
- Include one specific number or dollar amount
- Past tense action verb ("Got", "Built", "Automated") over promise verbs ("Will", "Can")
- No Tier 1 banned words
- No patterns: "Claude Code fires X", "Claude Code makes Y"
- Proven patterns: "Claude Code: How I [verb] [result]", "I [verb] X with Claude Code ([detail])"

## Thumbnail rules

- Face occupies 30-40% of frame, left or right aligned
- 2 text elements maximum (one large, one smaller below)
- Dark background (#0A0A0A or similar)
- One accent color only (Claude orange-red #C15F3C or green for positive results)
- No arrows, no shock emojis, no gradients, no decorative borders
- Text readable at phone size (test by shrinking to 2cm wide)
- 8% margin on all edges
- Direct camera expression (serious, slight lean-in, no fake shock)

## YouTube description format

```
[One-line hook matching the title claim.]

[CTA link 1]: https://theagentfounders.com/claude
[CTA link 2]: https://theagentfounders.com/

[Timestamps from the script sections]
0:00 [Hook topic]
0:45 [Problem topic]
2:30 [Solution section 1]
...
9:00 Results
11:00 How to get started

#hashtag1 #hashtag2 #hashtag3 #hashtag4 #hashtag5
```

**Rules**:
- Description under 500 words
- CTA links above the fold (first 3 lines, visible before "show more")
- Timestamps match the actual video (adjust after editing)
- 5-7 hashtags, no more
- No em dashes in the description

## Tags

15-20 keywords. Mix of:
- Exact topic ("claude code cold email", "ai outreach automation")
- Broad niche ("ai service business", "solo founder")
- Tool names ("claude code", "instantly ai", "apify")
- Brand ("agent founders", "chris lee")
- Competitor adjacent ("ai agency", "claude code tutorial 2026")

## Pinned comment

```
Get the full 5-mission roadmap + 3 core skills free: [CTA link]

Drop a comment if you have questions about this video. I read every one.
```

Short. CTA first line. Engagement ask second line. No em dashes.

## YouTube community post

```
[1-line hook. Same energy as the video title.]

[2-3 lines describing what the video covers. Concrete, not vague.]

[Call to action: "Link in the comments."]
```

4-5 lines total. Post this the same day you publish the video.

## Upload settings

- **Visibility**: Public (or Unlisted for review, then switch to Public)
- **Category**: Education (category ID 27)
- **Language**: English
- **Made for kids**: No
- **Paid promotion**: No
- **End screen**: Subscribe button (bottom-left) + next video card (bottom-right) at last 20 seconds
- **Cards**: Link to CTA page at the Outro timestamp
- **Playlist**: Add to the relevant mission playlist

## Publishing via YouTube MCP

If YouTube MCP is connected, the skill can upload directly:

1. `youtube_upload_video` with title, description, tags, category, privacy
2. `youtube_update_video` to add end screens and cards after upload
3. `youtube_post_comment` for the pinned comment

The student verifies the upload in YouTube Studio and pins the comment manually (MCP cannot pin).

## Post-publish checklist

- [ ] Title live and correct
- [ ] Thumbnail uploaded (student designs separately or uses Canva with the brief)
- [ ] Description has CTA links above the fold
- [ ] Timestamps match the actual video
- [ ] Pinned comment posted and pinned
- [ ] Community post published
- [ ] End screen cards active
- [ ] Added to playlist
- [ ] First 10 comments replied to within 2 hours of publish
