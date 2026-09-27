"""藏干跨源对照：四份古籍 + 三份引擎口径 → 长表 + 逐支对照 + 分歧清单。

python3 build.py
（engines.json 由 `node engines.cjs engines.json` 生成，需 lunar-typescript 与 tyme4ts；
 结果已入库，重建数据不需要 node。）
"""
import json, csv
from curated import SOURCES, C, NOTES

BR = '子丑寅卯辰巳午未申酉戌亥'
STEM_EL = dict(zip('甲乙丙丁戊己庚辛壬癸', '木木火火土土金金水水'))
errs, rows = [], []

# ---------- 古籍 ----------
texts = {k: open(v['file'], encoding='utf-8').read() for k, v in SOURCES.items()}
for sid, entries in C.items():
    seen = set()
    for br, stems, quote in entries:
        seen.add(br)
        if quote not in texts[sid]:
            errs.append(('quote not in source', sid, br, quote))
        for pos, (raw, stem, days) in enumerate(stems, 1):
            if raw not in quote:
                errs.append(('stem not in quote', sid, br, raw))
            rows.append(dict(source=sid, kind='classical', branch=br, position=pos, stem_raw=raw, stem=stem or '',
                             element=STEM_EL.get(stem, '土' if raw.endswith('土') else ''), role='',
                             days=days, weight='', note=NOTES.get((sid, br, raw), ''), quote=quote))
    if seen != set(BR):
        errs.append(('branches missing', sid, set(BR) - seen))

# ---------- 引擎 ----------
E = json.load(open('engines.json', encoding='utf-8'))
ROLE = ['main', 'middle', 'residual']
W = [0.6, 0.3, 0.1]           # lib/bazi/wuxing.ts HIDDEN_WEIGHTS，按藏干位次取，未按支归一
for br in BR:
    for pos, stem in enumerate(E['lunar'][br], 1):
        rows.append(dict(source='lunar-typescript', kind='engine', branch=br, position=pos, stem_raw=stem, stem=stem,
                         element=STEM_EL[stem], role=ROLE[pos - 1], days=None, weight='', note='', quote=''))
        rows.append(dict(source='auspice-engine', kind='engine', branch=br, position=pos, stem_raw=stem, stem=stem,
                         element=STEM_EL[stem], role=ROLE[pos - 1], days=None, weight=W[pos - 1],
                         note='weights not normalised per branch' if pos == len(E['lunar'][br]) and len(E['lunar'][br]) < 3 else '',
                         quote=''))
    for pos, p in enumerate(E['tyme_nominal'][br], 1):
        others = sum(x['days'] for x in E['tyme_nominal'][br] if x['days'])
        rows.append(dict(source='tyme4ts-nominal', kind='engine', branch=br, position=pos, stem_raw=p['stem'], stem=p['stem'],
                         element=STEM_EL[p['stem']], role=p['type'], days=p['days'] if p['days'] else 30 - others,
                         weight='', note='' if p['days'] else 'remainder of a nominal 30-day month', quote=''))
    for pos, r in enumerate(E['tyme'][br]['runs'], 1):
        rows.append(dict(source='tyme4ts-as-run', kind='engine', branch=br, position=pos, stem_raw=r['stem'], stem=r['stem'],
                         element=STEM_EL[r['stem']], role=r['type'], days=r['days'], weight='',
                         note=f"counted day by day, {E['tyme'][br]['year']} solar-term month", quote=''))

ENGINE_META = {
    'lunar-typescript': dict(title='lunar-typescript LunarUtil.ZHI_HIDE_GAN', version=E['versions']['lunar-typescript'],
                             url='https://github.com/6tail/lunar-typescript', license='MIT'),
    'tyme4ts-nominal': dict(title='tyme4ts SolarDay.getHideHeavenStemDay — table encoded in source', version=E['versions']['tyme4ts'],
                            url='https://github.com/6tail/tyme4ts', license='MIT'),
    'tyme4ts-as-run': dict(title='tyme4ts SolarDay.getHideHeavenStemDay — counted by running it', version=E['versions']['tyme4ts'],
                           url='https://github.com/6tail/tyme4ts', license='MIT'),
    'auspice-engine': dict(title='Auspice strength weights (lib/bazi/wuxing.ts HIDDEN_WEIGHTS over lunar-typescript order)',
                           version='2026-09', url='https://auspiceoracle.com/en/method', license='—'),
}

print('errors:', errs or 'none')
assert not errs

# ---------- 逐支对照 ----------
ORDER = ['sanming-a', 'sanming-b', 'yuanhai-zangdun', 'yuanhai-anzang', 'lunar-typescript', 'tyme4ts-nominal', 'tyme4ts-as-run']
by = {}
for r in rows:
    if r['source'] == 'auspice-engine':
        continue
    by.setdefault(r['branch'], {}).setdefault(r['source'], []).append(r)


def cell(rs):
    return ' '.join(f"{r['stem'] or r['stem_raw']}{r['days'] if r['days'] else ''}" for r in rs)


compare = []
for br in BR:
    distinct = sorted({r['stem'] or r['stem_raw'] for s in ORDER for r in by[br][s]})
    compare.append(dict(branch=br, **{s: cell(by[br][s]) for s in ORDER}, stems_seen=' '.join(distinct)))

# 两个问题分开比：「支里藏什么」（成分）与「一月之内谁当令几天」（司令）。
# 跨问题比较会凭空造出分歧（司令表的子月都有壬，成分表的子只有癸），所以只在同一问题内比。
FAMILY = {
    'contents': ['yuanhai-zangdun', 'lunar-typescript'],
    'command': ['sanming-a', 'sanming-b', 'yuanhai-anzang', 'tyme4ts-nominal'],
}
diffs, agree = [], {}
for fam, srcs in FAMILY.items():
    agree[fam] = 0
    for br in BR:
        sets = {s: {r['stem'] or r['stem_raw'] for r in by[br][s]} for s in srcs}
        if len({frozenset(v) for v in sets.values()}) == 1:
            agree[fam] += 1
        for st in sorted(set().union(*sets.values())):
            have = [s for s in srcs if st in sets[s]]
            if len(have) != len(srcs):
                diffs.append(dict(family=fam, branch=br, stem=st, in_sources=' '.join(have),
                                  not_in=' '.join(s for s in srcs if s not in have)))

# ---------- 输出 ----------
FIELDS = ['source', 'kind', 'branch', 'position', 'stem_raw', 'stem', 'element', 'role', 'days', 'weight', 'note', 'quote']
with open('hidden-stems.long.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=FIELDS); w.writeheader(); w.writerows(rows)
with open('hidden-stems.compare.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['branch'] + ORDER + ['stems_seen']); w.writeheader(); w.writerows(compare)
for k, v in SOURCES.items(): v['family'] = 'command' if k in FAMILY['command'] else 'contents'
for k, v in ENGINE_META.items(): v['family'] = 'contents' if k in ('lunar-typescript', 'auspice-engine') else 'command'
json.dump(dict(sources={**SOURCES, **ENGINE_META}, families=FAMILY, rows=rows, compare=compare, differences=diffs),
          open('hidden-stems.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

print(f'rows: {len(rows)}')
for fam in FAMILY:
    print(f'{fam}: branches where all sources list the same stems: {agree[fam]}/12;',
          'differences:', sum(d["family"] == fam for d in diffs))
for c in compare:
    print(c['branch'], ' | '.join(c[s] for s in ORDER))
