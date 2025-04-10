# ACC424-Accounting-Information-System_Python

This repository contains full Python lecture notes and code examples for **ACC424 Accounting Information System**, Spring 2025. The course focuses on applying Python in AIS for auditing, financial analysis, automated internal controls testing, AI-enhanced accounting procedures, predictive analytics, and business intelligence. No prior coding experience is required.


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

🔗 [Automating Internal Controls Testing Notebook](https://nb.anaconda.cloud/jupyterhub/user/976e55b1-05fb-4288-8798-8a416ead9118/lab/workspaces/auto-d/tree/anaconda_projects/Automating%20Internal%20Controls%20Testing.ipynb?)
  
---

## Predictive Analytics for Financial Forecasting and BI (Module 7.1–7.5)
Covers how to build predictive models for forward-looking business intelligence using financial transaction data.

Forecasting Targets:

- Revenue growth
- Operating expenses
- Net income and ROA trends

Techniques:

- Feature engineering with lagged values and moving averages
- Linear and polynomial regression
- Time series decomposition (trend, seasonality, residual)

Framework:

- Load historical financial data
- Transform into supervised learning format
- Fit predictive models and evaluate accuracy (e.g., MAE, RMSE)
- Visualize forecasted vs. actuals using matplotlib or plotly

Benefits:

- Data-driven budgeting and planning
- Scenario modeling and what-if analysis
- Enhanced decision support for CFOs and controllers

🔗 [Forecasting & BI Notebook](https://nb.anaconda.cloud/jupyterhub/user/976e55b1-05fb-4288-8798-8a416ead9118/lab/workspaces/auto-d/tree/anaconda_projects/Predictive%20analytics%20and%20business%20intelligence%20applications.ipynb?)

## Source Files
- All Python notes are provided as PDF files:
  - `Python 2_Benford’s Law Analysis_2.1–2.3`
  - `Python 3_Accounts Receivable Aging Analysis and Visualization_3.1–3.3`
  - `Python 4_Financial Statement Analysis with AI-Assisted Data Visualization_4.1–4.4`
  - `Python 5_Auditing data sets with prompt engineering_5.1–5.4`
  - `Python 6_Automating internal controls testing_6.1–6.3`
  - `Python 6_Automating internal controls testing_6.4`
  - `Python 7_Predictive analytics for financial forecasting and business intelligence_7.1–7.2`
  - `Python 7_Predictive analytics for financial forecasting and business intelligence_7.3–7.5`
- All coding scripts are aggregated in:
  - `ACC424 Python code all.py`
- All interactive coding notebooks are linked above via Anaconda Cloud

🧠 If you have any questions about the Python notes or encounter any coding difficulties, I am here to help you and are available to meet you in person during office hours:
- 🕓 **Office Hours**: 2:30 PM – 3:45 PM on Mondays and Wednesdays
- 📍 **Location**: 435J Gatton B&E

For quick questions, feel free to reach out via my email zju222@uky.edu. For more complex or hands-on questions, visiting during office hours will be more effective.


---







