#!/usr/bin/env python3
"""Mechanical pre-push scan of posts for secrets, PII, and GPS-tagged images.

Usage: scan.py <post.md> [...]
Prints findings as `path:line: [kind] snippet`. Exit code 1 if anything was found.
Flags only; a human decides. Judgment checks (tone, private people, etc.) are in SKILL.md.
"""
import os
import re
import struct
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

# Addresses that are fine to appear publicly
ALLOWED_EMAILS = {'openafox@gmail.com'}
ALLOWED_EMAIL_DOMAINS = {'example.com', 'users.noreply.github.com', 'noreply.github.com'}

SECRET_PATTERNS = [
    ('aws-key', r'\bAKIA[0-9A-Z]{16}\b'),
    ('github-token', r'\b(gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{22,})\b'),
    ('anthropic/openai-key', r'\bsk-(ant-)?[A-Za-z0-9_-]{20,}'),
    ('slack-token', r'\bxox[abprs]-[A-Za-z0-9-]{10,}'),
    ('google-api-key', r'\bAIza[0-9A-Za-z_-]{35}\b'),
    ('private-key', r'-----BEGIN [A-Z ]*PRIVATE KEY-----'),
    ('credential-assignment',
     r'(?i)\b(password|passwd|pwd|secret|token|api[_-]?key|access[_-]?key)\b\s*[:=]\s*["\']?[^\s"\'<>]{6,}'),
    ('url-with-credentials', r'\b[a-z][a-z0-9+.-]*://[^/\s:@]+:[^/\s@]+@'),
]

PII_PATTERNS = [
    ('email', r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'),
    ('phone', r'(?<![\d.])(\+?1[ .-]?)?\(?\b\d{3}\)?[ .-]\d{3}[ .-]\d{4}\b'),
    ('street-address',
     r'\b\d{1,5}\s+(?:[A-Z][a-z]+\s+){1,3}(?:St|Street|Ave|Avenue|Rd|Road|Blvd|Dr|Drive|Ln|Lane|Way|Ct|Court|Pl|Place)\b\.?'),
    ('gps-coordinates', r'-?\b\d{1,2}\.\d{4,}\s*,\s*-?\d{1,3}\.\d{4,}\b'),
    ('ssn', r'\b\d{3}-\d{2}-\d{4}\b'),
    ('private-ip', r'\b(10\.\d{1,3}|192\.168|172\.(1[6-9]|2\d|3[01]))\.\d{1,3}\.\d{1,3}\b'),
    ('editable-share-link', r'https://docs\.google\.com/[^\s)]*/edit[^\s)]*'),
    ('drive-link', r'https://drive\.google\.com/[^\s)]+'),
]

IMG_REF = re.compile(r'(/resources/img/[^\s)"\']+)')


def email_ok(addr):
    addr = addr.lower()
    return addr in ALLOWED_EMAILS or addr.split('@', 1)[1] in ALLOWED_EMAIL_DOMAINS


def jpeg_has_gps(path):
    with open(path, 'rb') as f:
        data = f.read()
    if data[:2] != b'\xFF\xD8':
        return False
    i = 2
    while i + 4 <= len(data) and data[i] == 0xFF and data[i + 1] != 0xDA:
        length = struct.unpack('>H', data[i + 2:i + 4])[0]
        seg = data[i + 4:i + 2 + length]
        if data[i + 1] == 0xE1 and seg[:6] == b'Exif\x00\x00':
            t = seg[6:]
            e = '<' if t[:2] == b'II' else '>'
            off = struct.unpack(e + 'I', t[4:8])[0]
            n = struct.unpack(e + 'H', t[off:off + 2])[0]
            for k in range(n):
                if struct.unpack(e + 'H', t[off + 2 + 12 * k:off + 4 + 12 * k])[0] == 0x8825:
                    return True
        i += 2 + length
    return False


def scan(path):
    findings = []
    with open(path, encoding='utf-8', errors='replace') as f:
        lines = f.read().splitlines()
    for n, line in enumerate(lines, 1):
        for kind, pat in SECRET_PATTERNS + PII_PATTERNS:
            for m in re.finditer(pat, line):
                if kind == 'email' and email_ok(m.group(0)):
                    continue
                findings.append((n, kind, m.group(0)[:80]))
        for m in IMG_REF.finditer(line):
            img = os.path.join(REPO, m.group(1).lstrip('/'))
            if not os.path.exists(img):
                findings.append((n, 'missing-image', m.group(1)))
            elif img.lower().endswith(('.jpg', '.jpeg')) and jpeg_has_gps(img):
                findings.append((n, 'image-has-gps', m.group(1)))
    return findings


def main():
    total = 0
    for path in sys.argv[1:]:
        for n, kind, snippet in scan(path):
            print(f'{path}:{n}: [{kind}] {snippet}')
            total += 1
    print(f'{total} finding(s) in {len(sys.argv) - 1} file(s)')
    sys.exit(1 if total else 0)


if __name__ == '__main__':
    main()
