#!/usr/bin/env python3
"""Merge raw mined events into a canonical event database.

Pipeline:
1. Load all raw_events/*.jsonl, validate + normalize each record.
2. LLM clustering pass (external) produces cluster files: data/mining/clusters/*.json
   [{cluster: [event_ids], canonical_title, variant_notes, notes}]
3. This script applies the clusters: one canonical event per cluster, all source
   records attached, scores merged, variant_notes preserved.

Output:
  data/canonical_events.json  — the deduplicated Krishna event database
"""
import os, re, json, sys, glob

BASE = os.path.expanduser('~/Documents/projects/indian_apps/dailyX/daily_krishna_stories')
RAW = os.path.join(BASE, 'data/mining/raw_events')
OUT = os.path.join(BASE, 'data/canonical_events.json')

LIFE_STAGES = {'birth', 'gokul', 'vrindavan', 'mathura', 'dwaraka',
               'pandava_period', 'kurukshetra', 'later_life', 'other'}
SENS = {'all', 'mild_violence', 'mature'}
ARCS = {'prophecy_of_kamsa','birth_of_krishna','krishna_reaches_gokul','early_gokul_childhood',
        'vrindavan_childhood','kaliya_and_yamuna','govardhan_and_indra','rasa_and_gopis',
        'akrura_and_departure','mathura_and_kamsa','jarasandha_and_kings','dwaraka_founded',
        'rukmini_and_marriages','syamantaka_jewel','narakasura_and_gods','pandava_friendship',
        'rajasuya_and_sisupala','draupadi_honour','peace_mission','kurukshetra_war',
        'post_war_krishna','uddhava_and_teachings','end_of_yadavas','krishna_departure','other'}

def load_raw():
    events = {}
    problems = []
    for f in sorted(glob.glob(os.path.join(RAW, '*.jsonl'))):
        n = 0
        for line in open(f, encoding='utf-8'):
            line = line.strip()
            if not line:
                continue
            n += 1
            try:
                ev = json.loads(line)
            except Exception as e:
                problems.append({'file': os.path.basename(f), 'line': n, 'error': str(e)})
                continue
            # normalize work-name variants
            ps = ev.get('primary_source') or {}
            w = (ps.get('work') or '')
            if 'Kisari Mohan Ganguli' in w:
                ps['work'] = 'Mahabharata (Ganguli translation)'
            events[ev.get('event_id', f'{os.path.basename(f)}:{n}')] = ev
        print(f'  {os.path.basename(f)}: {n} records')
    return events, problems

def validate(events):
    issues = []
    for eid, ev in events.items():
        if ev.get('life_stage') not in LIFE_STAGES:
            issues.append({'event_id': eid, 'issue': f"life_stage '{ev.get('life_stage')}'"})
        if ev.get('age_sensitivity') not in SENS:
            issues.append({'event_id': eid, 'issue': f"age_sensitivity '{ev.get('age_sensitivity')}'"})
        if ev.get('story_arc') not in ARCS:
            issues.append({'event_id': eid, 'issue': f"story_arc '{ev.get('story_arc')}'"})
        ps = ev.get('primary_source', {})
        for k in ('work', 'book_or_canto', 'chapter_or_section'):
            if not ps.get(k):
                issues.append({'event_id': eid, 'issue': f'primary_source missing {k}'})
        for field in ('title', 'one_line_summary', 'source_excerpt'):
            if not ev.get(field):
                issues.append({'event_id': eid, 'issue': f'missing {field}'})
        for field in ('estimated_story_strength', 'visual_potential', 'independent_story_score', 'source_confidence'):
            v = ev.get(field)
            if not isinstance(v, int) or not (1 <= v <= 5):
                issues.append({'event_id': eid, 'issue': f'{field} = {v!r} (not 1-5 int)'})
    return issues

def score_merge(vals, mode='max'):
    vals = [v for v in vals if isinstance(v, int)]
    return max(vals) if vals else 1

def apply_clusters(events, cluster_files):
    clusters = []
    for f in cluster_files:
        for line in open(f, encoding='utf-8'):
            line = line.strip()
            if not line:
                continue
            try:
                clusters.append(json.loads(line))
            except Exception:
                pass
    # build event -> cluster map
    used = set()
    canonical = []
    for cl in clusters:
        members = [e for e in cl.get('cluster', []) if e in events and e not in used]
        if not members:
            continue
        used.update(members)
        recs = [events[e] for e in members]
        # primary record: prefer Bhagavata, then Harivamsha, then Vishnu Purana, then Mahabharata
        prio = {'srimad bhagavata': 0, 'harivamsha': 1, 'vishnu purana': 2, 'mahabharata': 3}
        def rank(r):
            w = (r.get('primary_source', {}).get('work', '') or '').lower()
            for k, p in prio.items():
                if k in w:
                    return p
            return 9
        recs.sort(key=rank)
        primary = recs[0]
        sources = []
        for r in recs:
            ps = r.get('primary_source', {})
            sources.append({
                'work': ps.get('work', ''),
                'book_or_canto': ps.get('book_or_canto', ''),
                'chapter_or_section': ps.get('chapter_or_section', ''),
                'verse_range': ps.get('verse_range', ''),
                'source_excerpt': r.get('source_excerpt', ''),
                'source_confidence': r.get('source_confidence', 1),
                'event_id': r.get('event_id'),
            })
        # variant handling: if cluster notes say variants differ materially, mark
        variant_notes = cl.get('variant_notes') or ''
        if not variant_notes:
            # if any member's variant_notes non-empty, surface it
            vnotes = [r.get('variant_notes') for r in recs if r.get('variant_notes')]
            if vnotes:
                variant_notes = ' | '.join(vnotes)
        canonical.append({
            'canonical_event_id': cl.get('canonical_event_id') or f"evt_{len(canonical)+1:04d}",
            'working_title': cl.get('canonical_title') or primary.get('title'),
            'one_line_summary': primary.get('one_line_summary'),
            'life_stage': primary.get('life_stage'),
            'story_arc': primary.get('story_arc'),
            'characters': primary.get('characters', []),
            'locations': primary.get('locations', []),
            'themes': primary.get('themes', []),
            'festival_tags': primary.get('festival_tags', []),
            'age_sensitivity': primary.get('age_sensitivity', 'all'),
            'estimated_story_strength': score_merge([r.get('estimated_story_strength') for r in recs]),
            'visual_potential': score_merge([r.get('visual_potential') for r in recs]),
            'independent_story_score': score_merge([r.get('independent_story_score') for r in recs]),
            'source_confidence': score_merge([r.get('source_confidence') for r in recs]),
            'sources': sources,
            'variant_notes': variant_notes,
            'notes': cl.get('notes') or '',
            'member_event_ids': members,
        })
    # events not in any cluster
    for eid, ev in events.items():
        if eid in used:
            continue
        ps = ev.get('primary_source', {})
        canonical.append({
            'canonical_event_id': f"evt_{len(canonical)+1:04d}",
            'working_title': ev.get('title'),
            'one_line_summary': ev.get('one_line_summary'),
            'life_stage': ev.get('life_stage'),
            'story_arc': ev.get('story_arc'),
            'characters': ev.get('characters', []),
            'locations': ev.get('locations', []),
            'themes': ev.get('themes', []),
            'festival_tags': ev.get('festival_tags', []),
            'age_sensitivity': ev.get('age_sensitivity', 'all'),
            'estimated_story_strength': ev.get('estimated_story_strength', 3),
            'visual_potential': ev.get('visual_potential', 3),
            'independent_story_score': ev.get('independent_story_score', 3),
            'source_confidence': ev.get('source_confidence', 3),
            'sources': [{
                'work': ps.get('work', ''), 'book_or_canto': ps.get('book_or_canto', ''),
                'chapter_or_section': ps.get('chapter_or_section', ''), 'verse_range': ps.get('verse_range', ''),
                'source_excerpt': ev.get('source_excerpt', ''), 'source_confidence': ev.get('source_confidence', 1),
                'event_id': eid}],
            'variant_notes': ev.get('variant_notes', ''),
            'notes': ev.get('notes', ''),
            'member_event_ids': [eid],
        })
    return canonical

if __name__ == '__main__':
    events, problems = load_raw()
    print('total raw events:', len(events), '| load problems:', len(problems))
    issues = validate(events)
    print('validation issues:', len(issues))
    for iss in issues[:15]:
        print('  ', iss)
    cluster_files = sorted(glob.glob(os.path.join(BASE, 'data/mining/clusters', '*.jsonl')))
    if not cluster_files:
        print('NO CLUSTER FILES — writing unmerged events as canonical (each event its own entry)')
        # still build canonical DB so downstream can run
        canonical = apply_clusters(events, [])
        json.dump({'schema': 'canonical_events', 'count': len(canonical), 'events': canonical},
                  open(OUT, 'w'), indent=1, ensure_ascii=False)
        print('wrote', OUT, len(canonical), 'events')
        sys.exit(0)
    canonical = apply_clusters(events, cluster_files)

    # ---- arc overrides (curatorial): pattern rules applied to member titles/summaries
    arc_rules = json.load(open(os.path.join(BASE, 'data/mining/arc_overrides.json')))
    remapped = 0
    for ev in canonical:
        hay = ' '.join([ev.get('working_title') or '', ev.get('one_line_summary') or '']).lower()
        for rule in arc_rules:
            if any(p in hay for p in rule['patterns']):
                if ev.get('story_arc') != rule['arc']:
                    ev['story_arc'] = rule['arc']
                    note = ev.get('notes') or ''
                    if 'arc-remap' not in note:
                        ev['notes'] = (note + ' | [arc-remap by curator rule]').strip()
                        remapped += 1
                break
    print('arc overrides applied:', remapped)

    json.dump({'schema': 'canonical_events', 'count': len(canonical), 'raw_count': len(events), 'events': canonical},
              open(OUT, 'w'), indent=1, ensure_ascii=False)
    print('wrote', OUT, len(canonical), 'canonical events (multi-source:',
          sum(1 for e in canonical if len(e['sources']) > 1), ')')
