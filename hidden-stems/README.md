# Hidden stems (藏干) across sources

Every earthly branch stores one to three heavenly stems. Chart apps print them as if the
table were settled. It is settled for one question and not for the other:

- **What does a branch contain?** (藏干, the contents) — the modern engines agree with
  each other and with one 16th-century verse, word for word.
- **Which stem is in command on which days of the month?** (人元司令, the command) —
  no two classical tables agree for all twelve branches, and one book disagrees with itself.

This folder puts the sources side by side, each classical row with a verbatim quote that
the build checks against the source text.

## Sources

| id | question | what it is |
|---|---|---|
| `sanming-a` | command | *Sanming Tonghui* 三命通會 vol. 2, 論人元司事, main text (Siku Quanshu edition) — days per stem |
| `sanming-b` | command | same section, the month-by-month table annotated with solar terms — a different set of days |
| `yuanhai-anzang` | command | *Yuanhai Ziping* 淵海子平, 論天干地支暗藏總訣 — a verse by solar term; only explicit numbers are taken |
| `yuanhai-zangdun` | contents | *Yuanhai Ziping*, 又地支藏遁歌 — the verse the modern table comes from |
| `lunar-typescript` | contents | `LunarUtil.ZHI_HIDE_GAN` (MIT), v1.8.6 |
| `tyme4ts-nominal` | command | `SolarDay.getHideHeavenStemDay` (MIT), v1.5.2 — the table encoded in its source |
| `tyme4ts-as-run` | command | the same function, counted day by day over a real year |
| `auspice-engine` | contents | the weights our own strength calculation puts on each hidden stem |

The Wikisource text of *Yuanhai Ziping* names no base edition; treat those two rows as a
weaker witness than the *Sanming Tonghui* rows.

## What the comparison shows

**Contents: 12 of 12 branches agree.** lunar-typescript reproduces the 藏遁歌 exactly,
main stem first.

**Command: the four tables never all agree on a branch.** Some of the difference is
wording (`sanming-a` writes 艮土 / 坤土, "earth of Gen / Kun", without saying 戊 or 己;
the 暗藏總訣 verse skips stems). What remains is real:

| | `sanming-a` | `sanming-b` | `tyme4ts-nominal` |
|---|---|---|---|
| storage stem in 辰 | **壬** 5 days | 癸 3 | 癸 3 |
| storage stem in 丑 | **庚** 5 | 辛 5 | 辛 3 |
| storage stem in 未 | **甲** 5 | 乙 5 | 乙 3 |
| storage stem in 戌 | **丙** 5 | 丁 5 | 丁 3 |
| 己 in 午 | none | none (乙 3 instead) | 己 9 |
| main stem days in 寅 (甲) | 20 | 18 | 16 |

The same section of the *Sanming Tonghui* also quotes a critic, 醉醒子, who rejects day
counts altogether: 「又豈可以三五七日為限哉」 — "how can it be limited to three, five or
seven days?"

**tyme4ts, nominal vs as run.** Run day by day, the first segment of every month is one
day longer than the encoded table (子: 壬 11 days, not 10), because the solar-term day
itself is counted into it. Whether that is intended is a convention question; both
versions are recorded.

**Weights.** Our engine weights hidden stems 0.6 / 0.3 / 0.1 by position. A branch
with one stem (子 卯 酉) therefore totals 0.6, two stems (午 亥) 0.9, three stems 1.0.

## Files

- `data/hidden-stems.long.csv` / `.json` — one row per (source, branch, stem): position,
  role, days, weight, note, verbatim quote
- `data/hidden-stems.compare.csv` — one row per branch, one column per source
- `classical/` — source texts and the build (`python3 build.py`; engine rows from
  `node engines.cjs engines.json`)

## What this is not

A record of what the sources say, not a ruling on which is right. The days in the
command tables are conventions for weighting the month; nothing here predicts anything.
Structured data CC BY 4.0; the classical texts are in the public domain.

---

## 中文摘要

藏干分两个问题：**支里藏什么**（成分）——现代引擎与《渊海子平·藏遁歌》逐字一致，12/12；
**一月之内谁当令几天**（人元司令）——四份表没有一支完全一致。三命通会正文把四库的墓气写成阳干
（辰壬、丑庚、未甲、戌丙），两份三命通会表的午里都没有己，寅中甲木的天数从 20 到 16 不等。
同一节还录了醉醒子的反对：「又豈可以三五七日為限哉」。每条古籍记录附原文，build 逐字核对。
