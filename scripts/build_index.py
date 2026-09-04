#!/usr/bin/env python3
"""Build data/story_index.json + data/story_index.csv + data/story_arcs.json linkage
from data/canonical_events.json.

- Assigns DKS_#### ids (stable, sorted by chronological order).
- chronological_order = sequential rank after sorting by (arc order, internal position).
- Internal position: primary source position (book/canto/chapter/section) for
  events within an arc; multi-source events use their best (highest-priority) source.
- Every story maps to an arc.
"""
import os, re, json, csv

BASE = os.path.expanduser('~/Documents/projects/indian_apps/dailyX/daily_krishna_stories')
CANON = json.load(open(os.path.join(BASE, 'data/canonical_events.json')))
ARCS = json.load(open(os.path.join(BASE, 'data/story_arcs.json')))
REG = json.load(open(os.path.join(BASE, 'sources/normalized/registry.json')))

arc_order = {a['slug']: a['order'] for a in ARCS['arcs']}
arc_name = {a['slug']: a['name'] for a in ARCS['arcs']}

# source priority for position & excerpt
SRC_PRIO = {'srimad bhagavata': 0, 'harivamsha': 1, 'vishnu purana': 2, 'mahabharata': 3}

def src_rank(work):
    w = (work or '').lower()
    for k, p in SRC_PRIO.items():
        if k in w:
            return p
    return 9

def num(x):
    try:
        return int(re.sub(r'\D', '', str(x)) or 0)
    except Exception:
        return 0

def primary_ref(ev):
    """Best source for ordering: highest-priority source with a numeric locator."""
    best = None
    for s in ev['sources']:
        loc = num(s.get('chapter_or_section'))
        rank = src_rank(s.get('work'))
        key = (rank, -loc if loc else 0)
        if best is None or key < best[0]:
            best = (key, s)
    return best[1]

def sort_key(ev):
    arc = ev.get('story_arc', 'other')
    ref = primary_ref(ev)
    return (arc_order.get(arc, 900), num(ref.get('book_or_canto')), num(ref.get('chapter_or_section')),
            num(ref.get('verse_range', '')), ev.get('canonical_event_id', ''))

events = sorted(CANON['events'], key=sort_key)

index = []
for i, ev in enumerate(events, 1):
    ref = primary_ref(ev)
    ps = ev['sources'][0]
    arc = ev.get('story_arc', 'other')
    idx = {
        'id': f'DKS_{i:04d}',
        'canonical_event_id': ev.get('canonical_event_id'),
        'working_title': ev.get('working_title') or ev.get('title'),
        'one_line_summary': ev.get('one_line_summary', ''),
        'chronological_order': i,
        'life_stage': ev.get('life_stage', 'other'),
        'story_arc': arc,
        'story_arc_name': arc_name.get(arc, arc),
        'characters': ev.get('characters', []),
        'locations': ev.get('locations', []),
        'themes': ev.get('themes', []),
        'source_tier': 'A',
        'primary_source': {
            'work': ps.get('work', ''),
            'book_or_canto': ps.get('book_or_canto', ''),
            'chapter_or_section': ps.get('chapter_or_section', ''),
            'verse_range': ps.get('verse_range', ''),
        },
        'additional_sources': [
            {'work': s.get('work', ''), 'book_or_canto': s.get('book_or_canto', ''),
             'chapter_or_section': s.get('chapter_or_section', ''), 'verse_range': s.get('verse_range', '')}
            for s in ev['sources'][1:]],
        'source_excerpt': ps.get('source_excerpt', ''),
        'variant_notes': ev.get('variant_notes', ''),
        'festival_tags': ev.get('festival_tags', []),
        'age_sensitivity': ev.get('age_sensitivity', 'all'),
        'estimated_story_strength': ev.get('estimated_story_strength', 3),
        'visual_potential': ev.get('visual_potential', 3),
        'independent_story_score': ev.get('independent_story_score', 3),
        'source_confidence': ev.get('source_confidence', 3),
        'notes': ev.get('notes', ''),
    }
    index.append(idx)

out = os.path.join(BASE, 'data/story_index.json')
json.dump({'schema_version': '1.0', 'story_count': len(index), 'stories': index},
          open(out, 'w'), indent=1, ensure_ascii=False)

csv_path = os.path.join(BASE, 'data/story_index.csv')
cols = ['id', 'chronological_order', 'working_title', 'one_line_summary', 'life_stage', 'story_arc',
        'characters', 'locations', 'themes', 'source_tier', 'primary_work', 'primary_book',
        'primary_chapter', 'verse_range', 'festival_tags', 'age_sensitivity',
        'estimated_story_strength', 'visual_potential', 'independent_story_score',
        'source_confidence', 'variant_notes']
with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(cols)
    for s in index:
        w.writerow([
            s['id'], s['chronological_order'], s['working_title'], s['one_line_summary'],
            s['life_stage'], s['story_arc'], '; '.join(s['characters']), '; '.join(s['locations']),
            '; '.join(s['themes']), s['source_tier'], s['primary_source']['work'],
            s['primary_source']['book_or_canto'], s['primary_source']['chapter_or_section'],
            s['primary_source']['verse_range'], '; '.join(s['festival_tags']), s['age_sensitivity'],
            s['estimated_story_strength'], s['visual_potential'], s['independent_story_score'],
            s['source_confidence'], s['variant_notes']])
print(f'story_index.json: {len(index)} stories')
print(f'story_index.csv: {csv_path}')
