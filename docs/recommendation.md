# Recommendation Summary

## Reframed Problem
Leadership asked for a quick churn prediction model focused on a recent price increase.  
The more useful question became: **Why did churn increase, which drivers are strongest and actionable, and what should we do next?**

## Key Findings
- Low monthly usage is a much stronger signal than the price-increase flag.
- The combination of a recent UI change + low usage shows elevated risk.
- Price has a real but secondary and concentrated effect.
- High support volume and very new customers also contribute.
- Data quality issues (e.g., missing support records) exist.

## Recommended Actions
1. Investigate the impact of the UI/product change on lower-usage customers.
2. Run a small experiment (usage prompts or improved onboarding) on the high-risk segment.
3. Use a transparent risk score for near-term targeting.
4. Treat price as a secondary factor unless further evidence appears.
5. Improve completeness of support and usage data.

## Delivered Solution
- Live Streamlit app that supports:
  - Synthetic demo data
  - CSV upload
  - Direct database connection (PostgreSQL, MySQL, SQLite)
- Transparent risk score
- Interpretable Logistic Regression baseline
- Full background documentation of the critical-thinking process

*Based on synthetic data designed to illustrate the critical-thinking approach.*
