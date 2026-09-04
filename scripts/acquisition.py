#!/usr/bin/env python3
"""Tier A acquisition — Daily Krishna Stories Milestone 1."""
import os, sys, time, hashlib, json, urllib.request

BASE = os.path.expanduser('~/Documents/projects/indian_apps/dailyX/daily_krishna_stories/sources/raw')
UA = {'User-Agent': 'Mozilla/5.0 (research corpus acquisition; non-commercial)'}

def fetch(url, dest, timeout=300):
    if os.path.exists(dest) and os.path.getsize(dest) > 1000:
        print(f'skip (exists): {dest}'); return 'exists'
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    req = urllib.request.Request(url, headers=UA)
    print(f'GET {url}')
    with urllib.request.urlopen(req, timeout=timeout) as r, open(dest, 'wb') as f:
        while True:
            chunk = r.read(1 << 20)
            if not chunk: break
            f.write(chunk)
    sz = os.path.getsize(dest)
    print(f'  -> {dest} ({sz} bytes)')
    return 'ok'

def sha256(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()

jobs = [
    # Mahabharata — Ganguli via Project Gutenberg (all volumes, dedupe later by content)
    ('https://www.gutenberg.org/cache/epub/7864/pg7864.txt',  'mahabharata/pg7864.txt'),
    ('https://www.gutenberg.org/cache/epub/7965/pg7965.txt',  'mahabharata/pg7965.txt'),
    ('https://www.gutenberg.org/cache/epub/11894/pg11894.txt','mahabharata/pg11894.txt'),
    ('https://www.gutenberg.org/cache/epub/12058/pg12058.txt','mahabharata/pg12058.txt'),
    ('https://www.gutenberg.org/cache/epub/12333/pg12333.txt','mahabharata/pg12333.txt'),
    ('https://www.gutenberg.org/cache/epub/15474/pg15474.txt','mahabharata/pg15474.txt'),
    ('https://www.gutenberg.org/cache/epub/15475/pg15475.txt','mahabharata/pg15475.txt'),
    ('https://www.gutenberg.org/cache/epub/15476/pg15476.txt','mahabharata/pg15476.txt'),
    ('https://www.gutenberg.org/cache/epub/15477/pg15477.txt','mahabharata/pg15477.txt'),
    # Vishnu Purana — Wilson 1840, clean epub digitization on archive.org
    ('https://archive.org/download/thevishnupuranacomplete6bookssethoracehaymanwilson/The%20Vishnu%20Purana%20(Complete%206%20Books%20Set)%20-%20Horace%20Hayman%20Wilson.epub',
     'vishnu_purana/wilson_vishnupurana_1840.epub'),
    ('https://archive.org/download/thevishnupuranacomplete6bookssethoracehaymanwilson/The%20Vishnu%20Purana%20(Complete%206%20Books%20Set)%20-%20Horace%20Hayman%20Wilson_djvu.txt',
     'vishnu_purana/wilson_vishnupurana_1840_djvu.txt'),
    # Srimadbhagabatam — M.N. Dutt, archive.org OCR volumes (Books 1-2, 7-12)
    ('https://archive.org/download/proseenglishtran12dutt/proseenglishtran12dutt_djvu.txt',
     'bhagavata/dutt_srimadbhagabatam_books1-2_djvu.txt'),
    ('https://archive.org/download/india.history.resource.40625/40625_djvu.txt',
     'bhagavata/dutt_srimadbhagabatam_books7-12_djvu.txt'),
]

ok, fail = [], []
for url, rel in jobs:
    dest = os.path.join(BASE, rel)
    try:
        st = fetch(url, dest)
        ok.append(rel)
    except Exception as e:
        fail.append((rel, str(e)))
        print(f'FAIL {rel}: {e}', file=sys.stderr)
    time.sleep(0.4)

print('\n=== SUMMARY ===')
for rel in ok:
    dest = os.path.join(BASE, rel)
    print(f'{sha256(dest)[:16]}  {os.path.getsize(dest):>10}  {rel}')
if fail:
    print('FAILED:')
    for rel, e in fail: print('  ', rel, e)
print('done')
