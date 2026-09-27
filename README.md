# The Thirty Nayin (纳音) — English Translations & Dataset

The **nayin** (纳音, *nà yīn*, "received tones") are thirty poetic sound-images from
Chinese metaphysics. Each one covers two adjacent pairs of the sixty Jiazi (六十甲子)
stem-branch cycle and attaches an elemental image to them — not just *Metal*, but
*Gold in the Sea*; not just *Fire*, but *Thunderbolt Fire*.

English resources for BaZi (八字, Four Pillars of Destiny) are inconsistent about these
names — the same nayin gets rendered three or four different ways across sites, which
makes cross-referencing painful. This repo is a small, carefully considered set of
English translations, published as open data.

**Translation principles**

1. **Keep the image, not the word order.** 海中金 is "Gold in the Sea", not "Sea Middle Gold".
2. **Say *Gold* when the image is refined treasure, *Metal* when it is raw or forged** — 海中金 / 沙中金 are gold; 剑锋金 (sword-edge) stays metal.
3. **Use the established English term where one exists** (e.g. Milky Way for 天河), and plain concrete English elsewhere.

Full explanations of each image — what "Gold in the Sea" actually implies in a reading —
are on the reference page this dataset comes from:
**[The 30 Nayin, explained →](https://auspiceoracle.com/en/content/nayin)**

## The table

| Ganzhi pairs | 纳音 | Pinyin | English | Element |
|---|---|---|---|---|
| 甲子·乙丑 | 海中金 | *hǎi zhōng jīn* | Gold in the Sea | Metal |
| 丙寅·丁卯 | 炉中火 | *lú zhōng huǒ* | Fire in the Furnace | Fire |
| 戊辰·己巳 | 大林木 | *dà lín mù* | Great Forest Wood | Wood |
| 庚午·辛未 | 路旁土 | *lù páng tǔ* | Roadside Earth | Earth |
| 壬申·癸酉 | 剑锋金 | *jiàn fēng jīn* | Sword-Edge Metal | Metal |
| 甲戌·乙亥 | 山头火 | *shān tóu huǒ* | Hilltop Fire | Fire |
| 丙子·丁丑 | 涧下水 | *jiàn xià shuǐ* | Water in the Ravine | Water |
| 戊寅·己卯 | 城头土 | *chéng tóu tǔ* | City Wall Earth | Earth |
| 庚辰·辛巳 | 白蜡金 | *bái là jīn* | White Wax Metal | Metal |
| 壬午·癸未 | 杨柳木 | *yáng liǔ mù* | Willow Wood | Wood |
| 甲申·乙酉 | 泉中水 | *quán zhōng shuǐ* | Water in the Spring | Water |
| 丙戌·丁亥 | 屋上土 | *wū shàng tǔ* | Rooftop Earth | Earth |
| 戊子·己丑 | 霹雳火 | *pī lì huǒ* | Thunderbolt Fire | Fire |
| 庚寅·辛卯 | 松柏木 | *sōng bǎi mù* | Pine and Cypress Wood | Wood |
| 壬辰·癸巳 | 长流水 | *cháng liú shuǐ* | Long-Flowing Water | Water |
| 甲午·乙未 | 沙中金 | *shā zhōng jīn* | Gold in the Sand | Metal |
| 丙申·丁酉 | 山下火 | *shān xià huǒ* | Fire at the Foothill | Fire |
| 戊戌·己亥 | 平地木 | *píng dì mù* | Wood on Level Ground | Wood |
| 庚子·辛丑 | 壁上土 | *bì shàng tǔ* | Earth on the Wall | Earth |
| 壬寅·癸卯 | 金箔金 | *jīn bó jīn* | Gold Foil Metal | Metal |
| 甲辰·乙巳 | 覆灯火 | *fù dēng huǒ* | Sheltered Lamp Fire | Fire |
| 丙午·丁未 | 天河水 | *tiān hé shuǐ* | Water of the Milky Way | Water |
| 戊申·己酉 | 大驿土 | *dà yì tǔ* | Post-Road Earth | Earth |
| 庚戌·辛亥 | 钗钏金 | *chāi chuàn jīn* | Hairpin Metal | Metal |
| 壬子·癸丑 | 桑柘木 | *sāng zhè mù* | Mulberry Wood | Wood |
| 甲寅·乙卯 | 大溪水 | *dà xī shuǐ* | Water of the Great Stream | Water |
| 丙辰·丁巳 | 沙中土 | *shā zhōng tǔ* | Earth in the Sand | Earth |
| 戊午·己未 | 天上火 | *tiān shàng huǒ* | Fire in the Sky | Fire |
| 庚申·辛酉 | 石榴木 | *shí liú mù* | Pomegranate Wood | Wood |
| 壬戌·癸亥 | 大海水 | *dà hǎi shuǐ* | Water of the Great Sea | Water |

## Data

Machine-readable copies live in [`data/`](data/):

- [`nayin.json`](data/nayin.json) — array of 30 entries: `hanzi`, `pinyin`, `english`, `element`, `element_en`, `ganzhi` (the two stem-branch pairs), `ganzhi_pinyin`
- [`nayin.csv`](data/nayin.csv) — same data, one row per nayin

The ganzhi→nayin pairing follows the traditional sixty Jiazi order (甲子乙丑海中金 …
壬戌癸亥大海水), cross-checked against [lunar-typescript](https://github.com/6tail/lunar-typescript).

Also mirrored on the Hugging Face Hub, if that is where you work:
**[huggingface.co/datasets/Shann5/bazi-nayin](https://huggingface.co/datasets/Shann5/bazi-nayin)**
(`load_dataset("Shann5/bazi-nayin")`). This repo is the source of truth — the mirror is
generated from it, and corrections belong here as issues.

## v2 — what the classical text says about each pillar, and about meetings

v1 names the thirty images. v2 adds **how they were read**, structured from volume 1 of
the *Sānmìng Tōnghuì* (三命通會, Ming dynasty, Siku Quanshu edition on
[Chinese Wikisource](https://zh.wikisource.org/wiki/三命通會_(四庫全書本)/卷01)). Every
relation carries a short verbatim quote, and the build fails if any quote is not found
word for word in the source text ([`classical/`](classical/)).

**[`data/v2/pillars.json`](data/v2/pillars.json)** (+ [`.csv`](data/v2/pillars.csv)) — all sixty stem-branch pillars:

| Field | From the chapter | Example (甲午, Gold in the Sand) |
|---|---|---|
| `arc` | 論納音取象 — the thirty images read in order as one life of qi, in six stages by branch pair | stage 4, *Revealed* — "fully formed" |
| `image`, `likes` | 釋六十甲子性質吉凶, the per-pillar note | "gold refined a hundred times"; likes water, wood, earth |
| `relations` | the per-pillar paragraphs: `welcome`, `avoid`, `unharmed_by`, `state` + `quotes` | welcomes fire — 「遇火生旺其器乃成」 ("meeting strong fire, the vessel is made") |
| `scale` | the *large absorbs small* rule for same-element nayin across the four pillars | Pine and Cypress Wood (large) absorbs Willow Wood (small) |

**[`data/v2/matrix.json`](data/v2/matrix.json)** (+ [`.csv`](data/v2/matrix.csv), [`matrix.en.csv`](data/v2/matrix.en.csv), and [`matrix.long.csv`](data/v2/matrix.long.csv) — one row per meeting, for pandas / `datasets`) — nayin × nayin, from the thirty
chapters that each describe one image meeting the others. Row = the image whose chapter
it is; column = the one it meets.

| | meaning | share of 663 filled cells |
|---|---|---|
| `+` | welcomes | 42% |
| `~` | conditional — the condition is in the quote ("fine if water is present") | 29% |
| `-` | avoids | 18% |
| `0` | no effect ("of no use") | 11% |

Cells marked `*` in the CSV are filled from a blanket statement ("other metals are of no
use"), not named directly. Empty cells: the text says nothing — they are left empty.

**The relations are directional.** In 41 pairs the two chapters disagree: Sword-Edge
Metal welcomes Willow Wood (it can cut it); Willow Wood avoids Sword-Edge Metal (it gets
cut). Ask "who benefits from this meeting", not "are these compatible".

**What this is not.** A record of what one Ming-dynasty text says, not a claim that any
of it comes true. 喜 / 忌 ("welcome" / "avoid") are the text's words, reported as found.
Nayin belongs to an older lineage than the day-master method most modern BaZi uses; the
two assign different elements to the same pillar, and this table does not feed any
strength calculation. Where the text contradicts itself, both readings are kept
(`textual_notes`). The verdict for each quote is a curation call — if you read one
differently, open an issue with the chapter and line.

The source of truth is a private repo; this folder is regenerated from it. Issues welcome;
PRs that change data will be redirected to an issue.

## Usage note: your input time is probably wrong

A nayin lookup keys off the stem-branch (ganzhi) pillars, and the pillars key off
the birth *time* — in solar time, not clock time. Clock time can be off by well
over an hour once you stack historical DST rules, longitude offset from the zone's
standard meridian (4 min/degree; Ürümqi runs ~2 h ahead of the sun), and the
equation of time (±16 min). Near a two-hour branch boundary that's the difference
between two different pillars, i.e. two different nayin.

The calculator this dataset comes from corrects for all three. How the correction
works, with a city-by-city table:
**[True solar time, explained →](https://auspiceoracle.com/en/content/true-solar-time)**

## License & attribution

Data and translations are **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)**
(SPDX: `CC-BY-4.0`). The full legal text is in [`LICENSE`](LICENSE).

In plain terms: share and adapt them freely — in apps, articles, datasets, training
corpora, commercial or not — as long as you credit the source with a link and say so
if you changed anything.

Copy-paste attribution:

> Nayin translations by [Auspice Oracle](https://auspiceoracle.com), used under
> [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Copyright © 2026 Auspice Oracle (https://auspiceoracle.com).

The classical source text in [`classical/`](classical/) is in the public domain (Ming-dynasty work, transcribed on Wikisource).
