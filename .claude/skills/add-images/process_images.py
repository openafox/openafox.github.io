#!/usr/bin/env python3
"""Prepare images for a blog post: resize, fix rotation, strip metadata (incl. GPS).

Usage:
  process_images.py <slug> <file-or-dir> [...] [--max 1400] [--pano-max 2200] [--quality 70]
  process_images.py <slug> --strip-only            # re-strip resources/img/<slug>/ in place

Output goes to resources/img/<slug>/ with lowercase, URL-safe names. Prints one
Markdown image line per file plus a size summary. macOS only (uses `sips`); no
third-party packages.
"""
import argparse
import os
import re
import shutil
import struct
import subprocess
import sys
import tempfile

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PHOTO_EXT = {'.jpg', '.jpeg', '.heic', '.heif', '.tif', '.tiff', '.webp'}
PNG_EXT = {'.png'}

# EXIF orientation -> sips flags that bake it into the pixels
ORIENT_FIX = {
    2: ['-f', 'horizontal'], 3: ['-r', '180'], 4: ['-f', 'vertical'],
    5: ['-r', '90', '-f', 'horizontal'], 6: ['-r', '90'],
    7: ['-r', '270', '-f', 'horizontal'], 8: ['-r', '270'],
}

# JPEG segments to drop: APP1 (EXIF/XMP, where GPS lives), APP12, APP13 (IPTC), COM
JPEG_DROP = {0xE1, 0xEC, 0xED, 0xFE}
# PNG chunks to drop: EXIF and text/time metadata
PNG_DROP = {b'eXIf', b'tEXt', b'iTXt', b'zTXt', b'tIME'}


def jpeg_orientation(data):
    """Return the EXIF orientation (1-8) of a JPEG, or 1 if absent."""
    i = 2
    while i + 4 <= len(data) and data[i] == 0xFF:
        marker = data[i + 1]
        if marker == 0xDA:
            break
        length = struct.unpack('>H', data[i + 2:i + 4])[0]
        seg = data[i + 4:i + 2 + length]
        if marker == 0xE1 and seg[:6] == b'Exif\x00\x00':
            t = seg[6:]
            e = '<' if t[:2] == b'II' else '>'
            off = struct.unpack(e + 'I', t[4:8])[0]
            n = struct.unpack(e + 'H', t[off:off + 2])[0]
            for k in range(n):
                p = off + 2 + 12 * k
                tag, typ = struct.unpack(e + 'HH', t[p:p + 4])
                if tag == 0x0112:
                    return struct.unpack(e + 'H', t[p + 8:p + 10])[0]
        i += 2 + length
    return 1


def strip_jpeg(data):
    out, i = [data[:2]], 2
    while i + 4 <= len(data) and data[i] == 0xFF:
        marker = data[i + 1]
        if marker == 0xDA:  # start of scan: rest is image data
            break
        length = struct.unpack('>H', data[i + 2:i + 4])[0]
        if marker not in JPEG_DROP:
            out.append(data[i:i + 2 + length])
        i += 2 + length
    out.append(data[i:])
    return b''.join(out)


def strip_png(data):
    out, i = [data[:8]], 8
    while i < len(data):
        length = struct.unpack('>I', data[i:i + 4])[0]
        ctype = data[i + 4:i + 8]
        if ctype not in PNG_DROP:
            out.append(data[i:i + 12 + length])
        i += 12 + length
    return b''.join(out)


def strip_file(path):
    with open(path, 'rb') as f:
        data = f.read()
    if data[:2] == b'\xFF\xD8':
        data = strip_jpeg(data)
    elif data[:8] == b'\x89PNG\r\n\x1a\n':
        data = strip_png(data)
    else:
        sys.exit(f'unexpected format after conversion: {path}')
    with open(path, 'wb') as f:
        f.write(data)


def sips_size(path):
    out = subprocess.run(['sips', '-g', 'pixelWidth', '-g', 'pixelHeight', path],
                         capture_output=True, text=True, check=True).stdout
    w = int(re.search(r'pixelWidth: (\d+)', out).group(1))
    h = int(re.search(r'pixelHeight: (\d+)', out).group(1))
    return w, h


def safe_name(path, ext):
    stem = os.path.splitext(os.path.basename(path))[0].lower()
    stem = re.sub(r'[^a-z0-9._-]+', '-', stem).strip('-.') or 'image'
    return stem + ext


def unique(dest_dir, name, taken):
    stem, ext = os.path.splitext(name)
    candidate, n = name, 2
    while candidate in taken or os.path.exists(os.path.join(dest_dir, candidate)):
        candidate, n = f'{stem}-{n}{ext}', n + 1
    taken.add(candidate)
    return candidate


def process(src, dest, args):
    ext = os.path.splitext(src)[1].lower()
    is_png = ext in PNG_EXT
    with tempfile.TemporaryDirectory() as tmp:
        work = os.path.join(tmp, 'in' + ('.png' if is_png else '.jpg'))
        # Normalize to JPEG/PNG first so orientation can be read uniformly
        subprocess.run(['sips', '-s', 'format', 'png' if is_png else 'jpeg', src, '--out', work],
                       capture_output=True, check=True)
        if not is_png:
            # sips carries the EXIF orientation tag through conversion but does not apply it
            with open(work, 'rb') as f:
                orient = jpeg_orientation(f.read())
            if orient in ORIENT_FIX:
                subprocess.run(['sips', *ORIENT_FIX[orient], work], capture_output=True, check=True)
        w, h = sips_size(work)
        limit = args.pano_max if max(w, h) > 2 * min(w, h) else args.max
        cmd = ['sips', '-Z', str(limit)] if max(w, h) > limit else ['sips']
        if not is_png:
            cmd += ['-s', 'format', 'jpeg', '-s', 'formatOptions', str(args.quality)]
        if cmd == ['sips']:  # nothing to change; sips writes no output without an operation
            shutil.copyfile(work, dest)
        else:
            subprocess.run(cmd + [work, '--out', dest], capture_output=True, check=True)
    strip_file(dest)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('slug')
    ap.add_argument('inputs', nargs='*')
    ap.add_argument('--max', type=int, default=1400, help='long side in px (default 1400)')
    ap.add_argument('--pano-max', type=int, default=2200, help='long side for panoramas (>2:1)')
    ap.add_argument('--quality', type=int, default=70, help='JPEG quality 0-100 (default 70)')
    ap.add_argument('--strip-only', action='store_true',
                    help='only strip metadata from files already in resources/img/<slug>/')
    args = ap.parse_args()

    dest_dir = os.path.join(REPO, 'resources', 'img', args.slug)
    url_dir = f'/resources/img/{args.slug}'

    if args.strip_only:
        files = sorted(f for f in os.listdir(dest_dir)
                       if os.path.splitext(f)[1].lower() in {'.jpg', '.jpeg', '.png'})
        for f in files:
            strip_file(os.path.join(dest_dir, f))
        print(f'stripped metadata from {len(files)} files in {url_dir}/')
        return

    srcs = []
    for p in args.inputs:
        if os.path.isdir(p):
            srcs += sorted(os.path.join(p, f) for f in os.listdir(p))
        else:
            srcs.append(p)
    srcs = [s for s in srcs if os.path.splitext(s)[1].lower() in PHOTO_EXT | PNG_EXT]
    if not srcs:
        sys.exit('no images found (jpg, jpeg, heic, heif, tif, webp, png)')

    os.makedirs(dest_dir, exist_ok=True)
    taken, total = set(), 0
    for src in srcs:
        ext = '.png' if os.path.splitext(src)[1].lower() in PNG_EXT else '.jpg'
        name = unique(dest_dir, safe_name(src, ext), taken)
        dest = os.path.join(dest_dir, name)
        process(src, dest, args)
        size = os.path.getsize(dest)
        total += size
        w, h = sips_size(dest)
        alt = os.path.splitext(name)[0]
        print(f'![{alt}]({url_dir}/{name})  <!-- {w}x{h}, {size // 1024} KB -->')
    print(f'\n{len(srcs)} images -> {url_dir}/ ({total / 1e6:.1f} MB, metadata stripped)')


if __name__ == '__main__':
    main()
