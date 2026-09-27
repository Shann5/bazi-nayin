// 从两个 MIT 引擎实跑取藏干：lunar-typescript（成员与次序）、tyme4ts（人元司令分野天数）。
// tyme4ts 的天数按实际节气区间给，这里取 2025 各节后一个月逐日跑，数出每段天数。
const { LunarUtil } = require('/Users/shanliu/idea-2026/AuspiceOracle/node_modules/lunar-typescript')
const T = require('./package/dist/lib/index.cjs')
const BR = '子丑寅卯辰巳午未申酉戌亥'
const out = { lunar: {}, tyme: {} }
for (const b of BR) out.lunar[b] = LunarUtil.ZHI_HIDE_GAN[b]
// 月支 → 该月节（寅=立春 index 3 …）
const JIE = { 寅: 3, 卯: 5, 辰: 7, 巳: 9, 午: 11, 未: 13, 申: 15, 酉: 17, 戌: 19, 亥: 21, 子: 23, 丑: 1 }
for (const b of BR) {
  const y = b === '子' ? 2025 : b === '丑' ? 2026 : 2025
  const start = T.SolarTerm.fromIndex(y, JIE[b]).getSolarDay()
  const end = T.SolarTerm.fromIndex(y, JIE[b] + 2).getSolarDay()
  const runs = []
  for (let d = start; d.isBefore(end); d = d.next(1)) {
    const h = d.getHideHeavenStemDay().getHideHeavenStem()
    const stem = h.getName(), type = { [T.HideHeavenStemType.RESIDUAL]: 'residual', [T.HideHeavenStemType.MIDDLE]: 'middle', [T.HideHeavenStemType.MAIN]: 'main' }[h.getType()]
    const last = runs[runs.length - 1]
    if (last && last.stem === stem) last.days++
    else runs.push({ stem, type, days: 1 })
  }
  out.tyme[b] = { year: y, runs }
}
// tyme4ts 源码里编码的名义天数表（dist 中 getHideHeavenStemDay 的 data 串，逐节 3 组「干序+天数档」）。
// 实跑与名义不同：首段恒多 1 天（判定用 dayIndex <= days，节气当日也算进首段）。两份都记。
{
  const src = require('fs').readFileSync('./package/dist/lib/index.cjs.js', 'utf8')
  const data = src.match(/data="([0-9x]{72})"/)[1]
  const dayCounts = JSON.parse(src.match(/dayCounts=(\[[0-9,]+\])/)[1])
  const STEMS = '甲乙丙丁戊己庚辛壬癸'
  const JIE_ORDER = { 丑: 1, 寅: 3, 卯: 5, 辰: 7, 巳: 9, 午: 11, 未: 13, 申: 15, 酉: 17, 戌: 19, 亥: 21, 子: 23 }
  out.tyme_nominal = {}
  for (const [b, idx] of Object.entries(JIE_ORDER)) {
    const seg = data.substr(3 * (idx - 1), 6), parts = []
    ;['residual', 'middle', 'main'].forEach((type, k) => {
      const s = seg[2 * k], c = seg[2 * k + 1]
      if (s !== 'x') parts.push({ stem: STEMS[+s], type, days: type === 'main' ? null : dayCounts[+c] })
    })
    out.tyme_nominal[b] = parts
  }
}
out.versions = { 'lunar-typescript': require('/Users/shanliu/idea-2026/AuspiceOracle/node_modules/lunar-typescript/package.json').version, tyme4ts: require('./package/package.json').version }
require('fs').writeFileSync(process.argv[2], JSON.stringify(out, null, 1))
for (const b of BR) console.log(b, out.lunar[b].join(''), out.tyme[b].runs.map(r => r.stem + r.days + r.type.slice(0, 3)).join(' '))
