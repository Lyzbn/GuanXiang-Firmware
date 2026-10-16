# GuanXiang

Offline three-coin I Ching and self-study firmware for **M5Stack Cardputer ADV**, with a dark landscape interface, warm gold text, and local reading history. Learn the eight trigrams and explore all 64 hexagrams without making a cast.

**The updated 1.1.0 candidate passed fixed-source CI and was written to the device application partition. The serial boot smoke test passed; user acceptance is in progress, with no user result recorded yet, and firmware remains unpublished.** The written application digest matches, and all 20,480 NVS bytes remain identical to the pre-upgrade state. These checks do not establish acceptance of the display, controls or history interface. Matching release materials are being updated; application source remains private. [中文](README.md)

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

## Casting and history

Press Enter once to spin and again to toss for each line: twelve presses complete a six-line cast. Explore the primary hexagram, moving lines and changed hexagram. Choose relaxed or snappy timing, sound and reduced motion independently. An optional intention accepts up to 24 ASCII bytes; local history holds twelve entries. No network or microSD is needed.

The firmware interface and reading texts are in Chinese; this English guide does not imply an English firmware interface.

## Planned installation assets

| Installation | Flash address | Existing history and settings |
| --- | --- | --- |
| Complete merged image | `0x0` | Resets NVS; preserve important records first |
| Compatible GuanXiang application update | `0x10000` | Does not write NVS; requires matching partitions and app0 boot selection |

Follow the final package instructions and checksums once released. Existing history and settings formats remain unchanged. Device interaction, history retention and cold starts still require acceptance for the expanded-reading and self-study candidate. Matching installation assets, checksums and relink materials are being updated. No public 1.1.0 release download is available.

## Validation status

The updated **1.1.0** application source is `38f2db6`. Local Release and Debug builds and **238,355 native checks** passed. Main-reading checks cover **13,522 layouts and 214,191 bounds**; study checks cover **5,359 layouts and 34,070 bounds**, with zero errors. The two galleries contain 68 and 29 host previews respectively. Fixed-source CI `38964682642` passed; the selected Linux application image is **1,567,440 bytes**. Its digest and device-check boundaries are recorded in [VALIDATION.md](VALIDATION.md).

The updated candidate is flashed, with the serial boot smoke test passed and user acceptance in progress; no user result has been recorded yet. Device evidence for earlier applications, including the previous three-mode draft, applies only to those images. The [validation record](VALIDATION.md) will distinguish each artifact and its device results; the [release notes](RELEASE_NOTES_v1.1.0.md) remain a candidate draft.

## Release materials

Firmware downloads will appear on the [releases page](https://github.com/Lyzbn/GuanXiang-Firmware/releases) after candidate device acceptance. See the [installation guide](INSTALL.md), [third-party notices](THIRD_PARTY_NOTICES.md) and [font sources](FONT_SOURCES.md).
