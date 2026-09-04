#!/usr/bin/env python3
"""Build evidence packs for ALL corpus stories (full-corpus run).

Output: data/evidence_full/<DKS>.txt
Chain: full chronological order (index chronological_order), with the
documented birth-sequence fix (0018 crossing precedes 0015 girl-slaying).
Passage limit raised to 5000 chars to avoid mid-sentence truncation.
"""
import json, os, re

BASE = os.path.expanduser('~/Documents/projects/indian_apps/dailyX/daily_krishna_stories')
NORM = os.path.join(BASE, 'sources/normalized')
IDX = json.load(open(os.path.join(BASE, 'data/story_index.json')))
CANON = json.load(open(os.path.join(BASE, 'data/canonical_events.json')))
PILOT = json.load(open(os.path.join(BASE, 'data/pilot_story_selection.json')))

stories = {s['id']: s for s in IDX['stories']}
cids = {e['canonical_event_id']: e for e in CANON['events']}
pilot_ids = {s['id'] for s in PILOT['stories']}

# full chain in chronological order + the documented birth fix
order = sorted(stories.keys(), key=lambda i: stories[i]['chronological_order'])
# swap: put 0018 (Yamuna crossing, BP 10.3) before 0015 (girl-slaying, BP 10.4)
def fix_order(lst):
    if 'DKS_0015' in lst and 'DKS_0018' in lst:
        a, b = lst.index('DKS_0015'), lst.index('DKS_0018')
        if a < b:
            lst[a], lst[b] = lst[b], lst[a]
    return lst
order = fix_order(order)
chain = {order[i]: (order[i-1] if i > 0 else None, order[i+1] if i+1 < len(order) else None)
         for i in range(len(order))}

def num(x):
    try:
        return int(re.sub(r'\D', '', str(x)) or 0)
    except Exception:
        return 0

def passage(ps, limit=5000):
    work = (ps.get('work') or '').lower()
    b, c = num(ps.get('book_or_canto')), num(ps.get('chapter_or_section'))
    vr = ps.get('verse_range') or ''
    path = None
    if 'bhagavata' in work:
        path = f'{NORM}/bhagavata_sanskrit/canto_{b:02d}/chapter_{c:03d}.txt'
    elif 'vishnu' in work:
        path = f'{NORM}/vishnu_purana/book_{b:02d}/chapter_{c:03d}.txt'
    elif 'harivamsha' in work:
        path = f'{NORM}/harivamsa/part_{b:02d}/chapter_{c:03d}.txt'
    elif 'mahabharata' in work:
        path = f'{NORM}/mahabharata/parva_{b:02d}/section_{c:03d}.txt'
    if not path or not os.path.exists(path):
        return f'[passage unavailable: {ps.get("work")} {b}.{c}]'
    txt = open(path, encoding='utf-8', errors='replace').read()
    if 'bhagavata' in work and vr:
        nums = [num(m) for m in re.findall(r'\d+', vr)]
        if len(nums) >= 2:
            lo, hi = min(nums), max(nums)
            verses = {}
            for line in txt.split('\n'):
                m = re.match(r'^(\d+)\.\s*(.*)$', line.strip())
                if m:
                    verses[int(m.group(1))] = m.group(2)
            picked = [f'{v}. {verses[v]}' for v in range(lo, hi + 1) if v in verses]
            if picked:
                return '\n'.join(picked)
    return txt[:limit] + ('\n[...]' if len(txt) > limit else '')

OUT = os.path.join(BASE, 'data/evidence_full')
os.makedirs(OUT, exist_ok=True)
written = 0
for pid in sorted(stories.keys()):
    s = stories[pid]
    ev = cids[s['canonical_event_id']]
    prev, nxt = chain[pid]
    L = []
    L.append(f'# STORY {pid} — {s["working_title"]}')
    L.append('')
    L.append('## Index entry')
    L.append(f'title: {s["working_title"]}')
    L.append(f'summary: {s["one_line_summary"]}')
    L.append(f'life_stage: {s["life_stage"]} | story_arc: {s["story_arc"]}')
    L.append(f'characters: {", ".join(s["characters"])}')
    L.append(f'locations: {", ".join(s["locations"])}')
    L.append(f'themes: {", ".join(s["themes"])}')
    L.append(f'festival_tags: {", ".join(s["festival_tags"])}')
    L.append(f'age_sensitivity: {s["age_sensitivity"]} | notes: {s.get("notes", "")[:200]}')
    L.append('')
    L.append('## Canonical event')
    L.append(f'event_id: {ev["canonical_event_id"]}')
    L.append(f'variant_notes: {ev.get("variant_notes", "")}')
    L.append('')
    L.append('## Sources and evidence excerpts')
    for src in ev['sources']:
        L.append(f'- {src["work"]} | book/canto {src["book_or_canto"]} | chapter/section {src["chapter_or_section"]} | verses {src["verse_range"]} | confidence {src["source_confidence"]}')
        L.append(f'  excerpt: {src["source_excerpt"][:400]}')
    L.append('')
    L.append('## Primary source passage(s)')
    for src in ev['sources'][:2]:
        L.append(f'### {src["work"]} {src["book_or_canto"]}.{src["chapter_or_section"]} ({src["verse_range"]})')
        L.append(passage(src, 5000))
        L.append('')
    L.append('## Corpus chain')
    L.append(f'previous_story_id: {prev} | next_story_id: {nxt}')
    if prev:
        L.append(f'previous title: {stories[prev]["working_title"]}')
    if nxt:
        L.append(f'next title: {stories[nxt]["working_title"]}')
    if pid in pilot_ids:
        L.append('')
        L.append('## NOTE: this story already exists in the pilot (data/pilot_stories/) — do not rewrite it.')
    open(os.path.join(OUT, f'{pid}.txt'), 'w').write('\n'.join(L))
    written += 1
print(f'wrote {written} evidence packs to data/evidence_full/')
print('pilot ids flagged in packs:', sum(1 for p in pilot_ids if os.path.exists(os.path.join(OUT, f"{p}.txt"))))
