---
name: publish
description: Publish a draft from _drafts/ to the live openafox.com site - date it, move it into _posts/, verify the build, commit and push to master. Use when Austin says to publish or post a draft.
---

# Publish

Austin invoking this is the go-ahead to push to the live site. Stop and ask only if a
check below fails.

## Checks (stop and report if any fail)
1. Which draft? If more than one is in `_drafts/` and he didn't say, ask.
2. No `**TODO:**` markers left: `grep -n 'TODO' _drafts/<slug>.md`.
3. Front matter has `title`, `category`, and `excerpt`.
4. Every `/resources/img/...` path in the post exists on disk.
5. Current branch is `master` and clean apart from this post and its images. If not, ask.

## Publish
1. Move it, using today's date and the category folder (lowercase). Drafts are
   gitignored, so use plain `mv`:
   `mkdir -p _posts/<category> && mv _drafts/<slug>.md _posts/<category>/YYYY-MM-DD-<slug>.md`
2. Build to confirm it renders:
   ```bash
   docker run --rm -v "$PWD":/site -w /site -v openafox-gems:/usr/local/bundle ruby:3.3 \
     sh -c 'bundle install --quiet && bundle exec jekyll build --quiet'
   ```
   (If Docker isn't running: `open -a Docker`, then wait for `docker info` to succeed.)
3. Commit the post and its `resources/img/<slug>/` folder:
   `Add post: <title>`, then push to `origin master`.
4. Reply with the live URL, `https://openafox.com/<category>/<slug>.html`, noting that
   GitHub Pages usually takes a minute or two to update.

## Updating a published tech note
Edit it in place, set `last_updated: YYYY-MM-DD` in the front matter, keep the original
filename and date, then build, commit (`Update post: <title>`) and push.
