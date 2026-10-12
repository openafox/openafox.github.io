# openafox.com

Austin Fox's personal site and notes, built with [Jekyll](https://jekyllrb.com) and
hosted on GitHub Pages at https://openafox.com. Pushing to `master` publishes the site.

The theme is a customized copy of [codinfox-lanyon](https://github.com/codinfox/codinfox-lanyon)
(based on [Lanyon](https://github.com/poole/lanyon)).

## Run it locally

Requires [Docker Desktop](https://www.docker.com/products/docker-desktop/) (no local Ruby needed).

```bash
./serve.sh
```

Then open http://localhost:4000. Pages rebuild and the browser reloads when files change.
To also show unpublished posts in `_drafts/`:

```bash
./serve.sh --drafts
```

The first run downloads the Ruby image and gems (a few minutes); they are cached in the
`openafox-gems` Docker volume after that. To force a clean reinstall:

```bash
docker volume rm openafox-gems
```

## Writing a post

Create `_posts/<category>/YYYY-MM-DD-slug.md` (or start it in `_drafts/slug.md`):

```markdown
---
layout: post
title: My Post Title
category: Programming
tag: Web Dev
excerpt: One-line summary shown in listings.
---

Body in GitHub-flavored Markdown. Math goes in $$ ... $$.
Images go in resources/img/ and are referenced as /resources/img/name.png.
```

## Analytics (Google Analytics 4)

1. In [Google Analytics](https://analytics.google.com), open **Admin → Data streams** and
   pick (or create) the web stream for `openafox.com`.
2. Copy its **Measurement ID** (`G-XXXXXXXXXX`).
3. Set it in `_config.yml`:

   ```yaml
   google_analytics_token: G-XXXXXXXXXX
   ```

Leave it blank to turn analytics off.

## Comments (giscus)

Comments use [giscus](https://giscus.app), which stores them in this repo's GitHub
Discussions. They are off until both IDs below are set.

1. In the repo's **Settings → General → Features**, enable **Discussions**, and create a
   discussion category named `Comments` (type: Announcement, so only giscus can create threads).
2. Install the [giscus GitHub app](https://github.com/apps/giscus) on this repo.
3. On [giscus.app](https://giscus.app), enter `openafox/openafox.github.io`, choose the
   `Comments` category, and copy `data-repo-id` and `data-category-id` from the generated snippet.
4. Fill them in under `giscus:` in `_config.yml`.

## License

Posts and other content are [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Theme code is MIT; see [LICENSE.md](LICENSE.md).
