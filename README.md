# ACC424-Accounting-Information-System_Python

# ACC424 Accounting Information System (Python)

This repository contains full Python lecture notes and code examples for **ACC424 Accounting Information System**, Spring 2025. The focus is on applying Python programming for auditing, financial analysis, internal controls testing, and AI-enhanced accounting procedures.

---

## 📚 Table of Contents
1. [Benford’s Law Analysis (Module 2.1–2.3)](#benfords-law-analysis-module-21–23)
2. [Accounts Receivable Aging (Module 3.1–3.3)](#accounts-receivable-aging-module-31–33)
3. [Financial Statement Analysis with AI (Module 4.1–4.4)](#financial-statement-analysis-with-ai-module-41–44)
4. [Auditing with Prompt Engineering (Module 5.1–5.4)](#auditing-with-prompt-engineering-module-51–54)
5. [Automating Internal Controls Testing (Module 6.1–6.4)](#automating-internal-controls-testing-module-61–64)
6. [Source Files](#source-files)

---

## Benford’s Law Analysis (Module 2.1–2.3)
Benford’s Law describes the frequency distribution of leading digits in naturally occurring datasets. It’s widely used in fraud detection.

Key Concepts:
- First-digit distribution should follow a logarithmic pattern.
- Auditors flag anomalies when actual vs. expected frequencies differ.

Code Highlights:
- Extract first digits from values
- Count digit frequencies
- Compare with Benford’s expected distribution
- Identify significant deviations (e.g., difference > 0.05)

🔗 [Benford Notebook Link](https://anaconda.cloud/share/notebooks/ed1b63e8-c936-4fa7-b83a-a08400b2f986/overview)

---

## Accounts Receivable Aging (Module 3.1–3.3)
Analyzes overdue invoices using time buckets:
- Current
- 1–30 days
- 31–60 days
- 61–90 days
- Over 90 days

Metrics:
- % receivables in each bucket
- Average collection period
- Estimated bad debt using bucket-based risk weights

Code Features:
- Class-based structure with Pandas and datetime
- Bucket assignment and visualization (pie and bar charts)

🔗 [AR Aging Notebook Link](https://anaconda.cloud/share/notebooks/e73bd848-9f05-4f59-98f1-eee23297ea5f/overview)

---

## Financial Statement Analysis with AI (Module 4.1–4.4)
Combines traditional ratio analysis with AI-enhanced Python visualizations:
- Ratios: Gross Profit Margin, Net Profit Margin, Current Ratio, ROE
- Tools: pandas, seaborn, plotly, sklearn
- Interactive dashboards for better communication of insights

AI Uses:
- Automated data processing
- Interactive trend analysis
- Forecasting future ratios (linear regression)

🔗 [Financial Visualization Notebook](https://anaconda.cloud/share/notebooks/05f70fbd-ef5c-4aee-80bb-fde64484c485/overview)

---

## Auditing with Prompt Engineering (Module 5.1–5.4)
Use LLMs like ChatGPT or DeepSeek to:
- Detect data issues (missing, duplicates, outliers, bad formats)
- Auto-generate Python audit code from natural-language prompts
- Debug Python code with AI assistance

Prompt examples:
- “Find missing customer names”
- “Detect duplicates in Transaction ID”
- “Flag values not in YYYY-MM-DD format”

🔗 [Prompt Engineering Notebook](https://anaconda.cloud/share/notebooks/bfbbbb2d-00f9-45c7-825c-fcaf1357f0ad/overview)

---

## Automating Internal Controls Testing (Module 6.1–6.4)
Covers how to automate:
- Data validation
- Transaction limit checks
- Segregation of duties
- Master data change tracking

Framework:
- Define rules (e.g., max amounts, role conflicts)
- Apply rules to full data population
- Output violations and audit trail logs

Benefits:
- 100% testing coverage
- Real-time flagging of control failures
- Traceable, structured audit documentation

---

## Source Files
- `Python notes all.pdf` (full lecture notes)
- All coding notebooks available via Anaconda links above

🧠 For any questions, refer to lecture notes or reach out during MW class sessions.

---

> ✨ This README is auto-generated using prompt engineering and code snippets from in-class Python notebooks.



