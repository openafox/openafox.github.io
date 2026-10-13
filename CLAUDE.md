# openafox.com

Personal blog/knowledge base for Austin Fox. Jekyll site built by GitHub Pages
(`github-pages` gem) from `master`, served at https://openafox.com (see `CNAME`).
Theme is a customized fork of codinfox-lanyon, vendored in `_layouts/`, `_includes/`, `_scss/`.

## Running locally

Uses Docker so no local Ruby is needed (system Ruby on this Mac is 2.6, too old):

```bash
./serve.sh            # http://localhost:4000, live reload
./serve.sh --drafts   # also render _drafts/
```

Docker Desktop must be running (`open -a Docker`). Gems are cached in the
`openafox-gems` Docker volume; `docker volume rm openafox-gems` forces a clean install.
`Gemfile.lock` is gitignored: GitHub Pages pins its own versions.

## Writing posts

Project skills in `.claude/skills/` handle the workflow: `/new-post` (draft from rough
notes, voice guide in `new-post/voice.md`), `/add-images` (resize + strip GPS via script),
`/publish` (date, build, push to master), `/idea` (append to `IDEAS.md`), and
`/check-post` (secrets/PII/tone scan). The repo is public: drafts are pushed (they never
appear on the site), so check-post runs before every draft or post commit.


- Posts live in `_posts/<category-folder>/YYYY-MM-DD-slug.md`; work in progress goes in `_drafts/`.
- Front matter: `layout: post`, `title`, `category`, `tag` (or `tags`), optional `excerpt`.
- Permalinks come out as `/<category>/<slug>.html`.
- Math: write `$$...$$` (kramdown turns it into MathJax inline/display). Single `$` is
  deliberately *not* math so prices like `$20` render as text.
- Images: put them in `resources/img/` and reference `/resources/img/name.png`.
  Many 2017 posts hotlink Google Drive (`drive.google.com/uc?id=...`) images, which no
  longer render; don't add new ones that way.

## Config notes

- `google_analytics_token` in `_config.yml` expects a GA4 `G-...` ID; blank disables it.
- Comments use giscus (GitHub Discussions); off until `giscus.repo_id`/`category_id` are set.
- Setup steps for analytics and comments are in `README.md`.
