#!/usr/bin/env python3
"""Build per-story evidence packs for the 48 pilot stories.

Each pack (data/pilot_evidence/<DKS>.txt) contains:
  - the index entry
  - the canonical event (all sources + excerpts + variant notes)
  - the primary-source passage(s) from the normalized corpus
  - the pilot-chain neighbours (previous/next story ids)
This is the factual boundary for story writing and fact-checking.
"""
import json, os, re

BASE = os.path.expanduser('~/Documents/projects/indian_apps/dailyX/daily_krishna_stories')
NORM = os.path.join(BASE, 'sources/normalized')
IDX = json.load(open(os.path.join(BASE, 'data/story_index.json')))
CANON = json.load(open(os.path.join(BASE, 'data/canonical_events.json')))
SEL = json.load(open(os.path.join(BASE, 'data/pilot_story_selection.json')))

stories = {s['id']: s for s in IDX['stories']}
cids = {e['canonical_event_id']: e for e in CANON['events']}
pilot_ids = [s['id'] for s in SEL['stories']]
chrono = sorted(pilot_ids, key=lambda i: stories[i]['chronological_order'])
chain = {i: (chrono[idx-1] if idx > 0 else None, chrono[idx+1] if idx+1 < len(chrono) else None)
         for idx, i in enumerate(chrono)}

OUT = os.path.join(BASE, 'data/pilot_evidence')
os.makedirs(OUT, exist_ok=True)

def num(x):
    try:
        return int(re.sub(r'\D', '', str(x)) or 0)
    except Exception:
        return 0

def passage(ps, limit=2600):
    """Return the cited source passage(s) text from the normalized corpus."""
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
        # verse-numbered: extract the range
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

packs = 0
for pid in pilot_ids:
    s = stories[pid]
    ev = cids[s['canonical_event_id']]
    prev, nxt = chain[pid]
    lines = []
    lines.append(f'# STORY {pid} — {s["working_title"]}')
    lines.append('')
    lines.append('## Index entry')
    lines.append(f'title: {s["working_title"]}')
    lines.append(f'summary: {s["one_line_summary"]}')
    lines.append(f'life_stage: {s["life_stage"]} | story_arc: {s["story_arc"]}')
    lines.append(f'characters: {", ".join(s["characters"])}')
    lines.append(f'locations: {", ".join(s["locations"])}')
    lines.append(f'themes: {", ".join(s["themes"])}')
    lines.append(f'festival_tags: {", ".join(s["festival_tags"])}')
    lines.append(f'age_sensitivity: {s["age_sensitivity"]} | notes: {s.get("notes", "")[:200]}')
    lines.append('')
    lines.append('## Canonical event')
    lines.append(f'event_id: {ev["canonical_event_id"]}')
    lines.append(f'variant_notes: {ev.get("variant_notes", "")}')
    lines.append('')
    lines.append('## Sources and evidence excerpts')
    for src in ev['sources']:
        lines.append(f'- {src["work"]} | book/canto {src["book_or_canto"]} | chapter/section {src["chapter_or_section"]} | verses {src["verse_range"]} | confidence {src["source_confidence"]}')
        lines.append(f'  excerpt: {src["source_excerpt"][:400]}')
    lines.append('')
    lines.append('## Primary source passage(s)')
    for src in ev['sources'][:2]:
        lines.append(f'### {src["work"]} {src["book_or_canto"]}.{src["chapter_or_section"]} ({src["verse_range"]})')
        lines.append(passage(src, 2600))
        lines.append('')
    lines.append('## Pilot chain')
    lines.append(f'previous_story_id: {prev} | next_story_id: {nxt}')
    if prev:
        lines.append(f'previous title: {stories[prev]["working_title"]}')
    if nxt:
        lines.append(f'next title: {stories[nxt]["working_title"]}')
    open(os.path.join(OUT, f'{pid}.txt'), 'w').write('\n'.join(lines))
    packs += 1

print(f'wrote {packs} evidence packs to data/pilot_evidence/')
