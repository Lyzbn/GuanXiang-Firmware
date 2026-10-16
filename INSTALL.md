# 观象 1.1.0 候选版安装

这是三档阅读候选版的安装说明。固定源码构建、CI 与离线升级检查已通过，新版尚未烧录验收；发行材料尚未公开。

适用设备：M5Stack Cardputer-ADV（ESP32-S3，8 MB Flash）。固件离线运行，不需要 microSD。

| 安装方式 | 文件 | 写入地址 | 现有历史和设置 |
| --- | --- | --- | --- |
| 首次安装／主动重装 | `GuanXiang-Cardputer-ADV-v1.1.0-candidate-Full.bin` | `0x0` | 会清除 NVS 中的历史和设置 |
| 从兼容观象版本升级 | `GuanXiang-Cardputer-ADV-v1.1.0-candidate-AppUpgrade.zip` | 应用 `0x10000` | 仅更新 app0，保留 NVS 字节；须通过分区及启动选择检查 |

先下载并核对 `SHA256SUMS`。Linux 用 `sha256sum -c SHA256SUMS`，macOS 用 `shasum -a 256 -c SHA256SUMS`。应用升级 zip 内另有自己的校验清单。

## 保留历史和设置的应用升级

此方式用于已有兼容观象安装：分区表为已验证的 `default_8MB.csv` 布局，从 app0 启动，历史和设置数据格式为版本 1。它不会把其他应用的记录转换成观象记录，也不能恢复已经损坏的数据。保留对你重要的记录，并保持供电稳定。

解压升级 zip，在该目录运行（将 `PORT` 换为设备端口，例如 Windows `COM5` 或 macOS `/dev/cu.usbmodem...`）：

```sh
python -m pip install esptool==4.11.0
python upgrade_app.py --port PORT --write
```

脚本先校验应用 SHA-256，再仅读取设备的分区表与 OTA 启动选择。两项都匹配才写应用；不会读取或归档 NVS。省略 `--write` 可仅检查兼容性。

若分区表或启动选择不匹配，脚本停止。不要通过擦除整片 Flash 绕过检查，也不要为了保留数据而改用 Full 镜像。应先确认原安装及启动分区。应用升级流程只有 `write_flash 0x10000`，没有 `erase_flash`，也不写 `0x0`、`0x8000`、`0xe000`。

当前应用大小 1,202,112 字节，实际写入 `0x10000..0x1357bf`；按 4 KB 扇区擦除的范围为 `0x10000..0x135fff`。NVS 位于 `0x9000..0xdfff`，在该范围之外。

## 首次安装或重装

Full 镜像包含 bootloader、分区表、启动选择和应用。它是构建产物组合，大小 1,267,648 字节；不是从任何用户设备读取的 8 MB 备份。

此方式会清除 NVS 历史和设置。M5Burner 导入该文件时使用地址 `0x0`；CLI 可运行：

```sh
python -m pip install esptool==4.11.0
python -m esptool --chip esp32s3 --port PORT --baud 115200 write_flash --flash_mode keep --flash_freq keep --flash_size keep 0x0 GuanXiang-Cardputer-ADV-v1.1.0-candidate-Full.bin
```

保留 DIO 启动头，不要改成 QIO。该文件在 `0x9000..0xdfff` 填充 `0xff`，写入必然清除该 NVS 区域。完整写入按扇区覆盖 `0x0..0x135fff`；它并不是整片 8 MB 擦除。

## 验收和来源

安装后确认能启动、旧历史及设置是否符合所选安装方式，并完成一卦、保存、重启后读取。本候选使用固定提交 CI 生成的应用字节，应用 SHA-256：

`6a694cd5e1bec230d249fa4298cd9568841b52689c28484f853b38075b2b06f3`

候选号为 `1.1.0-candidate`；这些字节编译自源码提交 `4d412daab3e4f18339637392813d51ea159af610`，源码版本元数据为 `1.1.0-dev`。详细摘要、依赖来源及兼容布局见 `PROVENANCE.json`。

新版尚未进行实机验收。升级脚本已通过 8 项离线检查；Full 合并文件的结构、摘要、应用偏移和 NVS 填充值已核对。旧版硬件验收记录只适用于旧版镜像，不能代替本候选的验收。

固件 ESP-IDF application descriptor 中的 `arduino-lib-builder`、SDK 版本与 2024 年日期来自预编译框架；它们不是观象发行版本或本轮构建时间。请用本发行的文件名、SHA-256 与来源清单识别版本。

## 三档阅读验收

首页 I 打开设置，T 在短意、精意、古文间循环，并保存默认档位。重新打开历史或开始新的一卦时应采用所选默认档位。阅读页 T 仅临时切换，从第一页开始，不改变默认档位。使用 ↑↓ 或 Enter 阅读完整内容；确认长文无缺字和截断，查看历史不增加记录。完成一次起卦后历史应只新增一条，USB 与电池冷启动后默认档位和历史应保留。
