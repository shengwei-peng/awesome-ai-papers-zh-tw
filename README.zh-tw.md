<div align="center">

# awesome-ai-papers-zh-tw

**每日最新 AI 研究論文 × 繁體中文深度翻譯**

[![Papers](https://img.shields.io/badge/papers-1810-blue)](https://github.com/shengwei-peng/awesome-ai-papers-zh-tw/tree/main/papers)
[![License: CC BY 4.0](https://img.shields.io/badge/授權-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![Last Updated](https://img.shields.io/github/last-commit/shengwei-peng/awesome-ai-papers-zh-tw?label=最後更新&color=green)](https://github.com/shengwei-peng/awesome-ai-papers-zh-tw/commits/main)

[English](./README.md)

</div>

---

閱讀 AI 研究論文需要時間。每天追蹤數十篇全英文新論文更是負擔。

本專案每天自動收集最新 AI 研究論文，翻譯並分析後以繁體中文（台灣用語）整理發佈。每篇論文不只是翻譯——還包含深度分析、結構化問答與實務應用指南，幫助你真正讀懂並應用所學。

---

## 每篇論文包含

論文內容依以下順序排列：

| # | 區塊 | 說明 |
|---|------|------|
| 1 | ⚡ **TL;DR** | 三句話快速掌握論文核心 |
| 2 | 📝 **摘要翻譯** | 忠實全文翻譯，術語保留英文並括號標注，附核心貢獻與適合讀者說明 |
| 3 | 🔬 **深度分析** | 方法論解析 · 實驗數據解讀 · 與現有研究比較 · 可重現性評估 · 未來研究方向 |
| 4 | 💬 **論文問答** | 15 個深度問答，涵蓋背景、方法、實驗、應用與局限性 |
| 5 | 🛠️ **實務應用指南** | 適用場景 · 前置條件 · 實作步驟 · 潛在風險 · 整合建議 · 各背景讀者閱讀建議 |
| 6 | 📋 **術語對照表** | 全篇統一使用的英文 ↔ 繁體中文術語對照 |

---

## 瀏覽論文

所有論文位於 [`papers/`](./papers/) 資料夾，以 arXiv ID 為前綴命名：

```text
papers/
├── 2605.13757_FrameSkip_Learning_from_...md
├── 2605.09433_Offline_Preference_Optimization_...md
├── 2605.06527_STALE_Can_LLM_Agents_Know_...md
└── ...
```

**尋找特定論文：**

```bash
find papers/ -name "2605.13757_*"
```

**以關鍵字搜尋（中文或英文皆可）：**

```bash
grep -rl "retrieval-augmented" papers/
grep -rl "檢索增強生成" papers/
```

**查看最新發佈的論文：**

```bash
ls -lt papers/ | head -20
```

---

## 授權

論文版權歸原作者所有，保留所有權利。

本專案的翻譯與分析內容以 [Creative Commons 姓名標示 4.0 國際授權（CC BY 4.0）](LICENSE) 釋出，歡迎在標注來源的前提下自由分享與改作。

---

<div align="center">

如果這個專案節省了你的時間，歡迎按 ⭐ 支持！

</div>
