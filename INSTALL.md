# 观象 v1.1.0-rc.2 预发行安装

本版修复「入门 → 03 读六十四卦」目录跨页：左右键每次翻一页（4 卦），可连续访问全部 16 页；首尾循环不再跳过 61–64 卦，打开第 64 卦后返回仍保留所在页。修复提交为 `96057ad3627ad6f43f429ebddca6d1dadd72d48b`。

仅适用于 M5Stack Cardputer ADV（ESP32-S3，8 MB Flash）。公开版本号为 **v1.1.0-rc.2**；为原样发布已经实机验收的 CI 二进制，固件内部源码版本仍显示 `1.1.0-dev`。以文件名、摘要和 `PROVENANCE.json` 识别本次修复版。

安装前下载[本次预发行材料](https://github.com/Lyzbn/GuanXiang-Firmware/releases/tag/v1.1.0-rc.2)，核对发行页 `SHA256SUMS`；解压升级包后，再核对包内独立的 `SHA256SUMS`。macOS/Linux 可运行 `shasum -a 256 -c SHA256SUMS`（或 Linux 的 `sha256sum -c SHA256SUMS`）。

## 保留历史和设置：应用升级

适用于分区布局和 app0 启动选择均符合检查的既有观象安装。先保留重要记录，连接稳定的 USB 电源；本工具不转换其他固件的数据，也不自动备份 NVS。

解压 `GuanXiang-Cardputer-ADV-v1.1.0-rc.2-AppUpgrade.zip`，进入解压目录，把 `PORT` 替换为实际端口，然后运行：

```sh
python -m pip install esptool==4.11.0
python upgrade_app.py --port PORT --write
```

省略 `--write` 只检查。升级器先校验应用摘要，再读取分区表与 OTA 启动选择；这两次读取不包含 NVS。任一检查不符即停止；不要擦除 Flash 绕过检查。

唯一写入地址是 app0 的 `0x10000`。应用长 **1,567,664 字节**，实际字节范围 `0x10000..0x18ebaf`，Flash 扇区范围 `0x10000..0x18efff`。NVS 位于 `0x9000..0xdfff`，不在写入范围内；应用升级也不写启动程序、分区表或 OTA 元数据。

如果升级器提示分区或启动选择不符，应先确认当前安装和备份情况；不要改用完整镜像来尝试保留旧数据。

## 首次安装或主动重装：完整镜像

`GuanXiang-Cardputer-ADV-v1.1.0-rc.2-Full.bin` 是 **1,633,200 字节**的 CI 合并固件，原样取自本版构建产物，**不是设备备份**。

**完整镜像写入 `0x0` 会清除 NVS 中的历史和设置。** 需要保留记录且检查兼容的既有观象用户应使用上方 AppUpgrade。M5Burner 提供的是完整镜像，具有相同的数据影响。

```sh
python -m pip install esptool==4.11.0
python -m esptool --chip esp32s3 --port PORT --baud 115200 write_flash --flash_mode keep --flash_freq keep --flash_size keep 0x0 GuanXiang-Cardputer-ADV-v1.1.0-rc.2-Full.bin
```

保留镜像已有的 DIO 启动头，不改为 QIO。完整镜像中的 NVS 区全部填充为 `0xff`；其写入扇区范围为 `0x0..0x18efff`，不是整片 8 MB Flash 擦除。

## 本版识别与验收

| 镜像 | SHA-256 |
| --- | --- |
| App（解压后的应用） | `44dd57a8d659d0097c00e48154155ce8d289ef2272c89fbe6df7feaf48239ec5` |
| Full（完整安装） | `81f8cea104067171cf768409fd686dd82cb8b3f359d0f95c6aa8ef109e472069` |

上述摘要不是 ZIP 归档摘要。CI run `40195260690` 的检出提交 `fd68d2017fbc170a3f683679d279a2a282080ee4` 与修复提交、最终合并提交具有相同源码树。预编译框架描述符日期不代表本次应用构建日期。

本版已完成应用写入校验、NVS 保持检查、20 秒启动烟测和以下用户实机验收：正常进入观象、旧历史与设置保留、按 `←`：`1–4 → 61–64 → 57–60`；按 `→`：`57–60 → 61–64 → 1–4`、打开第 64 卦返回仍在 61–64 页。

安装后可按上述顺序复核目录。完整起卦、USB／电池冷启动及长期运行未在本版重复验收；旧版相关结果不作为本版新增验收。详细范围见 [VALIDATION.md](VALIDATION.md)，可重链接材料见同一发行版的 `GuanXiang-Cardputer-ADV-v1.1.0-rc.2-Relink.zip`。
