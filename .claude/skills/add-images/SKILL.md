---
name: add-images
description: Resize, auto-rotate, and strip metadata (including GPS) from photos for a blog post, saving them to resources/img/<slug>/ and printing Markdown image lines. Use whenever images are added to a post.
---

# Add images

Run the script; don't read or reimplement it. It prints one Markdown line per image and a
size summary, which is all you need.

```bash
python3 -I .claude/skills/add-images/process_images.py <slug> <file-or-folder> [...]
```

- `<slug>` is the post slug; output goes to `resources/img/<slug>/`.
- Accepts jpg, jpeg, heic/heif (iPhone), tif, webp, png. Photos become JPEG; PNGs
  (screenshots, diagrams) stay PNG.
- Defaults: 1400 px long side, 2200 px for panoramas (wider than 2:1), JPEG quality 70.
  Override with `--max`, `--pano-max`, `--quality` only if asked.
- Rotation from phone EXIF is baked into the pixels, then **all metadata is stripped**
  (GPS, camera, timestamps).
- File names are lowercased and made URL-safe; existing names get `-2`, `-3`.
- `--strip-only` re-strips everything already in `resources/img/<slug>/` without resizing.

After running:
- Replace the `alt` text in the printed lines with a short description of each photo.
- For side-by-side photos with text, append `{: style='width:50%; float:right'}`.
- Never hotlink images from Google Drive, Google Photos, or similar; they stop working.

macOS only (uses `sips`). The originals are left untouched.
