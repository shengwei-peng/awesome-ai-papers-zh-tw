<div align="center">

# awesome-ai-papers-zh-tw

**Daily AI research papers — translated into Traditional Chinese (Taiwan)**

[![Papers](https://img.shields.io/badge/papers-1835-blue)](https://github.com/shengwei-peng/awesome-ai-papers-zh-tw/tree/main/papers)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![Last Updated](https://img.shields.io/github/last-commit/shengwei-peng/awesome-ai-papers-zh-tw?label=Last%20Updated&color=green)](https://github.com/shengwei-peng/awesome-ai-papers-zh-tw/commits/main)

[繁體中文](./README.zh-tw.md)

</div>

---

Reading AI research takes time. Keeping up with dozens of new papers every day is even harder when they are all in English.

This project automatically collects the latest AI research papers daily, translates and analyzes them, and publishes the results in Traditional Chinese. Every paper goes beyond raw translation — each one includes deep analysis, structured Q&A, and a practical guide to help you act on what you read.

---

## What Each Paper Contains

Papers appear in this order:

| # | Section | Description |
|---|---------|-------------|
| 1 | ⚡ **TL;DR** | 3-sentence summary — the core idea at a glance |
| 2 | 📝 **Abstract (ZH)** | Full translation with English terms in parentheses, plus key contributions and recommended audience |
| 3 | 🔬 **Deep Analysis** | Methodology · Experimental results · Comparison with prior work · Reproducibility · Future directions |
| 4 | 💬 **Q&A** | 15 questions covering background, method, experiments, applications, and limitations |
| 5 | 🛠️ **Practical Guide** | Use cases · Prerequisites · Implementation steps · Risks · Integration advice · Reading guide by audience |
| 6 | 📋 **Glossary** | English ↔ Traditional Chinese term mapping used consistently throughout the paper |

---

## Browse Papers

All papers are in the [`papers/`](./papers/) folder, prefixed with the arXiv ID:

```text
papers/
├── 2605.13757_FrameSkip_Learning_from_...md
├── 2605.09433_Offline_Preference_Optimization_...md
├── 2605.06527_STALE_Can_LLM_Agents_Know_...md
└── ...
```

**Find a specific paper:**

```bash
find papers/ -name "2605.13757_*"
```

**Search by keyword (Chinese or English):**

```bash
grep -rl "retrieval-augmented" papers/
grep -rl "檢索增強生成" papers/
```

**List the most recent papers:**

```bash
ls -lt papers/ | head -20
```

---

## License

Original papers © their respective authors. All rights reserved.

Translations and analysis in this repository are released under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE). You are free to share and adapt the content with proper attribution.

---

<div align="center">

If this saves you time, a ⭐ is appreciated.

</div>
