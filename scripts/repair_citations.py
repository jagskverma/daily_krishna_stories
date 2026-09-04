#!/usr/bin/env python3
"""Repair pass on raw mined events:
- HV citations pointing at chapter numbers absent from the corpus: re-cite to the
  nearest existing chapter whose text contains the source_excerpt's distinctive
  words; drop source_confidence to 3 and note the repair.
- BP verse_range exceeding the chapter's verse count: clamp to chapter max + note.
Output: repaired JSONL written back in place (idempotent; original kept as .bak).
"""
import os, re, json, glob, shutil

BASE = os.path.expanduser('~/Documents/projects/indian_apps/dailyX/daily_krishna_stories')
RAW = os.path.join(BASE, 'data/mining/raw_events')
REG = json.load(open(os.path.join(BASE, 'sources/normalized/registry.json')))

hv_files = {}   # (part, chapter) -> path
for r in REG:
    if r['work'] == 'harivamsa':
        hv_files[(r['part'], r['chapter'])] = os.path.join(BASE, 'sources/normalized', r['file'])
bp_verses = {}
for r in REG:
    if r['work'] == 'bhagavata_sanskrit':
        bp_verses[(r['canto'], r['chapter'])] = r['verses']

def num(x):
    try:
        return int(re.sub(r'\D', '', str(x)) or 0)
    except Exception:
        return 0

def hv_text(part, ch):
    p = hv_files.get((part, ch))
    if not p:
        return None
    return open(p, encoding='utf-8', errors='replace').read()

def find_hv_chapter(part, excerpt):
    """Find the existing chapter in `part` whose text contains the excerpt's words."""
    words = [w for w in re.findall(r"[A-Za-z]{5,}", (excerpt or '')) if w.lower() not in
             {'krishna', 'lord', 'said', 'would', 'shall', 'kansa', 'their', 'there', 'these', 'those',
              'having', 'being', 'which', 'whose', 'should', 'mount'}]
    if not words:
        return None
    best, best_score = None, 0
    for (p, c), path in hv_files.items():
        if p != part:
            continue
        t = open(path, encoding='utf-8', errors='replace').read().lower()
        score = sum(1 for w in words if w.lower() in t)
        if score > best_score:
            best, best_score = (p, c), score
    return best if best_score >= max(1, len(words) // 2) else None

repaired = []
for f in sorted(glob.glob(os.path.join(RAW, '*.jsonl'))):
    shutil.copy(f, f + '.bak')
    lines = open(f, encoding='utf-8').read().splitlines()
    out = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        ev = json.loads(line)
        ps = ev.get('primary_source', {})
        work = (ps.get('work') or '').lower()
        note = ev.get('notes') or ''
        if 'harivamsha' in work:
            part, ch = num(ps.get('book_or_canto')), num(ps.get('chapter_or_section'))
            if (part, ch) not in hv_files:
                target = find_hv_chapter(part, ev.get('source_excerpt'))
                if target:
                    ps['chapter_or_section'] = str(target[1])
                    ev['source_confidence'] = min(ev.get('source_confidence', 3), 3)
                    note = (note + ' | [citation-repair: ch %s absent from etext; re-cited to ch %s by content match]' % (ch, target[1])).strip()
                    ev['notes'] = note
                    repaired.append((ev.get('event_id'), f'HV {part}.{ch} -> {target[1]}'))
                else:
                    repaired.append((ev.get('event_id'), f'HV {part}.{ch} UNREPAIRABLE'))
        elif 'bhagavata' in work:
            c, ch = num(ps.get('book_or_canto')), num(ps.get('chapter_or_section'))
            vr = ps.get('verse_range') or ''
            if vr and (c, ch) in bp_verses:
                mx = max([num(m) for m in re.findall(r'\d+', vr)] or [0])
                if mx > bp_verses[(c, ch)]:
                    ps['verse_range'] = f'1-{bp_verses[(c, ch)]}'
                    ev['source_confidence'] = min(ev.get('source_confidence', 5), 4)
                    note = (note + f' | [citation-repair: verse_range clamped to chapter max {bp_verses[(c,ch)]}]').strip()
                    ev['notes'] = note
                    repaired.append((ev.get('event_id'), f'BP {c}.{ch} verse clamp'))
        out.append(json.dumps(ev, ensure_ascii=False))
    open(f, 'w', encoding='utf-8').write('\n'.join(out) + ('\n' if out else ''))

print('repairs:', len(repaired))
for r in repaired[:15]:
    print('  ', r)
