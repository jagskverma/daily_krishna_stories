#!/usr/bin/env python3
"""Consolidate fact-check agent outputs (data/mining/factcheck/*.jsonl)
into data/pilot_fact_checks.json, and apply required corrections to the
story files (only UNSUPPORTED / CONTRADICTED claims).

Usage:
  python3 scripts/consolidate_factchecks.py          # consolidate + report
  python3 scripts/consolidate_factchecks.py --apply  # apply corrections
"""
import json, os, glob, sys, re

BASE = os.path.expanduser('~/Documents/projects/indian_apps/dailyX/daily_krishna_stories')
FC_DIR = os.path.join(BASE, 'data/mining/factcheck')
OUT = os.path.join(BASE, 'data/pilot_fact_checks.json')
STORIES = os.path.join(BASE, 'data/pilot_stories')

records = {}
for f in sorted(glob.glob(os.path.join(FC_DIR, '*.jsonl'))):
    for line in open(f, encoding='utf-8'):
        line = line.strip()
        if not line:
            continue
        r = json.loads(line)
        sid = r.get('story_id')
        if sid not in records:
            records[sid] = {'statements': [], 'corrections': [], 'source_fidelity_score': r.get('source_fidelity_score', 3), 'notes': r.get('notes', '')}
        records[sid]['statements'] += r.get('statements', [])
        records[sid]['corrections'] += r.get('corrections', [])

# fidelity: any UNSUPPORTED/CONTRADICTED caps at 3; REASONABLE_CONNECTIVE_NARRATION fine
for sid, rec in records.items():
    bad = [st for st in rec['statements'] if st.get('verdict') in ('UNSUPPORTED', 'CONTRADICTED')]
    if bad:
        rec['source_fidelity_score'] = min(rec['source_fidelity_score'], 3)
    rec['issues'] = [{'claim': st.get('claim'), 'verdict': st.get('verdict')} for st in rec['statements'] if st.get('verdict') in ('UNSUPPORTED', 'CONTRADICTED')]

json.dump(records, open(OUT, 'w'), indent=1, ensure_ascii=False)
print(f'fact checks consolidated: {len(records)} stories')
for sid, rec in sorted(records.items()):
    print(f'  {sid}: score {rec["source_fidelity_score"]}/5, issues {len(rec["issues"])}, statements {len(rec["statements"])}')

if '--apply' in sys.argv:
    applied = 0
    for sid, rec in records.items():
        if not rec['issues']:
            continue
        p = os.path.join(STORIES, f'{sid}.json')
        if not os.path.exists(p):
            print(f'  !! story file missing: {sid}')
            continue
        s = json.load(open(p))
        story = s.get('story', '')
        for corr in rec['corrections']:
            old = corr.get('original_sentence') or corr.get('claim')
            new = corr.get('suggested')
            if old and new and old in story:
                story = story.replace(old, new, 1)
                applied += 1
            elif old:
                # try fuzzy: first 60 chars match
                probe = old[:60]
                idx = story.find(probe)
                if idx >= 0:
                    story = story[:idx] + new + story[idx + len(old):]
                    applied += 1
                else:
                    print(f'  !! could not apply correction in {sid}: {old[:70]}')
        if story != s.get('story'):
            s['story'] = story
            json.dump(s, open(p, 'w'), indent=1, ensure_ascii=False)
            print(f'  applied corrections to {sid}')
    print(f'total correction replacements: {applied}')
