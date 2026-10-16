# 第三方软件与资源声明

观象 1.1.0 未发布候选的第三方声明，核对日期：2026-10-16。本说明覆盖固件和配套重链接材料中实际提供的第三方库、SDK 文件及资源；某个库随 SDK 提供，不表示其全部功能进入最终固件。配套重链包使用与候选固件对应的 Linux CI 材料；对象和验证结果由包内清单记录。

第三方组件保留各自许可。观象的[固件许可](LICENSE-FIRMWARE.md)不限制这些组件原有的权利。下表是阅读索引，完整版权、许可条款和逐文件声明见 [licenses/third-party](licenses/third-party/)；该目录的 `SHA256SUMS` 可检查材料完整性。原始声明保持原文，来源 JSON 仅将本地准备目录改为相对路径。

## Arduino 与设备库

| 组件及版本 | 适用文件或材料 | 许可与署名材料 |
| --- | --- | --- |
| Arduino-ESP32 2.0.17；PlatformIO framework `3.20017.241212+sha.dcc1105b` | Arduino core、SPI、Wire 及提供的源码；`libFrameworkArduino.a`、`libSPI.a`、`libWire.a` | LGPL-2.1-or-later；Arduino、Espressif 及各文件作者。见 [LGPL 全文](licenses/third-party/LGPL-2.1.txt)和 [Arduino 文件声明](licenses/third-party/extracted-notices/ARDUINO_SOURCE_NOTICES.txt)，其中 libb64 另见[原声明](licenses/third-party/libb64-LICENSE.txt)。 |
| M5Cardputer 1.2.0 | `libM5Cardputer.a` | M5Stack Technology CO LTD；[MIT](licenses/third-party/M5Cardputer-MIT.txt)。 |
| M5Unified 0.2.18 | `libM5Unified*.a` | M5Stack；[MIT](licenses/third-party/M5Unified-MIT.txt)和[文件声明](licenses/third-party/extracted-notices/M5UNIFIED_SOURCE_NOTICES.txt)。 |
| M5GFX 0.2.25 | `libM5GFX*.a` | M5Stack；[MIT](licenses/third-party/M5GFX-MIT.txt)。其字体、解码器等文件另有声明，见 [M5GFX 文件声明](licenses/third-party/extracted-notices/M5GFX_SOURCE_NOTICES.txt)。Adafruit GFX 字体见 [BSD 全文](licenses/third-party/vendor-fonts/Adafruit-GFXFF-BSD.txt)，Tom Thumb 的 BSD 声明也保留于文件声明中。 |
| IRremote 4.7.1 | 构建配置依赖；当前重链包无单独 IRremote archive | [MIT 与原版权](licenses/third-party/IRremote-MIT.txt)保留作依赖出处，不将它计为已确认链接的独立库。 |

Arduino 的配套材料采用随包提供所需材料的方式：对应库源码、构建配方、可重链应用对象和操作说明一并提供。接收者可修改这些库并重新编译、链接；个人修改以及为调试这些修改而进行的逆向工程权限见固件许可。不以源码仓库链接代替这套材料，也不设置由维护者日后供给材料的多年承诺。

## ESP32-S3 SDK

SDK 的 ESP-IDF 基线为 `v4.4.7`，主仓提交 `38eeba213aa695aabfd6d89aa9f5078dbe5a94c3`。通用 Espressif 代码采用 [Apache 2.0](licenses/third-party/esp-idf-4.4.7/LICENSE)，具体文件另有许可的，以该文件声明为准。这里没有将整个 SDK 归为单一许可。

以下路径均相对于重链包 `framework/tools/sdk/esp32s3/`。原始头文件及链接脚本中的声明保留在包内；为便于随固件一起阅读，另集中保存 [SDK 原始版权与许可块](licenses/third-party/extracted-notices/SDK_SOURCE_NOTICES.txt)。

| 组件或 archive | 许可及完整声明 |
| --- | --- |
| FreeRTOS：各构建目录下 `libfreertos.a` | [MIT](licenses/third-party/esp-idf-4.4.7/components/freertos/LICENSE.md)；Amazon、Cadence 及移植文件的版权见 SDK 文件声明。 |
| newlib 的 SDK 适配代码：`libnewlib.a`、`include/newlib/` | Espressif Apache 代码及 [newlib 多作者条款](licenses/third-party/esp-idf-4.4.7/components/newlib/COPYING.NEWLIB)。工具链独立 libc/libm 见后文外部依赖范围。 |
| lwIP：`liblwip.a` | Swedish Institute of Computer Science 等；[BSD 与原文件声明](licenses/third-party/submodules/lwip/COPYING)。 |
| Mbed TLS：`libmbedtls*.a`、`libmbedcrypto.a`、`libmbedx509.a` | ARM、Mbed TLS 作者等；[Apache 2.0](licenses/third-party/submodules/mbedtls/LICENSE)。 |
| wpa_supplicant：`libwpa_supplicant.a` | Jouni Malinen 等；[BSD 及原组件声明](licenses/third-party/esp-idf-4.4.7/components/wpa_supplicant/COPYING)。 |
| Asio：`libasio.a` | Christopher M. Kohlhoff；[Boost Software License 1.0](licenses/third-party/submodules/asio/asio/LICENSE_1_0.txt)，另保留 [COPYING](licenses/third-party/submodules/asio/asio/COPYING)。 |
| libcoap：`libcoap.a` | Olaf Bergmann 等；[BSD 2-Clause 及文件所列条款](licenses/third-party/submodules/libcoap/LICENSE)，保留 uthash/utlist 文件声明。 |
| libsodium：`liblibsodium.a` | Frank Denis 等；[ISC](licenses/third-party/submodules/libsodium/LICENSE)。 |
| Expat：`libexpat.a` | Expat 作者；[MIT](licenses/third-party/submodules/expat/COPYING)。 |
| TinyCBOR：`libcbor.a` | Intel Corporation；[MIT](licenses/third-party/submodules/tinycbor/LICENSE)。许可取自 IDF 固定 gitlink；本地只有包装头，未据此声称独立重现 archive 的源码提交。 |
| nghttp2：`libnghttp.a` | Tatsuhiro Tsujikawa 及贡献者；[MIT 全文](licenses/third-party/esp-idf-4.4.7/components/nghttp/COPYING)。 |
| protobuf-c：`libprotobuf-c.a` | Dave Benson 及 protobuf-c 作者；[BSD 2-Clause](licenses/third-party/submodules/protobuf-c/LICENSE)。 |
| cJSON、JSMN：`libjson.a`、`libjsmn.a` | Dave Gamble、cJSON 贡献者与 Serge A. Zaitsev；[cJSON MIT](licenses/third-party/submodules/cjson/LICENSE)及 SDK 文件声明内的 JSMN MIT 全文。 |
| SPIFFS：`libspiffs.a` | Peter Andersson；[MIT](licenses/third-party/submodules/spiffs/LICENSE)。 |
| FatFs：`libfatfs.a` | ChaN；`include/fatfs/src/ff.h` 的原许可全文保留于 SDK 文件声明。 |
| TLSF：`libheap.a` 中的实现 | Matthew Conte；[BSD 3-Clause 原声明](licenses/third-party/tlsf/TLSF-BSD-3-Clause-NOTICE.txt)。Espressif heap 包装层另有 Apache 声明。 |
| LittleFS：`libesp_littlefs.a` | `esp_littlefs` 1.14.1 / 提交 `41873c20…` 的 [MIT](licenses/third-party/littlefs/esp_littlefs-MIT-LICENSE.txt)；其固定 littlefs `f53a0cc9…` 的 [BSD 3-Clause](licenses/third-party/littlefs/littlefs-BSD-3-Clause-LICENSE.md)。 |
| FreeModbus：`libfreemodbus.a` | Christian Walter、Armink、Espressif 等；保留 [23 份有差异的原 BSD 声明](licenses/third-party/freemodbus/)，以及 [IDF 包装层许可](licenses/third-party/esp-idf-4.4.7/components/freemodbus/LICENSE)。 |
| Unity、CMock：`libunity.a`、`libcmock.a` | Mike Karlesky、Mark VanderVoord、Greg Williams；[Unity MIT](licenses/third-party/submodules/unity/docs/license.txt)、[CMock MIT](licenses/third-party/submodules/cmock/LICENSE.txt)。 |
| Console 的 argtable3、linenoise | [argtable3 原条款](licenses/third-party/esp-idf-4.4.7/components/console/argtable3/LICENSE)、[linenoise BSD](licenses/third-party/esp-idf-4.4.7/components/console/linenoise/LICENSE)。 |
| SDMMC、UBSan、QR Code 实现 | 分别保留 [SDMMC 原声明](licenses/third-party/extracted-notices/SDMMC_SOURCE_NOTICES.txt)、[UBSan 原声明](licenses/third-party/extracted-notices/UBSAN_SOURCE_NOTICES.txt)、[QR Code MIT](licenses/third-party/extracted-notices/QRCODE_SOURCE_NOTICES.txt)；包装层不替代其底层声明。 |
| Xtensa/Cadence 支持代码；SDK Bluetooth 主机代码 | Cadence MIT、Espressif/其他作者的 Apache/BSD 等原文件声明均保留在 SDK 文件声明及对应头文件中。 |
| Espressif Wi-Fi：`libcore/libcoexist/libespnow/libmesh/libnet80211/libpp/libsmartconfig/libwapi.a` | 固定上游提交的 [Apache 2.0](licenses/third-party/submodules/esp32-wifi-lib/LICENSE)；8 个实际 archive 已与该提交逐字节核对。 |
| Espressif PHY：`ld/libphy.a`、`ld/libbtbb.a`；Bluetooth 控制器：`ld/libbtdm_app.a` | [PHY Apache 2.0](licenses/third-party/submodules/esp-phy-lib/LICENSE)、[BT Apache 2.0](licenses/third-party/submodules/esp32-bt-lib/LICENSE)；所列 archive 已与各固定提交逐字节核对。 |
| ESP-DL：`ld/{libdl,libmfn,libcat_face_detect,libhuman_face_detect,libcolor_detect}.a` | Espressif Systems；固定 `0632d244…` 的 [MIT](licenses/third-party/submodules/esp-dl/LICENSE)。 |
| ESP32 Camera / FB GFX、ESP RainMaker、ESP-DSP | SDK 更新记录中固定 `f0bb4291…`、`d8e93454…`、`9b4a8b42…`；分别见 [Camera](licenses/third-party/submodules/esp32-camera/LICENSE)、[RainMaker](licenses/third-party/submodules/esp-rainmaker/LICENSE)、[DSP](licenses/third-party/submodules/esp-dsp/LICENSE)。保留源内单独版权与许可声明，包括 Camera 的 OpenMV 来源声明。 |
| Arduino TinyUSB：`libarduino_tinyusb.a` | 固定 `a0e5626b…` 的 [MIT](licenses/third-party/submodules/tinyusb/LICENSE)，保留其文件内及附属组件声明。 |
| ESP-MQTT 及其余 Espressif SDK 包装/功能组件 | [ESP-MQTT Apache 2.0](licenses/third-party/submodules/esp-mqtt/LICENSE)及 SDK 主仓 Apache 2.0；各文件版权与例外见 SDK 文件声明。 |

来源与版本证据见[补充映射](licenses/third-party/SUPPLEMENT_SOURCE_MAP.md)及同目录 `SUPPLEMENT_SOURCE_ORIGINS_*.json`。IDF gitlink、Arduino 官方 [SDK 更新 PR #9339](https://github.com/espressif/arduino-esp32/pull/9339)、头文件/二进制逐字节核对分别记录，匹配若只覆盖头文件，不扩大为整个库已可重现。

## 字体和阅读文字

应用所用 GNU Unifont 17.0.04、Noto Serif CJK SC Black、efont 的来源与许可见 [FONT_SOURCES.md](FONT_SOURCES.md)。古文来源与现代整理文字见 [TEXT_SOURCES.md](TEXT_SOURCES.md)。

当前 `ae85426` 配套重链包已从 M5GFX archive 删除未使用的 `lgfx_font_japan.c.o`（IPA 衍生日文字体），成员数由 59 变为 58，其余成员顺序保持不变。删除前后使用原始 CI 应用对象重链，固件均逐字节等于候选应用摘要 `57e9dd2d6238164209ce90b4fc03c7b92e6c33df8f383d3b3cbba28dfb087f5e`。因此该日文字体成员不随包分发；[IPA 原许可](licenses/third-party/vendor-fonts/IPA_Font_License_Agreement_v1.0.txt)仅作为裁剪来源记录保留。其他 GFXFF、efont 成员及相应声明仍保留。新候选完整来源、18 个去调试应用对象及修改框架重建的验证见 [RELINK_VALIDATION.json](RELINK_VALIDATION.json)；去调试后的重链产物有 65 个摘要／校验字段字节变化，不与安装镜像摘要混用。

## 外部工具链

公开重链包不分发 GCC 工具链，也不单独提供其 `libgcc.a`、`libstdc++.a`、`libsupc++.a` 或工具链 `libc.a/libm.a/libnosys.a`。接收者按重链包说明安装官方 Linux 包 `espressif/toolchain-xtensa-esp32s3@8.4.0+2021r2-patch5` 和实际 CI 使用的 `platformio/tool-esptoolpy@2.41100.260830`（内部 esptool 4.11.0）。工具包本身的许可由其官方发行提供。

已核对的 [Linux x86_64 工具链官方归档](https://dl.registry.platformio.org/download/espressif/tool/toolchain-xtensa-esp32s3/8.4.0+2021r2-patch5/toolchain-xtensa-esp32s3-linux_x86_64-8.4.0+2021r2-patch5.tar.gz)大小为 67,385,729 字节，SHA-256 为 `6618e8a91fca47da09c840a61bf008b1f06698553389c01c8788e595d8e84da9`，其 1,737 个文件与实际 CI 导出逐字节一致。完整安装与验证信息见重链包的 `README.md`、`TOOLCHAIN_PACKAGE.json`；esptool 的实际归档信息也应以包内核对记录为准。

工具链的 [GCC Runtime Library Exception 3.1](licenses/third-party/toolchain-reference/gcc/COPYING.RUNTIME)、[GPL 3](licenses/third-party/toolchain-reference/gcc/COPYING3)、相关 LGPL 文本和 [newlib](licenses/third-party/toolchain-reference/newlib/COPYING.NEWLIB) / [libgloss](licenses/third-party/toolchain-reference/newlib/COPYING.LIBGLOSS) 声明作为参考原文保留。Runtime Exception 对符合条件的编译所产生的合并目标代码作出规定；这里不将它解释为可省略独立运行库发行材料的通用许可。esptool 是外部构建/烧录工具，其许可不作为固件整体的许可。

## 随包材料

本说明与 `licenses/third-party/` 应随候选发行资产一起提供；`SHA256SUMS` 校验许可材料，重链包自身的清单与 `VALIDATION.json` 校验构建输入及结果。硬件验收和发布状态由项目维护记录说明，不由许可材料的准备状态代替。
