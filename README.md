# 🦷 STS 2026: The 4th Semi-supervised Teeth Segmentation Challenge on Metal Artifact Reduction and Beyond

**MICCAI 2026, Strasbourg, France | September 27 - October 1, 2026**

[Challenge Website](https://nixy495.github.io/miccai2026/index.html) · [Winners & Final Results](https://nixy495.github.io/miccai2026/task1_winners.html) · [Codabench](https://www.codabench.org/)

---

## 📖 Table of Contents
- [Introduction](#-introduction)
- [Tasks](#-tasks)
- [Final Rankings](#-final-rankings)
- [Released Materials](#-released-materials)
- [Docker Submissions](#-docker-submissions)
- [Important Dates](#-important-dates)
- [Contact](#-contact)

---

## 📌 Introduction

Digital dentistry increasingly relies on cone-beam computed tomography (CBCT) and intraoral scans (IOS).
While CBCT provides root, bone and anatomical context, IOS captures high-resolution crown geometry.
In patients with fillings, crowns, bridges or implants, metal artifacts introduce streaking, shadowing and
blooming effects that obscure boundaries and reduce the reliability of automated dental analysis.

STS 2026 focuses on artifact-resilient dental AI under real-world conditions. Unlike earlier editions centered
on cleaner segmentation data, this challenge uses a multi-center dataset in which every case contains metallic
objects. Participants build semi-supervised pipelines that remain robust when metal artifacts affect both
anatomical segmentation and cross-modal IOS-CBCT alignment.

The challenge is organized around three tasks: metal-artifact CBCT teeth segmentation, CBCT-IOS registration,
and MMDental multimodal analysis.

> **Final ranking note.** The final ranking of each task is based on the official Docker test evaluation
> published on the Codabench competition page. The Codabench validation leaderboard is **not** used for the
> final ranking.

---

## 🏁 Tasks

| Task | Topic | Codabench |
|------|-------|-----------|
| Task 1 | Metal Artifact CBCT Teeth Segmentation | [competition 16027](https://www.codabench.org/competitions/16027/) |
| Task 2 | CBCT-IOS Registration | [competition 16042](https://www.codabench.org/competitions/16042/) |
| Task 3 | MMDental Multimodal Analysis | [competition 16117](https://www.codabench.org/competitions/16117/) |

---

## 📊 Final Rankings

Full leaderboards, metric definitions and per-team material links are on the challenge website:
[Task 1 winners](https://nixy495.github.io/miccai2026/task1_winners.html) ·
[Task 2 winners](https://nixy495.github.io/miccai2026/task2_winners.html) ·
[Task 3 winners](https://nixy495.github.io/miccai2026/task3_winners.html)

### Task 1 — Metal Artifact CBCT Teeth Segmentation

| Rank | Team | Report | Slides | Code |
|------|------|--------|--------|------|
| 1st | cccc2026 | - | [PDF](./TechnicalReport/task1/MICCAI-STS-2026-Challenge-Task1-Rank1-chengliangyu.pdf) | - |
| 2nd | thisxu | [PDF](./TechnicalReport/task1/16_CBCT_Tooth_and_Pulp_Segment.pdf) | - | [Zip](./code/Task1/2%20thisxu.zip) |
| 3rd | fy666 | [PDF](./TechnicalReport/task1/22_Global_to_Local_Tooth_and_P.pdf) | - | [Zip](./code/Task1/3%20fy666.zip) |
| 4th | JLShen025 | [PDF](./TechnicalReport/STSR2026_JLShen_report.pdf) | - | - |

### Task 2 — CBCT-IOS Registration

| Rank | Team | Report | Slides | Code |
|------|------|--------|--------|------|
| 1st | avalanchezy | [PDF](./TechnicalReport/task2/1_Registration_Teaches_Registr.pdf) | [PDF](./TechnicalReport/task2/MICCAI-STS-2026-Challenge-Task2-Rank2-Zhuyi.pdf) | [Zip](./code/Task2/1%20avalanchezy.zip) |
| 2nd | qingfeng | - | - | [Zip](./code/Task2/2%20qingfeng.zip) |
| 3rd | aimagelabzip | [PDF](./TechnicalReport/task2/4_Landmark_Guided_Coarse_to_Fi.pdf) | - | [GitHub](https://github.com/AImageLab-zip/L2L-Registration) |

### Task 3 — MMDental Multimodal Analysis

| Rank | Team | Report | Slides | Code |
|------|------|--------|--------|------|
| 1st | abc-abc | - | - | [Zip](./code/Task3/2%20abc-abc.zip) |
| 2nd | vinunivnu | [PDF](./TechnicalReport/task3/17_Entity_Constrained_CBCT_Ret.pdf) | - | [Zip](./code/Task3/3%20vinunivnu.zip) |
| 3rd | sjtu426lab-task3 | [PDF](./TechnicalReport/task3/21_Segmentation_Guided_3D_Dent.pdf) | [PDF](./TechnicalReport/task3/MICCAI-STS-2026-Challenge-Task3-Rank3-ChangkaiJi.pdf) | [GitHub](https://github.com/duola-wa/MICCAI-2026-STS-Task-3) |
| 4th | jlshen | [PDF](./TechnicalReport/STSR2026_JLShen_report.pdf) | - | - |

---

## 📂 Released Materials

```
STS-Challenge-2026/
├── code/                          # Participant-released code archives (one zip per team)
│   ├── README.md                  # Collection notes (team list, source repos, gaps)
│   ├── Task1/                     # 2 thisxu.zip, 3 fy666.zip, 6 djw.zip, 8 feelok.zip
│   ├── Task2/                     # 1 avalanchezy.zip, 2 qingfeng.zip
│   └── Task3/                     # 2 abc-abc.zip, 3 vinunivnu.zip, 4 feelok.zip
├── TechnicalReport/
│   ├── task1/                     # Team technical reports + winner presentation slides
│   ├── task2/
│   ├── task3/
│   └── STSR2026_JLShen_report.pdf # Report covering Tasks 1-3
└── DockerFromParticipants/
    └── baiduNetdisk.txt           # Download link for the Docker image archive
```

Notes:

- Materials are published as released by the participating teams. Reports and code are included only when
  the teams shared them.
- `code/README.md` records each team's code source repository, commit and known gaps (e.g. repositories that
  had been deleted or made private at collection time).
- Some validation-phase participants did not take part in the final Docker evaluation, so their reports are
  also archived here for completeness.
- scripts/ contains the helper scripts used to download the large Docker archive and to extract participant code
  from the OCI image layers.

---

## 🐳 Docker Submissions

The Docker images evaluated in the final test phase are multi-GB archives and are therefore **not** stored in
this Git repository. They are archived on Baidu Netdisk:

- **Baidu Netdisk:** <https://pan.baidu.com/s/560FWJwzDV24p48MSVig7GA> (see
  [`DockerFromParticipants/baiduNetdisk.txt`](./DockerFromParticipants/baiduNetdisk.txt))
- For `vinunivnu` (Task 3), the source snapshot extracted from the Docker image is available as
  `code/Task3/3 vinunivnu.zip`; the full image archive was shared at
  <https://drive.google.com/file/d/1xFapoEOu8BOPA6b9mE0qQ37X9KjOJbCv/view?usp=sharing>

---

## 🗓️ Important Dates

| Event | Date |
|-------|------|
| Registration opens / training and validation data release | May 11, 2026 |
| Docker submission portal opens | July 15, 2026 |
| Final submission deadline | August 1, 2026 |
| Results announcement | August 15, 2026 |
| MICCAI 2026 (Strasbourg, France) | September 27 - October 1, 2026 |

---

## 📧 Contact

For any inquiries, please contact <SemiTeethSegChallenge@outlook.com> or <zhi.li@hdu.edu.cn>.
We welcome questions, feedback and collaboration requests related to the STS 2026 challenge.

Copyright @ STS 2026 Challenge Organizers.
