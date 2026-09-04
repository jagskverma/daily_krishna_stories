#!/usr/bin/env python3
"""Assemble the 48 pilot story JSONs into data/pilot_stories.json.
Validates the §20 schema, word counts, injects variant_notes from the canonical DB.
"""
import json, os, glob, re, sys

BASE = os.path.expanduser('~/Documents/projects/indian_apps/dailyX/daily_krishna_stories')
DIR = os.path.join(BASE, 'data/pilot_stories')
OUT = os.path.join(BASE, 'data/pilot_stories.json')
CANON = json.load(open(os.path.join(BASE, 'data/canonical_events.json')))
cids = {e['canonical_event_id']: e for e in CANON['events']}

REQ = ['id', 'title', 'story', 'reflection', 'life_stage', 'story_arc', 'characters', 'locations',
       'themes', 'previous_story_id', 'next_story_id', 'hero_scene', 'visual_elements',
       'sources', 'generation_metadata', 'editorial_status']

stories, errors = [], []
for f in sorted(glob.glob(os.path.join(DIR, '*.json'))):
    try:
        s = json.load(open(f))
    except Exception as e:
        errors.append(f'{os.path.basename(f)}: parse error {e}')
        continue
    sid = s.get('id')
    missing = [k for k in REQ if k not in s]
    if missing:
        errors.append(f'{sid}: missing fields {missing}')
    wc = len(re.findall(r"\S+", s.get('story', '')))
    if not (400 <= wc <= 1200):
        errors.append(f'{sid}: word count {wc} outside 400-1200')
    if not s.get('editorial_status'):
        s['editorial_status'] = 'unreviewed'
    # inject variant notes from the evidence pack (authoritative at writing time)
    pack = os.path.join(BASE, 'data/pilot_evidence', f'{sid}.txt')
    if os.path.exists(pack):
        for line in open(pack, encoding='utf-8'):
            if line.startswith('variant_notes:'):
                vn = line.split(':', 1)[1].strip()
                if vn and vn.lower() != 'none':
                    s['variant_notes'] = vn
                break
    s['_word_count'] = wc
    stories.append(s)

stories.sort(key=lambda x: x['id'])
json.dump({'schema_version': '2.0', 'story_count': len(stories), 'stories': stories},
          open(OUT, 'w'), indent=1, ensure_ascii=False)
print(f'assembled {len(stories)} stories -> {OUT}')
for e in errors:
    print('ERROR:', e)
sys.exit(1 if errors else 0)
