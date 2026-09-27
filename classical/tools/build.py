import json, csv, re
from extract import norm, SIXTY, raw
from curated import C
import en, os
ELEM = '金木水火土'
full = norm(''.join(raw))
d = json.load(open('nayin-v2.raw.json', encoding='utf-8'))
by = {r['ganzhi']: r for r in d['ganzhi']}
errs = []
for gzs, rel, quotes in C:
    for q in quotes:
        if q not in full: errs.append(('quote not in source', gzs, q))
    qq = ''.join(quotes)
    for k in ('welcome', 'avoid', 'unharmed'):
        for t in rel[k]:
            if len(t) == 2 and t not in SIXTY: errs.append(('bad ganzhi', gzs, t))
            if len(t) == 1 and t not in ELEM: errs.append(('bad element', gzs, t))
            if len(t) == 2 and t not in qq: errs.append(('ganzhi not in quote', gzs, t))
    for g in gzs:
        r = by[g]
        r.setdefault('relations', {'state': [], 'welcome': [], 'avoid': [], 'unharmed_by': [], 'quotes': [], 'textual_notes': []})
        R = r['relations']
        if rel['state']: R['state'].append(rel['state'])
        for k, kk in (('welcome', 'welcome'), ('avoid', 'avoid'), ('unharmed', 'unharmed_by')):
            R[kk] += [t for t in rel[k] if t not in R[kk]]
        R['quotes'] += quotes
        if rel.get('textual_note'): R['textual_notes'].append(rel['textual_note'])
missing = [g for g in SIXTY if 'relations' not in by[g]]
print('errors:', errs or 'none'); print('no relations:', missing or 'none')
# 英文层：缺一条就报错
site = '../../lib/labels.ts'
if os.path.exists(site):
    src = open(site, encoding='utf-8').read()
    for k, v in en.NAYIN_EN.items():
        if f"{k}: '{v}'" not in src: errs.append(('NAYIN_EN drift vs lib/labels.ts', k, v))
for r in d['ganzhi']:
    g = r['ganzhi']
    r['nayin_en'] = en.name_en(r['nayin'])
    r['arc']['label_en'] = en.ARC_EN[r['arc']['stage']]
    r['image_en'] = en.IMAGE_EN[g]
    r['likes_en'] = en.LIKES_EN[g]
    r['relations']['state_en'] = [en.STATE_EN[x] for x in r['relations']['state']]
assert not errs, errs
for r in d['ganzhi']:
    r.pop('state_label', None); r.pop('paragraph', None); r.pop('relations_auto', None)
json.dump(d, open('nayin-v2.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
with open('nayin-v2.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['ganzhi', 'nayin', 'nayin_en', 'nayin_element', 'scale', 'arc_stage', 'arc_branch_pair', 'image', 'image_en', 'likes', 'likes_en', 'state', 'state_en', 'welcome', 'avoid', 'unharmed_by'])
    for r in d['ganzhi']:
        R = r['relations']
        w.writerow([r['ganzhi'], r['nayin'], r['nayin_en'], r['nayin_element'], r['scale'] or '', r['arc']['stage'], r['arc']['branch_pair'], r['image'], r['image_en'], r['likes'], r['likes_en'],
                    '；'.join(R['state']), ' / '.join(R['state_en']), ' '.join(R['welcome']), ' '.join(R['avoid']), ' '.join(R['unharmed_by'])])
