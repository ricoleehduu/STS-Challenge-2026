# STS 2026 Challenge — 参赛队伍源代码（Participant Code）

本目录收集 STS 2026（MICCAI 2026）各参赛队伍公开的训练 / 推理源代码，目录结构与命名格式参照
[STS-Challenge-2024 / code](https://github.com/ricoleehduu/STS-Challenge-2024/tree/main/code)：
按赛道（`Task1` / `Task2` / `Task3`）分目录，每支队伍一个 zip（`<序号> <队伍名>.zip`）。

> - 文件名中的**序号为报名表顺序，不是最终排名**；官方最终排名公布后可整体替换为排名编号（对应 2024 仓库的 `1 choho tech.zip` 形式）。
> - 所有代码于 **2026-09-21** 从队伍公开仓库的默认分支 HEAD 抓取，对应的 commit 见下表。
> - zip 内为仓库根目录内容（已剔除 `.git/`、`__pycache__/`、`*.pyc` 等缓存），解压即可看到各队自己的 `README.md`。

## 目录结构

```
code/
├── README.md
├── Task1/
│   ├── 2 thisxu.zip
│   ├── 3 fy666.zip
│   ├── 6 djw.zip
│   └── 8 feelok.zip
├── Task2/
│   ├── 1 avalanchezy.zip
│   └── 2 qingfeng.zip
└── Task3/
    ├── 2 abc-abc.zip
    ├── 3 vinunivnu.zip          # 由原始提交的 3.1 GB Docker 镜像抽取，见下方说明
    └── 4 feelok.zip
```

## Task 1

| # | 队伍 | 代码来源 | 本地文件 | zip | commit |
| --- | --- | --- | --- | --- | --- |
| 2 | thisxu | [thisxu/TestMICCAI26](https://github.com/thisxu/TestMICCAI26) | `Task1/2 thisxu.zip` | 4.30 MB / 92 files | `b4c4cf7bdd0c` |
| 3 | fy666 | [LeguanFy/MICCAI-STSR-2026-Task1](https://github.com/LeguanFy/MICCAI-STSR-2026-Task1) | `Task1/3 fy666.zip` | 0.04 MB / 16 files | `99da1a5a2894` |
| 6 | djw | [EdmundJi/stsr2026-djw](https://github.com/EdmundJi/stsr2026-djw) | `Task1/6 djw.zip` | 0.37 MB / 117 files | `81ec4c42f6a4` |
| 8 | feelok | [Myselffe/AARU_STS-2026-challenge-Task1](https://github.com/Myselffe/AARU_STS-2026-challenge-Task1) | `Task1/8 feelok.zip` | 2.26 MB / 29 files | `96f02c7e7e3b` |

## Task 2

| # | 队伍 | 代码来源 | 本地文件 | zip | commit |
| --- | --- | --- | --- | --- | --- |
| 1 | avalanchezy | [avalanchezy/RegistrationTeachesRegistration](https://github.com/avalanchezy/RegistrationTeachesRegistration) | `Task2/1 avalanchezy.zip` | 2.70 MB / 151 files | `f0671fefcc14` |
| 2 | qingfeng | [qingfeng-dot/STSR2026](https://github.com/qingfeng-dot/STSR2026) | `Task2/2 qingfeng.zip` | 5.75 MB / 45 files | `92cbefa2f9b3` |

## Task 3

| # | 队伍 | 代码来源 | 本地文件 | zip | commit |
| --- | --- | --- | --- | --- | --- |
| 2 | abc-abc | [abc-w/stsr_task3_image_code](https://github.com/abc-w/stsr_task3_image_code) | `Task3/2 abc-abc.zip` | 0.04 MB / 23 files | `996a6c81c220` |
| 3 | vinunivnu | [Google Drive: vinunivnu.tar.gz](https://drive.google.com/file/d/1xFapoEOu8BOPA6b9mE0qQ37X9KjOJbCv/view?usp=sharing)（3.1 GB Docker 镜像，代码位于镜像内 `/opt/mmdental`） | `Task3/3 vinunivnu.zip` | 0.03 MB / 14 files | 源码 revision `4def33f0`（镜像内 SLSA 证明） |
| 4 | feelok | [Myselffe/GQ-TSR_STS-2026-Challenge-Task3](https://github.com/Myselffe/GQ-TSR_STS-2026-Challenge-Task3) | `Task3/4 feelok.zip` | 1.20 MB / 75 files | `934f69478270` |

## 抓取说明与已知缺口

| 队伍 | 赛道 | 状态 | 说明 |
| --- | --- | --- | --- |
| cccc2026 | Task 1 | ⚠️ 未能抓取 | 给定链接 `chenchenchenchencj/stsr2026-task1-nomirror-07599` 返回 404（仓库已删除或转为私有）。该账号下现有公开仓库为 `cccc`、`miccai2025`、`U-Mamba-CBCT-private` 等，均无法确认对应本次提交，需向队伍索要正确链接。 |
| JLShen025 | Task 1、Task 3 | ⚠️ 链接有误 | 给定链接指向 [jlshen025/codabench](https://github.com/jlshen025/codabench) 的 `stanceeval_t1` / `stanceeval_t2` 目录，内容为 **StanceEval-2026 / MoCha / UDIVA / SeaWinds** 等其它比赛的代码，与本挑战无关（全仓库检索无 tooth/teeth/STS 相关内容）。需要队伍提供真正的 STS 2026 代码链接。 |
| vinunivnu | Task 3 | 🐳 镜像形式提交（已抽取源码） | 原始提交为 3.1 GB 的 `vinunivnu.tar.gz`（OCI/Docker 镜像导出）。GitHub 单文件上限不足，故只把镜像中**参赛队自己的文件**抽取为 `Task3/3 vinunivnu.zip`：`mmdental/` 下 7 个文件（`run_task3.py`、`entrypoint.sh`、`config.py`、`eval_harness.py`、`med3dvlm_embed.py`、`retrieval_projection.py`、`max_accuracy_hybrid.py`）、`tmp/requirements-runtime.txt`，以及镜像的 OCI/SLSA 元数据（`index.json`/`manifest.json`/`image-config.json`/`provenance.json`）和一份 `SOURCE.md` 说明。镜像其余约 3.1 GB 是 `pytorch/pytorch:2.5.1-cuda12.1-cudnn9-runtime` 基础环境（CUDA + PyTorch + pip 依赖），未转存，完整镜像仍走上方 Google Drive 链接（与 2024 仓库 `DockerFromParticipants/docker.txt` 的做法一致）。 |
| vinunivnu（补充） | Task 3 | 🔎 源码仓库 | 从镜像内嵌的 SLSA provenance 可读出真正的源码仓库为 `https://github.com/NhiNguyen34/sts26-task3-mmdental.git`（revision `4def33f061f8c4ef293ee531ba77133fcfdee8d6`），截至 2026-09-21 该仓库不可公开访问（404），因此镜像抽取版是当前唯一可得的源码。 |
| 3dvmar | Task 1 | — 未提交 | 报名表中标注“未提交”。 |
| sjtu426lab | Task 1、Task 3 | — 未提交 | 报名表中标注“未提交”。 |
| my311 | Task 1 | — 未提交 | 报名表中标注“未提交”。 |
| aimagelabzip | Task 2 | — 未提交 | 报名表中标注“未提交”。 |

其它说明：

- **thisxu（Task 1）**：仓库用 Git LFS 管理 3 个 nnU-Net 权重（`checkpoint_final.pth`，各约 240 MB）。zip 内保留 LFS 指针文件（134 字节/个），需要权重时在原仓库执行 `git lfs pull`，本仓库不转存权重。
- **feelok** 同时在 Task 1（`AARU_STS-2026-challenge-Task1`）和 Task 3（`GQ-TSR_STS-2026-Challenge-Task3`）提交，因此出现在两个目录中（Task 3 中编号排在报名表 Task 3 队伍之后）。
- 所有 zip 均以 Python `zipfile`（UTF-8 文件名标志）打包，中文文件名可正常解压。

## 抓取脚本（`scripts/`）

为便于复核与重跑，本次抓取用的两个脚本保留在仓库中，可按需删除：

- `scripts/fetch_vinunivnu_gdrive.py`：分段并发、可断点续传地下载 vinunivnu 的 3.1 GB Google Drive 镜像（单连接约 0.3 MB/s，8 段并发约 1.1 MB/s）。
- `scripts/extract_oci_code.py`：流式扫描 OCI/Docker 镜像 tar.gz 的各个 layer（`blobs/sha256/*`），列出目录概况或按前缀抽取源码，自动跳过 conda/site-packages/apt 等基础环境与权重文件。
