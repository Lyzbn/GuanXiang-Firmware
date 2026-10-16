# GuanXiang

Offline three-coin I Ching and self-study firmware for **M5Stack Cardputer ADV**, with a dark landscape interface, warm gold text, and local reading history. Learn the eight trigrams and explore all 64 hexagrams without making a cast.

**v1.1.0-rc.1 is publicly available as a prerelease**, with three reading modes, continuous moving-line reading and self-study for all 64 hexagrams. Fixed-source CI and this release’s device acceptance checks passed. All study cards pair a 40px name with the hexagram figure. [Download the prerelease](https://github.com/Lyzbn/GuanXiang-Firmware/releases/tag/v1.1.0-rc.1). Application source remains private. [中文](README.md)

## Three reading modes

Both primary and changed hexagrams support all three modes across the 64 hexagrams:

- **Summary / 短意**: the default, with two four-character modern lines per hexagram.
- **Insight / 精意**: four sections on each hexagram’s situation, principles, practical considerations and common misreadings, followed by commentary excerpts and sources.
- **Classical / 古文**: the complete judgment text, rather than a shortened two-line excerpt.

Expanded readings cover **64 hexagrams**, with **386 individual readings: 384 lines plus the special Use of Nine and Use of Six texts**. Each line separates explanation of the cited commentary from present-day reflections. Long text is split by section and page, with a 16px body and at most four lines per screen.

Canonical texts, excerpts from Wang Bi’s commentary and Kong Yingda’s subcommentary, and GuanXiang’s modern interpretations are labelled separately. The modern text was prepared by the project with AI assistance and checked against classical sources; it is not an existing translation by those commentators or a modern scholar. Modern books are recommendations for further reading, not permissions or endorsements. The classical collection includes 64 complete judgments, 64 Great Images, 384 line texts and 384 Small Images, plus the special texts and Small Images for Qian and Kun. It is not the complete Yi Zhuan collection.

See the [source and editorial notes](TEXT_SOURCES.md), [all 64 expanded and 386 line/special-text readings with sources](readings.json), and the [twelve lessons, diagrams and 64 Great Images](study-content.json).

Press **I** on the home screen to open settings. **T** cycles and saves the default reading mode there. On a hexagram reading page, **T** changes only the current reading session and returns to page one; it does not save a new default. Opening a history entry applies the saved default and does not create another entry.

Use **Up/Down** to turn pages, or **Enter** to advance. Moving-line reading finishes every page of each card, then follows **line text → Small Image → Insight → next moving line → changed hexagram**. The final moving line leads directly to the changed hexagram. When all lines of Qian or Kun move, the special Use of Nine or Use of Six is completed first. Left/Right still switches cards directly.

## Learn the 64 hexagrams

Press **L** on the home screen. Study does not require a cast or create a history entry.

1. **Twelve foundation lessons** introduce yin and yang, reading lines from bottom to top, and the eight trigrams through traditional mnemonics and diagrams.
2. **Combine two trigrams** to see the resulting six-line figure, name and number. Li below Kan forms Jiji; reversing them forms Weiji. Up/Down selects the upper or lower trigram, and Left/Right changes it.

3. **Explore all 64 in the conventional order**, with Left/Right jumping eight entries. Read the judgment, Great Image, Insight, six lines and sources using the same material as casting. Returning preserves the catalogue or combination position.

Each study card uses a **40px name beside the hexagram figure**, with upper/lower trigram labels above and two short summary lines below. The layout supports all 64 hexagrams.

## Casting and history

Press Enter once to spin and again to toss for each line: twelve presses complete a six-line cast. Explore the primary hexagram, moving lines and changed hexagram. Choose relaxed or snappy timing, sound and reduced motion independently. An optional intention accepts up to 24 ASCII bytes; local history holds twelve entries. No network or microSD is needed.

The firmware interface and reading texts are in Chinese; this English guide does not imply an English firmware interface.

## Installation assets

| Installation | Flash address | Existing history and settings |
| --- | --- | --- |
| Complete merged image | `0x0` | Resets NVS; preserve important records first |
| Compatible GuanXiang application update | `0x10000` | Does not write NVS; requires matching partitions and app0 boot selection |

Follow the prerelease package instructions and checksums. Existing history and settings formats remain unchanged. The user accepted the large-name cards, confirmed preserved old history/settings, completed primary/moving-line/changed-hexagram reading with exactly one new history entry, and verified USB and battery cold starts with the new data retained. Prerelease assets, checksums and relink materials are available on the [download page](https://github.com/Lyzbn/GuanXiang-Firmware/releases/tag/v1.1.0-rc.1).

## Validation status

The public **v1.1.0-rc.1 prerelease** retains source-version metadata `1.1.0-dev`. Its application source is `ae85426`. The local Release build and fixed-source CI, including 238,355 native regression checks, passed. Main-reading checks cover **13,522 layouts and 214,191 bounds**; study checks cover **5,362 layouts and 34,342 bounds**, with zero errors. The two galleries contain 68 and 32 host previews respectively. Fixed-source CI `38967327177` passed; the selected Linux application image is **1,567,632 bytes**. Its digest and device-check boundaries are recorded in [VALIDATION.md](VALIDATION.md).

The new candidate passed app-only writing, independent flash verification, NVS preservation and the serial boot smoke test; user acceptance passed. Matching relink and modified-framework rebuild checks also passed; native execution of the public Linux wrapper remains pending. The [validation record](VALIDATION.md) will distinguish each artifact and its device results; the [release notes](RELEASE_NOTES_v1.1.0.md) describe this prerelease.

## Release materials

Prerelease firmware downloads are available on the [release page](https://github.com/Lyzbn/GuanXiang-Firmware/releases/tag/v1.1.0-rc.1). See the [installation guide](INSTALL.md), [third-party notices](THIRD_PARTY_NOTICES.md) and [font sources](FONT_SOURCES.md).
