# Fonts / 字体来源

The v1.1.0-rc.2 pagination fix retains the font data of v1.1.0-rc.1
(application source `ae85426`, unchanged from `38f2db6`). Runtime title and UI
glyphs were regenerated from official font inputs; this release adds no new fonts.
Both font subsets are distributed under SIL Open Font License 1.1; their licenses
apply independently from the proprietary application license.

- Noto Serif CJK SC Black 2.003: 32px brand/ceremony, 40px hexagram names.
  © 2017-2024 Adobe (http://www.adobe.com/).
  [Official source](https://github.com/notofonts/noto-cjk/tree/main/Serif),
  [license](licenses/NotoSerif-LICENSE.txt).
- GNU Unifont 17.0.04: 972 16px UI and short-reading glyphs, plus a separate
  317-glyph body-text supplement for the expanded readings and study pages.
  Copyright © 1998-2026 Roman Czyborra, Paul Hardy, Qianqian Fang, Andrew Miller,
  Johnnie Weaver, David Corbett, Ælla Chiana Moskopp, Rebecca Bettencourt,
  Ho-Seok Ee, et al.
  [Official source](https://unifoundry.com/unifont/index.html),
  [OFL license](licenses/Unifont-OFL-1.1.txt),
  [upstream dual-license statement](licenses/Unifont-COPYING.txt).
- Long paragraphs retain M5GFX efontCN_16 and the separately credited Noto Serif
  CJK SC Regular classical fallback subset, with the 317-glyph official Unifont
  supplement where needed. The body-text coverage audit checks 2,241 distinct
  characters across the included texts; this is a coverage total, not the size
  of a single font subset. Short readings use 234 distinct characters. Complete
  third-party notices and the efont copyright text accompany the release packages.

大字可复现原有像素；原417个小字中407个与官方Unifont一致，
其余10字“→养卦受回月美辞：？”采用官方字形。当前界面子集为972字，
另有317个新增正文补字；正文覆盖审计共2241字，短意用字234字。
这些是不同范围的统计，不能将2241当成某一子集字数，也不能把各数简单相加。
版本固定是为了复现，并不表示采用上游最新版。

The original font inputs and generated subsets have pinned SHA-256 digests in
[font-manifest.json](font-manifest.json). The manifest records reproducible sources;
it contains no device backups or user history. The manifest is copied exactly
from the 38 candidate’s official-font metadata and has been verified byte-identical
to the rc.1 `ae85426` commit. The rc.2 fix leaves these font files unchanged. Its `ui_16` entry
records the 972-glyph UI subset; the separate body supplement is described above.
Its SHA-256 is `918c2a8e8cc25c7b7de9aadf06be7ffbeb4ff34c337229dd8e3d42106a5f623d`.
