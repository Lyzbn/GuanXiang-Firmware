# GuanXiang

Offline three-coin I Ching firmware for **M5Stack Cardputer ADV**, with a dark landscape interface, warm gold text, and local reading history.

**Version 1.1.0 has passed build and host checks and remains an unpublished release candidate.** The Linux CI application image has been selected. It has not been flashed or accepted on hardware; licensing and matching relink materials are prepared. Application source remains private. [中文](README.md)

## Three reading modes

Both primary and changed hexagrams support all three modes across the 64 hexagrams:

- **Summary / 短意**: the default, with two four-character modern lines per hexagram.
- **Insight / 精意**: a longer modern explanation with complete pagination.
- **Classical / 古文**: the complete judgment text, rather than a shortened two-line excerpt.

The project prepares the modern readings from classical commentaries; they are not an existing scholarly translation. Classical coverage includes 64 complete judgments, 384 separately accessible line texts and their 384 Small Image commentaries, plus the applicable special texts and commentaries for Qian and Kun. It is not the complete Yi Zhuan collection.

See the [text sources and editorial notes](TEXT_SOURCES.md), or inspect [all 64 modern readings and their source records](readings.json).

Press **I** on the home screen to open settings. **T** cycles and saves the default reading mode there. On a hexagram reading page, **T** changes only the current reading session and returns to page one; it does not save a new default. Opening a history entry applies the saved default and does not create another entry.

Use **Up/Down** to turn pages, or **Enter** to advance. Summary and Insight offer the complete classical text after their final page. Classical mode proceeds to the next screen without repeating the same judgment. Moving-line pages retain complete line texts and Small Image commentaries.

## Casting and history

Press Enter once to spin and again to toss for each line: twelve presses complete a six-line cast. Explore the primary hexagram, moving lines and changed hexagram. Choose relaxed or snappy timing, sound and reduced motion independently. An optional intention accepts up to 24 ASCII bytes; local history holds twelve entries. No network or microSD is needed.

The firmware interface and reading texts are in Chinese; this English guide does not imply an English firmware interface.

## Planned installation assets

| Installation | Flash address | Existing history and settings |
| --- | --- | --- |
| Complete merged image | `0x0` | Resets NVS; preserve important records first |
| Compatible GuanXiang application update | `0x10000` | Does not write NVS; requires matching partitions and app0 boot selection |

Follow the final package instructions and checksums once released. The new reading default uses a separate storage key; existing history and settings formats remain unchanged. Offline application-upgrade checks passed, while history retention and cold starts still require acceptance on the new device build. Licensing and relink materials matching the selected image are prepared and relink checks passed. No public download is available.

## Validation status

Version **1.1.0** is frozen at application source commit `4d412daab3e4f18339637392813d51ea159af610`. The selected Linux CI application image is **1,202,112 bytes**; its SHA-256 is recorded in [VALIDATION.md](VALIDATION.md). **149,362 native checks**, **9,800 host layout checks** and the **62-page** preview audit passed, along with two CI rounds for the frozen application.

The candidate has not been flashed or accepted on hardware. Acceptance of the previous `b3a90f7a00e5f037e468d96917f6396db2b4dfeb` application applies only to that earlier image. See [validation records](VALIDATION.md) for current CI evidence and remaining work, and the [candidate release notes](RELEASE_NOTES_v1.1.0.md).

## Release materials

Firmware downloads will appear on the [releases page](https://github.com/Lyzbn/GuanXiang-Firmware/releases) after candidate device acceptance. See the [installation guide](INSTALL.md), [third-party notices](THIRD_PARTY_NOTICES.md) and [font sources](FONT_SOURCES.md).
