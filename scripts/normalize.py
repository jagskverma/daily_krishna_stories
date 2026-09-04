#!/usr/bin/env python3
"""Normalize Tier A raw sources into structured UTF-8 text.

Output layout (sources/normalized/):
  mahabharata/parva_{NN}/section_{SSS}.txt
  vishnu_purana/book_{NN}/chapter_{NNN}.txt
  harivamsa/part_{NN}/chapter_{NNN}.txt
  bhagavata_sanskrit/canto_{NN}/chapter_{NNN}.txt
  registry.json   — full structural index
"""
import os, re, json, zipfile, html as htmlmod

BASE = os.path.expanduser('~/Documents/projects/indian_apps/dailyX/daily_krishna_stories')
RAW = os.path.join(BASE, 'sources/raw')
OUT = os.path.join(BASE, 'sources/normalized')

def r2i(s):
    vals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    tot, prev = 0, 0
    for ch in reversed(s.strip()):
        v = vals[ch]
        tot += -v if v < prev else v
        prev = v
    return tot

def clean_ws(s):
    return re.sub(r'[ \t\r]+', ' ', s).strip()

def clean_paras(s):
    """Split text into paragraphs (blank-line separated), clean each, rejoin with newlines."""
    paras = []
    for p in re.split(r'\n\s*\n', s):
        p = clean_ws(p)
        if p:
            paras.append(p)
    return '\n\n'.join(paras)

def strip_gutenberg_header(txt):
    m = re.search(r'\*\*\* START OF (THE|THIS) PROJECT GUTENBERG', txt)
    if m: txt = txt[m.end():]
    m2 = re.search(r'\*\*\* END OF (THE|THIS) PROJECT GUTENBERG', txt)
    if m2: txt = txt[:m2.start()]
    return txt

# ---------------------------------------------------------------- Mahabharata
MB_FILES = [
    ('pg15474.txt', 1), ('pg15475.txt', 1), ('pg15476.txt', 1), ('pg15477.txt', 1),
    ('kmg_book08.txt', 2), ('kmg_book09.txt', 2), ('kmg_book10.txt', 2),
    ('kmg_book11.txt', 2), ('kmg_book16.txt', 2), ('kmg_book17.txt', 2), ('kmg_book18.txt', 2),
]
PARVA_NAMES = {1:'adi',2:'sabha',3:'vana',4:'virata',5:'udyoga',6:'bhishma',7:'drona',
               8:'karna',9:'salya',10:'sauptika',11:'stri',12:'santi',13:'anusasana',
               14:'asvamedha',15:'asramavasika',16:'mausala',17:'mahaprasthanika',18:'svargarohana'}

def norm_mahabharata():
    results = {}
    for fname, group in MB_FILES:
        p = os.path.join(RAW, 'mahabharata', fname)
        txt = strip_gutenberg_header(open(p, encoding='utf-8', errors='replace').read())
        if group == 1:
            parva_heads = [(m.start(), m.group(1).strip()) for m in re.finditer(r'^([A-Z][A-Z ]+?PARVA)[ \r]*$', txt, re.M)]
            heads = []
            for pos, name in parva_heads:
                if name.startswith('END OF'):
                    heads.append((pos, 'END', name.replace('END OF', '').strip()))
                elif not name.startswith('MAHABHARATA'):
                    heads.append((pos, 'START', name.strip()))
            spans = {}
            for i, (pos, kind, name) in enumerate(heads):
                if kind == 'START':
                    # body span: from the LAST START of this parva (body heading,
                    # skipping title-page duplicates) to the first END after it
                    last_start = pos
                    for j in range(i + 1, len(heads)):
                        if heads[j][2] == name and heads[j][1] == 'START':
                            last_start = heads[j][0]
                    endpos = None
                    for j in range(len(heads)):
                        if heads[j][2] == name and heads[j][1] == 'END' and heads[j][0] > last_start:
                            endpos = heads[j][0]
                            break
                    if endpos is None:
                        # no END marker: span to next parva's body start
                        for j in range(len(heads)):
                            if heads[j][1] == 'START' and heads[j][2] != name and heads[j][0] > last_start:
                                endpos = heads[j][0]
                                break
                    spans[(name, last_start)] = endpos
            for (name, last_start), endpos in spans.items():
                canon = re.sub(r'\s+', '', name).lower().replace('parva', '')
                canon = {'aswamedha': 'asvamedha'}.get(canon, canon)
                bn = {v: k for k, v in PARVA_NAMES.items()}[canon]
                seg = txt[last_start:endpos] if endpos else txt[last_start:]
                sections = re.split(r'^SECTION\s+([IVXLCDM]+)\.?\s*$', seg, flags=re.M)
                it = iter(sections)
                next(it)
                for num, body in zip(it, it):
                    sn = r2i(num.strip())
                    results.setdefault(bn, {})[sn] = clean_paras(body)
        else:
            pm = re.search(r'BOOK\s*\d+\s*\n\s*([A-Za-z-]+)', txt)
            canon = pm.group(1).strip().lower().replace('-', '') if pm else None
            canon = canon.replace('parva', '') if canon else canon
            canon = {'stree': 'stri', 'shalya': 'salya', 'svargarohanika': 'svargarohana'}.get(canon, canon)
            bn = {v: k for k, v in PARVA_NAMES.items()}[canon]
            parts = re.split(r'^\s*(\d{1,3})\s*$', txt, flags=re.M)
            it = iter(parts)
            next(it)
            for num, body in zip(it, it):
                results.setdefault(bn, {})[int(num)] = clean_paras(body)
    return results

# ---------------------------------------------------------------- Vishnu Purana
def norm_vishnu_purana():
    zp = zipfile.ZipFile(os.path.join(RAW, 'vishnu_purana', 'wilson_vishnupurana_1840.epub'))
    ncx = zp.read('toc.ncx').decode('utf-8', 'replace')
    navs = re.findall(r'<navPoint[^>]*>.*?<text>(.*?)</text>.*?<content[^>]*src="([^"]+)"', ncx, re.S)
    results = {}
    current_book = None
    for label, src in navs:
        label = htmlmod.unescape(clean_ws(label))
        bm = re.search(r'Book\s*(\d+)', label, re.I)
        cm = re.search(r'^(\d+)\.\s*Chapter', label, re.I) or re.search(r'Chapter\s*(\d+)', label, re.I)
        if bm:
            current_book = int(bm.group(1))
            continue
        if not (cm and current_book):
            continue
        book, chap = current_book, int(cm.group(1))
        if not src.startswith('OEBPS/'):
            src = 'OEBPS/' + src
        try:
            content = zp.read(src).decode('utf-8', 'replace')
        except KeyError:
            alt = src.replace('OEBPS/', '', 1)
            if alt in zp.namelist():
                content = zp.read(alt).decode('utf-8', 'replace')
            else:
                continue
        # confirm from content: <title>...Book N</title> and h2 "N. Chapter"
        tm = re.search(r'<title>([^<]*?)Book\s*(\d+)', content, re.I)
        h2 = re.search(r'<h2[^>]*>\s*(\d+)\.\s*Chapter', content)
        if tm and h2:
            book, chap = int(tm.group(2)), int(h2.group(1))
        paras = re.findall(r'<p[^>]*>(.*?)</p>', content, re.S)
        text = '\n\n'.join(clean_ws(htmlmod.unescape(re.sub(r'<[^>]+>', '', p))) for p in paras)
        results[(book, chap)] = text
    return results

# ---------------------------------------------------------------- Harivamsa
def norm_harivamsa():
    txt = strip_gutenberg_header(open(os.path.join(RAW, 'harivamsa', 'harivamsa_dutt_gutenberg61937.txt'),
                                      encoding='utf-8', errors='replace').read())
    # body chapter headings: "CHAPTER I. TITLE" (no dot-leaders). TOC lines end with '.....' page refs.
    markers = [(m.start(), m.group(1), m.group(2).strip()) for m in
               re.finditer(r'^CHAPTER\s+([IVXLCDM]+)\.\s+(.+)$', txt, re.M)]
    markers = [(pos, num, re.sub(r'\s*\.{3,}\d*\s*$', '', title).rstrip('.').strip())
               for pos, num, title in markers if not re.search(r'\.{3,}\s*\d*$', title)]
    # Bhavishya Parva boundary — use the LAST occurrence (body heading, not TOC entry)
    bh = txt.rfind('BHAVISHYA PARVA OR THE BOOK OF FUTURE.')
    results = {1: {}, 2: {}}
    for i, (pos, num, title) in enumerate(markers):
        part = 2 if pos > bh else 1
        endpos = markers[i + 1][0] if i + 1 < len(markers) else len(txt)
        body = clean_paras(txt[pos:endpos])
        nl = body.find('\n')
        body = clean_ws(body[nl:] if nl > 0 else body)
        sn = r2i(num)
        results[part][sn] = {'title': title, 'text': body}
    return results

# ---------------------------------------------------------------- Bhagavata Sanskrit
def norm_bhagavata_sanskrit():
    txt = open(os.path.join(RAW, 'bhagavata', 'bhagavata_sanskrit_gretil.txt'), encoding='utf-8', errors='replace').read()
    i = txt.find('# Text')
    txt = txt[i + 6:] if i > 0 else txt
    chunks = re.split(r'//\s*bhp_(\d+)\.(\d+)\.(\d+)([/*]?)\s*//', txt)
    results = {}
    for k in range(1, len(chunks) - 4, 5):
        c, ch, v = int(chunks[k]), int(chunks[k + 1]), int(chunks[k + 2])
        vtext = clean_ws(chunks[k + 4])
        if not vtext:
            continue
        results.setdefault((c, ch), {})[v] = vtext
    return results

# ---------------------------------------------------------------- main
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    registry = []

    print('== Mahabharata ==')
    mb = norm_mahabharata()
    total_sec = 0
    for bn in sorted(mb):
        for sn in sorted(mb[bn]):
            d = os.path.join(OUT, 'mahabharata', f'parva_{bn:02d}')
            os.makedirs(d, exist_ok=True)
            with open(os.path.join(d, f'section_{sn:03d}.txt'), 'w', encoding='utf-8') as f:
                f.write(mb[bn][sn])
            registry.append({'work': 'mahabharata', 'parva': bn, 'parva_name': PARVA_NAMES[bn], 'section': sn,
                             'file': f'mahabharata/parva_{bn:02d}/section_{sn:03d}.txt', 'chars': len(mb[bn][sn])})
            total_sec += 1
    print('  sections:', total_sec, '| parvas:', sorted(mb.keys()))

    print('== Vishnu Purana ==')
    vp = norm_vishnu_purana()
    for (book, chap), text in sorted(vp.items()):
        d = os.path.join(OUT, 'vishnu_purana', f'book_{book:02d}')
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, f'chapter_{chap:03d}.txt'), 'w', encoding='utf-8') as f:
            f.write(text)
        registry.append({'work': 'vishnu_purana', 'book': book, 'chapter': chap,
                         'file': f'vishnu_purana/book_{book:02d}/chapter_{chap:03d}.txt', 'chars': len(text)})
    books = sorted(set(b for b, _ in vp.keys()))
    print('  books:', books, '| chapters:', len(vp), '| book5 chapters:', sum(1 for b, _ in vp if b == 5))

    print('== Harivamsa ==')
    hv = norm_harivamsa()
    for part in sorted(hv):
        for sn in sorted(hv[part]):
            d = os.path.join(OUT, 'harivamsa', f'part_{part:02d}')
            os.makedirs(d, exist_ok=True)
            with open(os.path.join(d, f'chapter_{sn:03d}.txt'), 'w', encoding='utf-8') as f:
                f.write(f"TITLE: {hv[part][sn]['title']}\n\n{hv[part][sn]['text']}")
            registry.append({'work': 'harivamsa', 'part': part, 'chapter': sn, 'title': hv[part][sn]['title'],
                             'file': f'harivamsa/part_{part:02d}/chapter_{sn:03d}.txt', 'chars': len(hv[part][sn]['text'])})
    print('  parts:', sorted(hv.keys()), '| chapters per part:', {p: len(hv[p]) for p in hv})

    print('== Bhagavata Sanskrit ==')
    bp = norm_bhagavata_sanskrit()
    total_verses = 0
    for (c, ch), verses in sorted(bp.items()):
        d = os.path.join(OUT, 'bhagavata_sanskrit', f'canto_{c:02d}')
        os.makedirs(d, exist_ok=True)
        body = '\n'.join(f'{v}. {verses[v]}' for v in sorted(verses))
        with open(os.path.join(d, f'chapter_{ch:03d}.txt'), 'w', encoding='utf-8') as f:
            f.write(body)
        registry.append({'work': 'bhagavata_sanskrit', 'canto': c, 'chapter': ch, 'verses': len(verses),
                         'file': f'bhagavata_sanskrit/canto_{c:02d}/chapter_{ch:03d}.txt', 'chars': len(body)})
        total_verses += len(verses)
    cantos = sorted(set(c for c, _ in bp.keys()))
    print('  cantos:', cantos, '| chapters:', len(bp), '| verses:', total_verses)
    c10 = sum(len(v) for (c, ch), v in bp.items() if c == 10)
    print('  canto 10 chapters:', sum(1 for (c, ch) in bp if c == 10), '| canto 10 verses:', c10)

    with open(os.path.join(OUT, 'registry.json'), 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=1, ensure_ascii=False)
    print('registry entries:', len(registry))
    print('DONE')
