#!/usr/bin/env python3
"""Build compact per-chunk event listings for the LLM dedup/cluster pass.
Output: data/mining/clusters/input_<chunk>.txt — lines "EVENT_ID | WORK | LOC | TITLE || SUMMARY"
Chunks split by life_stage to keep each LLM pass small (~250 events max).
"""
import os, json, glob

BASE = os.path.expanduser('~/Documents/projects/indian_apps/dailyX/daily_krishna_stories')
RAW = os.path.join(BASE, 'data/mining/raw_events')
OUTDIR = os.path.join(BASE, 'data/mining/clusters')
os.makedirs(OUTDIR, exist_ok=True)

events = []
for f in sorted(glob.glob(os.path.join(RAW, '*.jsonl'))):
    for line in open(f, encoding='utf-8'):
        line = line.strip()
        if not line:
            continue
        try:
            ev = json.loads(line)
        except Exception:
            continue
        ps = ev.get('primary_source', {})
        events.append({
            'id': ev.get('event_id', ''),
            'work': ps.get('work', ''),
            'loc': f"{ps.get('book_or_canto')}.{ps.get('chapter_or_section')}",
            'title': ev.get('title', ''),
            'summary': ev.get('one_line_summary', ''),
            'life_stage': ev.get('life_stage', 'other'),
        })

# chunk by life_stage order
ORDER = ['birth', 'gokul', 'vrindavan', 'mathura', 'dwaraka', 'pandava_period', 'kurukshetra', 'later_life', 'other']
chunks = {}
for ev in events:
    chunks.setdefault(ev['life_stage'], []).append(ev)

# merge small chunks to keep ~250 per pass
merged = []
cur = []
for st in ORDER:
    cur.extend(chunks.get(st, []))
    if len(cur) >= 200:
        merged.append(cur)
        cur = []
if cur:
    merged.append(cur)

for i, chunk in enumerate(merged, 1):
    lines = []
    for ev in chunk:
        lines.append(f"{ev['id']} | {ev['work']} | {ev['loc']} | {ev['title']} || {ev['summary']}")
    open(os.path.join(OUTDIR, f'input_{i:02d}.txt'), 'w').write('\n'.join(lines))
    print(f'input_{i:02d}.txt: {len(chunk)} events')

print('total events:', len(events))
