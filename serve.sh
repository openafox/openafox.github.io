#!/bin/sh
# Serve the site locally at http://localhost:4000 using Docker (no local Ruby needed).
# Gems are cached in the "openafox-gems" volume, so only the first run is slow.
# Pass extra jekyll flags through, e.g. ./serve.sh --drafts
exec docker run --rm -it \
  -p 4000:4000 -p 35729:35729 \
  -v "$PWD":/site -w /site \
  -v openafox-gems:/usr/local/bundle \
  ruby:3.3 \
  sh -c 'bundle install --quiet && bundle exec jekyll serve --host 0.0.0.0 --livereload --force_polling "$@"' -- "$@"
