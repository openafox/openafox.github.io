---
name: photo-review
description: Choose which photos go in which blog posts when there are far too many (a trip album, a project's build photos). Matches photos to posts by timestamp, auto-picks a few per post, and gives Austin a local review page to add, remove, and move photos between posts; then resizes, strips metadata, and inserts photo grids. Use for any batch of photos spanning several posts.
---

# Photo review

For hundreds of photos across a series of posts. The person makes every judgment call on a
local page; the script does the matching, thumbnails, saving, and output.

## 1. Prepare

Photos can be a folder or a `.zip` (e.g. a Google Photos "Download all"). Keep the work folder
**outside the repo** (it holds originals with GPS); the session scratchpad is a good place.

Existing posts (a photo goes to the first post dated at or after it, since posts were usually
written that evening):

```bash
python3 -I .claude/skills/photo-review/photo_review.py prepare \
  --photos ~/Downloads/album.zip --posts '_posts/bike-tour/2012-*.md' \
  --work <scratch>/review-biketour --shift-hours 2
```

- `--shift-hours`: add to post timestamps when the posts' time zone differs from the camera
  clock (e.g. posts stamped Pacific, photos taken in Central: `2`).
- Posts published together after a gap (no service for days) all grab the first post's photos;
  fix those on the page, or use a plan for that stretch.

Posts not written yet: write a plan JSON (one entry per planned post) and use `--plan`:

```json
[{"slug": "kyoto", "title": "Kyoto by bike", "start": "2017-08-28", "end": "2017-08-30",
  "where": "Kyoto", "text": "Notes for the day: Nishiki market, Daisen-in, Fushimi Inari…",
  "file": "_drafts/kyoto.md"}]
```

A photo goes to the post whose date range covers its day; before `--day-starts` (default 4 am)
counts as the previous day. `file` is optional: where `apply` should insert the grid.

Other options: `--per-post 3` (auto-picks per post), `--reset` (discard saved choices).

## 2. Review (the person does this)

```bash
python3 -I .claude/skills/photo-review/photo_review.py serve --work <work>
```

Run it in the background, open http://127.0.0.1:8765/ in the browser pane, and tell the person:

- Each post shows its title, dates, where, and people/places mentioned, with the **post or draft
  text beside its photos**, read live from the file (reload after editing a draft). Plan `text`
  appears as fold-out **Notes**; `**TODO…**` markers are highlighted.
- **On the blog:** ◀ / ▶ move a photo to the previous/next post, ✕ removes it.
- **More from this time:** the post's other photos; **+ add** puts one on the blog.
- **Orange** = taken before 11 am (often "leaving the host's house" shots that belong to the
  previous post). **Blue outline** = moved away from the post its timestamp matched.
- Undated photos are at the bottom with an "add to…" menu.
- Every click saves to `<work>/state.json` immediately; any browser works, reloads are safe.

Read progress any time from `state.json` (`placement`: post slug → photo ids). Don't edit it
while the page is open.

## 3. Apply

```bash
python3 -I .claude/skills/photo-review/photo_review.py apply --work <work> --img-slug bike-tour-2012 --replace
```

- Copies chosen originals, names them `<post-slug>-NN.jpg` in time order, and processes them
  with the add-images skill (1200 px, rotation baked in, **all metadata incl. GPS stripped**).
- Inserts (or replaces) a `<div class="photo-grid">` before `## Comments` in each post file;
  grids for posts without a file are saved in `<work>/grids/<slug>.html`.
- `--replace` empties `resources/img/<img-slug>/` first, so re-running after more review
  leaves no stale files. Use `git add -A resources/img/<img-slug>` to stage deletions.

Then build, run check-post, commit. The site needs the `.photo-grid` CSS
(`_scss/component/_post.scss`).

## Notes

- Requires macOS (`sips`) and the add-images skill next to this one; otherwise stdlib only.
- Thumbnails are generated once and reused; a second `prepare` is fast.
- Only ~0.3% of old phone photos tend to have real GPS; don't plan maps around photo GPS.
- Stop the server when done (it's a background task).
