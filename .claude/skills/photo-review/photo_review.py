#!/usr/bin/env python3
"""Pick and place photos for blog posts with a local review page.

  prepare  Read photos (folder or .zip) and posts, match photos to posts by time, auto-pick a few
           per post, make thumbnails, and write the review page into a work folder.
  serve    Serve the review page on http://127.0.0.1:<port>/ ; every click is saved to state.json.
  apply    Resize + strip the chosen photos into the site and insert a photo grid into each post.

Posts come from either:
  --posts '<glob>'   existing Jekyll posts; a photo belongs to the first post dated at/after it
                     (posts written in the evening about that day). Use --shift-hours if the
                     post timestamps are in a different time zone than the camera clock.
  --plan plan.json   posts not written yet: [{"slug", "title", "start": "YYYY-MM-DD",
                     "end": "YYYY-MM-DD", "where": "...", "text": "..."}]; a photo belongs to the
                     post whose date range covers its day (photos before --day-starts count as
                     the previous day).

Standard library only, plus macOS `sips` via the add-images skill for thumbnails and output.
"""
import argparse
import datetime as dt
import glob
import html
import http.server
import json
import os
import re
import shutil
import struct
import sys
import types
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(HERE, '..', 'add-images'))
import process_images as pi  # noqa: E402  (resize, rotation, metadata stripping)

PHOTO_EXT = {'.jpg', '.jpeg', '.heic', '.heif', '.png', '.tif', '.tiff', '.webp'}

# Words that start sentences or are too common to be useful as "people & places" hints
STOP = set('''I We The A An It It's Its This That Then There They Today Tomorrow Tonight Yesterday After
Before When While Once So But And Or Oh Ok Okay Well Our My Me He She His Her Him Them Their In On At Of To
For From With By As Into Out Up Down Over Under About Around Through Thanks Thank Sorry Also Again Soon
Luckily Eventually Later Lunch Breakfast Dinner Supper Morning Evening Night Day Week Miles Total Hope
Hopefully Not No Yes Some Most Many All One Two Three Ps Being Since Because If Just Even Still Now Already
Here Where Why How What Who Which Haha Love Glad Got Had Went Made Did Do Was Were Are Is Be Been Have Has
Get Go Going Left Right Along Instead Overall Apparently Both Another Other First Second Next Last Great
Good Nice Long Short Little Big Fun Plan Trip Road Ride Bike Rain Wind Weather Mr Mrs Ms Everyone Someone
Nothing Something Everything Each Every Very Really Quite Pretty Too More Less Much Few Several Lots Lot
Let Lets You Your Any Without Though Although Anyway Maybe Probably Only Plus Shortly Finally Sadly
Actually Monday Tuesday Wednesday Thursday Friday Saturday Sunday January February March April May June
July August September October November December Found Walked Biked Ate Bought Stopped Decided Ended
Took Grabbed Saw Had Put Laid Early Lots Long Quick'''.split())


# ---------- EXIF ----------

def exif_datetime(path):
    """DateTimeOriginal (or DateTime) as naive datetime, or None."""
    try:
        with open(path, 'rb') as f:
            d = f.read(256 * 1024)
        i = d.find(b'Exif\x00\x00')
        if i < 0:
            return None
        t = d[i + 6:]
        e = '<' if t[:2] == b'II' else '>'

        def ifd(off):
            n = struct.unpack(e + 'H', t[off:off + 2])[0]
            return {struct.unpack(e + 'H', t[off + 2 + 12 * k:off + 4 + 12 * k])[0]:
                    t[off + 2 + 12 * k:off + 14 + 12 * k] for k in range(n)}

        def ascii_val(ent):
            cnt = struct.unpack(e + 'I', ent[4:8])[0]
            off = struct.unpack(e + 'I', ent[8:12])[0]
            return t[off:off + cnt].rstrip(b'\x00').decode(errors='replace')

        root = ifd(struct.unpack(e + 'I', t[4:8])[0])
        val = None
        if 0x8769 in root:
            sub = ifd(struct.unpack(e + 'I', root[0x8769][8:12])[0])
            if 0x9003 in sub:
                val = ascii_val(sub[0x9003])
        if not val and 0x0132 in root:
            val = ascii_val(root[0x0132])
        return dt.datetime.strptime(val[:19], '%Y:%m:%d %H:%M:%S') if val else None
    except Exception:
        return None


# ---------- posts ----------

def read_front_matter(path):
    s = open(path, encoding='utf-8').read()
    m = re.match(r'---\n(.*?)\n---\n(.*)', s, re.S)
    fm, body = (m.group(1), m.group(2)) if m else ('', s)
    meta = {}
    for line in fm.splitlines():
        mm = re.match(r'^(\w+):\s*(.*)$', line)
        if mm:
            v = mm.group(2).strip()
            if v.startswith('"') and v.endswith('"'):
                try:
                    v = json.loads(v)
                except ValueError:
                    v = v.strip('"')
            meta[mm.group(1)] = v.strip("'")
    return meta, body


def plain_text(body):
    body = re.sub(r'<div class="photo-grid">.*?</div>', ' ', body, flags=re.S)
    body = re.split(r'\n## Comments\n', body)[0]
    body = re.sub(r'!\[[^\]]*\]\([^)]*\)(\{[^}]*\})?', ' ', body)
    body = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', body)
    body = re.sub(r'<[^>]+>|[#*_>`]', ' ', body)
    return ' '.join(html.unescape(body).split())


def mentions(text):
    found = []
    for m in re.finditer(r"\b([A-Z][a-z'’-]+(?:\s+(?:[A-Z][a-z'’-]+|de|of|the))*)", text):
        w = re.sub(r"['’]s$", '', m.group(1).strip())
        if w.split()[0] in STOP or len(w) < 3 or w in found:
            continue
        found.append(w)
    return found[:25]


def load_posts(args):
    posts = []
    if args.plan:
        for p in json.load(open(args.plan)):
            text = p.get('text', '')
            posts.append({'slug': p['slug'], 'title': p.get('title', p['slug']), 'file': p.get('file', ''),
                          'start': p['start'], 'end': p.get('end', p['start']), 'where': p.get('where', ''),
                          'text': text, 'mentions': p.get('mentions') or mentions(text)})
        posts.sort(key=lambda p: p['start'])
        return posts
    for f in sorted(glob.glob(args.posts)):
        meta, body = read_front_matter(f)
        slug = re.sub(r'^\d{4}-\d\d-\d\d-', '', os.path.splitext(os.path.basename(f))[0])
        date = meta.get('date') or os.path.basename(f)[:10]
        when = dt.datetime.strptime(date[:19] if len(date) >= 16 else date[:10] + ' 23:59:00',
                                    '%Y-%m-%d %H:%M:%S' if len(date) >= 19 else
                                    ('%Y-%m-%d %H:%M' if len(date) >= 16 else '%Y-%m-%d %H:%M:%S'))
        when += dt.timedelta(hours=args.shift_hours)
        text = plain_text(body)
        posts.append({'slug': slug, 'title': meta.get('title', slug), 'file': os.path.relpath(f, REPO),
                      'published': when.isoformat(timespec='minutes'), 'where': meta.get('where', ''),
                      'text': text, 'mentions': mentions(text)})
    posts.sort(key=lambda p: p['published'])
    return posts


def home_post(t, posts, args):
    """Which post a photo taken at naive local time t belongs to."""
    if args.plan:
        day = (t - dt.timedelta(hours=args.day_starts)).date().isoformat()
        for p in posts:
            if p['start'] <= day <= p['end']:
                return p['slug']
        return None
    for p in posts:
        if dt.datetime.fromisoformat(p['published']) >= t:
            return p['slug']
    return posts[-1]['slug'] if posts else None


# ---------- prepare ----------

def collect_photos(src, work):
    if src.lower().endswith('.zip'):
        dest = os.path.join(work, 'originals')
        with zipfile.ZipFile(src) as z:
            for n in z.namelist():
                if n.startswith('/') or '..' in n.split('/'):
                    sys.exit(f'refusing unsafe path in zip: {n}')
            z.extractall(dest)
        src = dest
    files = []
    for root, _, names in os.walk(src):
        for n in names:
            if os.path.splitext(n)[1].lower() in PHOTO_EXT and not n.startswith('._'):
                files.append(os.path.join(root, n))
    return sorted(files)


def auto_pick(photos, n):
    """Spread n picks across the time range, skipping bursts (<90 s apart), preferring bigger files."""
    groups = []
    for p in photos:
        if groups and p['t'] and groups[-1][-1]['t'] and \
                (dt.datetime.fromisoformat(p['t']) - dt.datetime.fromisoformat(groups[-1][-1]['t'])).total_seconds() < 90:
            groups[-1].append(p)
        else:
            groups.append([p])
    best = [max(g, key=lambda p: p['size']) for g in groups]
    if len(best) <= n:
        return [p['id'] for p in best]
    k = len(best)
    return [max(best[i * k // n:(i + 1) * k // n], key=lambda p: p['size'])['id'] for i in range(n)]


def prepare(args):
    work = os.path.abspath(args.work)
    os.makedirs(os.path.join(work, 'thumbs'), exist_ok=True)
    posts = load_posts(args)
    if not posts:
        sys.exit('no posts found')
    files = collect_photos(os.path.abspath(args.photos), work)
    photos, thumb_args = {}, types.SimpleNamespace(max=360, pano_max=640, quality=60)
    for i, f in enumerate(files):
        pid = f'p{i:04d}'
        t = exif_datetime(f)
        thumb = os.path.join(work, 'thumbs', pid + ('.png' if f.lower().endswith('.png') else '.jpg'))
        if not os.path.exists(thumb):
            try:
                pi.process(f, thumb, thumb_args)
            except Exception as ex:
                print('skip (cannot read):', os.path.basename(f), ex)
                continue
        photos[pid] = {'id': pid, 'src': f, 'name': os.path.basename(f), 'thumb': 'thumbs/' + os.path.basename(thumb),
                       't': t.isoformat(timespec='minutes') if t else '', 'size': os.path.getsize(f)}
        photos[pid]['home'] = home_post(t, posts, args) if t else None
    by_home = {}
    for p in sorted(photos.values(), key=lambda p: p['t']):
        by_home.setdefault(p['home'], []).append(p)
    placement = {p['slug']: auto_pick(by_home.get(p['slug'], []), args.per_post) for p in posts}
    data = {'posts': posts, 'photos': photos}
    json.dump(data, open(os.path.join(work, 'data.json'), 'w'), indent=1)
    state = os.path.join(work, 'state.json')
    if not os.path.exists(state) or args.reset:
        json.dump({'placement': placement, 'auto': placement}, open(state, 'w'), indent=1)
    shutil.copyfile(os.path.join(HERE, 'review.html'), os.path.join(work, 'index.html'))
    dated = sum(1 for p in photos.values() if p['t'])
    placed = sum(1 for p in photos.values() if p['home'])
    print(f'{len(photos)} photos ({dated} dated, {placed} matched to a post, '
          f'{len(photos) - placed} unsorted), {len(posts)} posts, '
          f'{sum(map(len, placement.values()))} auto-picked')
    print(f'work folder: {work}\nnext: python3 -I {os.path.relpath(__file__, REPO)} serve --work {args.work}')


# ---------- serve ----------

def serve(args):
    work = os.path.abspath(args.work)

    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *a, **k):
            super().__init__(*a, directory=work, **k)

        def log_message(self, *a):
            pass

        def end_headers(self):
            self.send_header('Cache-Control', 'no-store')
            super().end_headers()

        def do_POST(self):
            if self.path != '/state':
                self.send_error(404)
                return
            body = self.rfile.read(min(int(self.headers.get('Content-Length', 0)), 5_000_000))
            new = json.loads(body)
            if not isinstance(new.get('placement'), dict):
                self.send_error(400)
                return
            path = os.path.join(work, 'state.json')
            state = json.load(open(path))
            state['placement'] = new['placement']
            state['saved'] = dt.datetime.now().isoformat(timespec='seconds')
            tmp = path + '.tmp'
            json.dump(state, open(tmp, 'w'), indent=1)
            os.replace(tmp, path)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'ok')

    print(f'Review page: http://127.0.0.1:{args.port}/   (Ctrl+C to stop)')
    http.server.ThreadingHTTPServer(('127.0.0.1', args.port), Handler).serve_forever()


# ---------- apply ----------

def grid_html(names, img_url, title):
    figs = '\n'.join(f'  <a href="{img_url}/{n}"><img src="{img_url}/{n}" '
                     f'alt="{html.escape(title)}, photo {i}" loading="lazy"></a>'
                     for i, n in enumerate(names, 1))
    return f'<div class="photo-grid">\n{figs}\n</div>\n'


def insert_grid(path, grid):
    s = open(path, encoding='utf-8').read()
    s = re.sub(r'\n?<div class="photo-grid">.*?</div>\n', '', s, flags=re.S)
    if grid:
        if '\n## Comments\n' in s:
            s = s.replace('\n## Comments\n', '\n' + grid + '\n## Comments\n', 1)
        else:
            s = s.rstrip('\n') + '\n\n' + grid
    open(path, 'w', encoding='utf-8').write(s)


def apply(args):
    work = os.path.abspath(args.work)
    data = json.load(open(os.path.join(work, 'data.json')))
    placement = json.load(open(os.path.join(work, 'state.json')))['placement']
    photos, posts = data['photos'], data['posts']
    stage = os.path.join(work, 'stage')
    shutil.rmtree(stage, ignore_errors=True)
    os.makedirs(stage)
    names = {}
    for p in posts:
        ids = sorted(placement.get(p['slug'], []), key=lambda i: photos[i]['t'] or '~')
        for n, pid in enumerate(ids, 1):
            src = photos[pid]['src']
            name = f"{p['slug']}-{n:02d}" + ('.png' if src.lower().endswith('.png') else '.jpg')
            shutil.copyfile(src, os.path.join(stage, name))
            names.setdefault(p['slug'], []).append(name)
    out_dir = os.path.join(REPO, 'resources', 'img', args.img_slug)
    if os.path.isdir(out_dir) and args.replace:
        for f in os.listdir(out_dir):
            os.remove(os.path.join(out_dir, f))
    os.makedirs(out_dir, exist_ok=True)
    opts = types.SimpleNamespace(max=args.max, pano_max=args.pano_max, quality=args.quality)
    total = 0
    for slug, ns in names.items():
        for n in ns:
            dest = os.path.join(out_dir, n)
            pi.process(os.path.join(stage, n), dest, opts)
            total += os.path.getsize(dest)
    img_url = f'/resources/img/{args.img_slug}'
    written, snippets = 0, os.path.join(work, 'grids')
    os.makedirs(snippets, exist_ok=True)
    for p in posts:
        grid = grid_html(names.get(p['slug'], []), img_url, p['title']) if names.get(p['slug']) else ''
        open(os.path.join(snippets, p['slug'] + '.html'), 'w').write(grid)
        target = p.get('file') and os.path.join(REPO, p['file'])
        if target and os.path.exists(target):
            insert_grid(target, grid)
            written += 1
    print(f'{sum(map(len, names.values()))} photos -> {img_url}/ ({total / 1e6:.1f} MB, metadata stripped); '
          f'grids written into {written} posts; snippets in {snippets}/')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    a = sub.add_parser('prepare')
    a.add_argument('--photos', required=True, help='folder or .zip of photos')
    src = a.add_mutually_exclusive_group(required=True)
    src.add_argument('--posts', help="glob of existing posts, e.g. '_posts/bike-tour/*.md'")
    src.add_argument('--plan', help='JSON list of planned posts with start/end dates')
    a.add_argument('--work', required=True, help='work folder (keep it outside the repo)')
    a.add_argument('--per-post', type=int, default=3)
    a.add_argument('--shift-hours', type=float, default=0, help='added to post times (--posts mode)')
    a.add_argument('--day-starts', type=int, default=4, help='hour a new day starts (--plan mode)')
    a.add_argument('--reset', action='store_true', help='discard saved picks and start from auto-picks')
    s = sub.add_parser('serve')
    s.add_argument('--work', required=True)
    s.add_argument('--port', type=int, default=8765)
    p = sub.add_parser('apply')
    p.add_argument('--work', required=True)
    p.add_argument('--img-slug', required=True, help='folder under resources/img/')
    p.add_argument('--max', type=int, default=1200)
    p.add_argument('--pano-max', type=int, default=2200)
    p.add_argument('--quality', type=int, default=70)
    p.add_argument('--replace', action='store_true', help='empty resources/img/<img-slug>/ first')
    args = ap.parse_args()
    {'prepare': prepare, 'serve': serve, 'apply': apply}[args.cmd](args)


if __name__ == '__main__':
    main()
