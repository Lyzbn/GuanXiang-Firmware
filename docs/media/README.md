# 展示素材 / Presentation media

这组素材对应观象 `v1.1.0-rc.1`（应用提交 `ae85426`）。图片直接复用 2026-10-17 已确认的设备演示封面与原生 UI 素材，未改动屏幕内容。

- `device-overview.png`：B07 设备演示封面，1200 × 675；设备和场景是效果示意，屏幕叠加下列固件界面。不是设备实拍。
- `device-portrait.png`：B04 设备演示竖版，1080 × 1440；窄屏使用，设备、场景和屏幕来源与上项相同。
- `jiji-native.png`、`qian-native.png`：既济、乾的大字卦象卡，240 × 135。
- `42-coin-rise-native.png`、`43-coin-apex-native.png`、`48-coin-settled-native.png`：三币起腾、腾落、落定的三个示例瞬间，240 × 135；示例使用合法的固定飞行参数，不是用户起卦记录。

界面按对应固件源码、嵌入字模和 M5GFX 0.2.25 栅格规则重绘，不是设备 framebuffer 截屏。原制作核验已对照 33 个原生字形及三币画面的 84 条绘图命令；实际 LCD 的亮度、反光及动画时序可能不同。图片是静态示例，未模拟交互。

本目录不包含私有应用源码、构建对象或设备数据。逐图摘要见 [manifest.json](manifest.json)。字体来源与单独适用的许可见 [FONT_SOURCES.md](../../FONT_SOURCES.md)。

The device scene is an illustration, not a hardware photograph. The five 240 × 135 UI images were rendered from the matching firmware source and embedded bitmap fonts. They are not captured hardware framebuffers. Coin frames use deterministic example motion, not a user's cast. The images are unchanged copies of the previously reviewed presentation assets; file hashes are recorded in the manifest.
