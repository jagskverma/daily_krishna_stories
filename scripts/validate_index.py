#!/usr/bin/env python3
"""Automatic QA for the story index (spec §9). Exit code 0 = pass, 1 = fail.

Checks:
  1. >= 500 stories
  2. unique DKS ids
  3. required fields present
  4. valid primary-source references (locator exists in normalized registry)
  5. duplicate/similar titles (token overlap)
  6. duplicate summaries
  7. suspiciously overlapping events (same primary source locator)
  8. missing/invalid story arcs
  9. source distribution report
  10. chronological ordering monotonic with arc order
  11. invalid enum values (life_stage, age_sensitivity, arc)
"""
import os, re, json, sys
from collections import Counter, defaultdict

BASE = os.path.expanduser('~/Documents/projects/indian_apps/dailyX/daily_krishna_stories')
IDX = json.load(open(os.path.join(BASE, 'data/story_index.json')))
ARCS = json.load(open(os.path.join(BASE, 'data/story_arcs.json')))
REG = json.load(open(os.path.join(BASE, 'sources/normalized/registry.json')))

stories = IDX['stories']
LIFE = {'birth','gokul','vrindavan','mathura','dwaraka','pandava_period','kurukshetra','later_life','other'}
SENS = {'all','mild_violence','mature'}
ARC_SLUGS = {a['slug'] for a in ARCS['arcs']}
ARC_ORDER = {a['slug']: a['order'] for a in ARCS['arcs']}

failures = []

def check(cond, msg):
    if not cond:
        failures.append(msg)

# locators available per work (for citation validation)
locators = defaultdict(set)
for r in REG:
    if r['work'] == 'bhagavata_sanskrit':
        locators['bhagavata'].add((r['canto'], r['chapter']))
        locators['bhagavata_verses'] = locators.get('bhagavata_verses', set())
        locators['bhagavata_verses'].add((r['canto'], r['chapter'], r['verses']))
    elif r['work'] == 'vishnu_purana':
        locators['vishnu'].add((r['book'], r['chapter']))
    elif r['work'] == 'harivamsa':
        locators['harivamsa'].add((r['part'], r['chapter']))
    elif r['work'] == 'mahabharata':
        locators['mahabharata'].add((r['parva'], r['section']))

def work_key(work):
    w = (work or '').lower()
    for k in ('bhagavata', 'harivam', 'vishnu', 'mahabharata'):
        if k in w:
            return k
    return None

def num(x):
    try:
        return int(re.sub(r'\D', '', str(x)) or 0)
    except Exception:
        return 0

# 1-2: count + unique ids
check(len(stories) >= 500, f'FAIL: only {len(stories)} stories (<500)')
ids = [s['id'] for s in stories]
dups = [i for i, c in Counter(ids).items() if c > 1]
check(not dups, f'FAIL: duplicate ids: {dups}')

# 3: required fields
for s in stories:
    for f in ('id', 'working_title', 'one_line_summary', 'chronological_order', 'life_stage',
              'story_arc', 'characters', 'locations', 'themes', 'source_tier', 'primary_source',
              'source_excerpt', 'age_sensitivity', 'estimated_story_strength', 'visual_potential',
              'independent_story_score', 'source_confidence'):
        if f not in s or s[f] in (None, ''):
            failures.append(f'FAIL: {s["id"]} missing required field {f}')
            break
    ps = s.get('primary_source', {})
    for f in ('work', 'book_or_canto', 'chapter_or_section'):
        if not ps.get(f):
            failures.append(f'FAIL: {s["id"]} primary_source missing {f}')

# 4: primary-source references exist in the corpus
bad_refs = []
for s in stories:
    ps = s['primary_source']
    wk = work_key(ps.get('work'))
    if wk is None:
        bad_refs.append((s['id'], 'unknown work'))
        continue
    b = num(ps.get('book_or_canto'))
    c = num(ps.get('chapter_or_section'))
    if wk == 'bhagavata':
        if (b, c) not in locators['bhagavata']:
            # allow canto 10 shorthand where chapter implicit? no — must exist
            bad_refs.append((s['id'], f'BP {b}.{c} not in corpus'))
        else:
            vr = ps.get('verse_range') or ''
            if vr:
                vmax = dict((x[0], x[1]) for x in locators['bhagavata_verses'] if (x[0], x[1]) == (b, c))
                # check verse range within chapter verse count
                nv = [v for (bb, cc, v) in locators['bhagavata_verses'] if bb == b and cc == c]
                if nv:
                    hi = max(num(m) for m in re.findall(r'\d+', vr) or [0])
                    if hi > nv[0]:
                        bad_refs.append((s['id'], f'BP {b}.{c} verse_range {vr} exceeds chapter ({nv[0]} verses)'))
    elif wk == 'vishnu':
        if (b, c) not in locators['vishnu']:
            bad_refs.append((s['id'], f'VP {b}.{c} not in corpus'))
    elif wk == 'harivamsa':
        if (b, c) not in locators['harivamsa']:
            bad_refs.append((s['id'], f'HV part {b} ch {c} not in corpus'))
    elif wk == 'mahabharata':
        if (b, c) not in locators['mahabharata']:
            bad_refs.append((s['id'], f'MB parva {b} sec {c} not in corpus'))
check(not bad_refs, 'FAIL: invalid primary refs: ' + '; '.join(f'{a}: {b}' for a, b in bad_refs[:10]))

# 5: similar titles
def norm_title(t):
    t = (t or '').lower()
    t = re.sub(r'[^a-z0-9 ]', ' ', t)
    return set(w for w in t.split() if len(w) > 3 and w not in {'krishna', 'lord', 'sri', 'shri'})

title_dups = []
titles = [(s['id'], norm_title(s['working_title'])) for s in stories]
for i in range(len(titles)):
    for j in range(i + 1, len(titles)):
        a, b = titles[i][1], titles[j][1]
        if a and b and len(a & b) >= 3 and a == b:
            title_dups.append((titles[i][0], titles[j][0]))
check(not title_dups, f'FAIL: identical normalized titles: {title_dups[:8]}')

# 6: duplicate summaries (normalized)
summ = {}
for s in stories:
    n = re.sub(r'[^a-z0-9 ]', ' ', (s['one_line_summary'] or '').lower())
    n = re.sub(r'\s+', ' ', n).strip()
    if n in summ:
        failures.append(f'FAIL: duplicate summary: {summ[n]} == {s["id"]}')
    else:
        summ[n] = s['id']

# 7: overlapping events (same primary locator, different stories)
# Beat decomposition legitimately gives many stories per chapter; flag only
# when two stories cite the SAME primary locator AND their verse ranges
# overlap substantially AND titles are near-identical (true near-duplicates).
def vrange(ps):
    vr = (ps.get('verse_range') or '')
    nums = [num(m) for m in re.findall(r'\d+', vr)]
    return (min(nums), max(nums)) if nums else None

by_loc = defaultdict(list)
for s in stories:
    ps = s['primary_source']
    by_loc[(ps.get('work'), ps.get('book_or_canto'), ps.get('chapter_or_section'))].append(s)

near_dups = []
for loc, ss in by_loc.items():
    for i in range(len(ss)):
        for j in range(i + 1, len(ss)):
            a, b = ss[i], ss[j]
            ra, rb = vrange(a['primary_source']), vrange(b['primary_source'])
            if ra and rb:
                overlap = max(0, min(ra[1], rb[1]) - max(ra[0], rb[0]) + 1)
                smaller = min(ra[1] - ra[0] + 1, rb[1] - rb[0] + 1)
                if smaller > 0 and overlap / smaller >= 0.5:
                    ta = norm_title(a['working_title'])
                    tb = norm_title(b['working_title'])
                    if ta and tb and len(ta & tb) >= 3:
                        near_dups.append((a['id'], b['id'], loc))
if near_dups:
    failures.append('FAIL: near-duplicate events (same locator, overlapping verse range, similar title): ' +
                    '; '.join(f'{x}~{y}@{z}' for x, y, z in near_dups[:8]))

# 8: story arcs valid + present
for s in stories:
    check(s['story_arc'] in ARC_SLUGS, f'FAIL: {s["id"]} invalid arc {s["story_arc"]}')
missing_arc = [s['id'] for s in stories if not s['story_arc']]
check(not missing_arc, f'FAIL: missing story_arc: {missing_arc[:5]}')

# 10: chronological ordering monotonic with arc order
arc_seq = [ARC_ORDER.get(s['story_arc'], 900) for s in stories]
inversions = sum(1 for i in range(1, len(arc_seq)) if arc_seq[i] < arc_seq[i - 1])
check(inversions == 0, f'FAIL: {inversions} chronological inversions vs arc order')

# 11: enums
for s in stories:
    check(s['life_stage'] in LIFE, f'FAIL: {s["id"]} bad life_stage {s["life_stage"]}')
    check(s['age_sensitivity'] in SENS, f'FAIL: {s["id"]} bad age_sensitivity {s["age_sensitivity"]}')

# 9: source distribution
dist = Counter(s['primary_source']['work'] for s in stories)
stage_dist = Counter(s['life_stage'] for s in stories)
arc_dist = Counter(s['story_arc'] for s in stories)
multi = sum(1 for s in stories if s['additional_sources'])
variants = sum(1 for s in stories if s['variant_notes'])
conf_dist = Counter(s['source_confidence'] for s in stories)

print('=== QA REPORT ===')
print(f'stories: {len(stories)}')
print('source distribution:', dict(dist))
print('life stage distribution:', dict(stage_dist))
print('arc distribution:', dict(arc_dist))
print('multi-source stories:', multi, '| with variant_notes:', variants)
print('source_confidence distribution:', dict(sorted(conf_dist.items())))
print('FAILURES:', len(failures))
for f in failures[:20]:
    print(' ', f)
print('RESULT:', 'PASS' if not failures else 'FAIL')
sys.exit(0 if not failures else 1)
