# Fonts / 字体来源

The 1.1.0 candidate regenerates runtime title and UI glyphs from official font inputs.
Both font subsets are distributed under SIL Open Font License 1.1; their licenses
apply independently from the proprietary application license.

- Noto Serif CJK SC Black 2.003: 32px brand/ceremony, 40px hexagram names.
  © 2017-2024 Adobe (http://www.adobe.com/).
  [Official source](https://github.com/notofonts/noto-cjk/tree/main/Serif),
  [license](licenses/NotoSerif-LICENSE.txt).
- GNU Unifont 17.0.04: 519 16px UI and short-reading glyphs.
  Copyright © 1998-2026 Roman Czyborra, Paul Hardy, Qianqian Fang, Andrew Miller,
  Johnnie Weaver, David Corbett, Ælla Chiana Moskopp, Rebecca Bettencourt,
  Ho-Seok Ee, et al.
  [Official source](https://unifoundry.com/unifont/index.html),
  [OFL license](licenses/Unifont-OFL-1.1.txt),
  [upstream dual-license statement](licenses/Unifont-COPYING.txt).
- Long paragraphs retain M5GFX efontCN_16 and the separately credited Noto Serif
  CJK SC Regular classical fallback subset. Complete third-party notices belong
  in the final distribution package.

大字可复现原有像素；原417个小字中407个与官方Unifont一致，
其余10字“→养卦受回月美辞：？”采用官方字形。本次同时补齐新短意所需字符。
版本固定是为了复现，并不表示采用上游最新版。

The original font inputs and generated subsets have pinned SHA-256 digests in
[font-manifest.json](font-manifest.json). The manifest records reproducible sources;
it contains no device backups or user history.
