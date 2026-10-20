# Executive Brief  
**Critical Thinking Applied to Customer Churn**  
**Project Owner:** Rajarao Gurindapalli  
**Date:** October 2026  
**Status:** Complete – Live App + Documentation + RAG Component

---

## 1. Business Context
Leadership observed monthly churn rising from approximately 4% to 7% and requested a churn prediction model within a short timeframe, with the working assumption that a recent price increase was the primary driver.

## 2. Approach Taken
Rather than immediately building a complex model, the engagement applied structured critical thinking:
- Reframed the problem from “build a model” to “diagnose drivers and recommend next actions under time pressure.”
- Evaluated multiple hypotheses using base rates and segment analysis.
- Preferred transparent, interpretable outputs over black-box solutions.
- Documented uncertainty and recommended small, testable next steps.

## 3. Key Findings
- Low monthly usage (especially combined with a recent UI change) showed a stronger signal than the price-increase flag.
- Price had a real but secondary and concentrated effect.
- Data quality issues (e.g., incomplete support records) were identified.
- No single causal story was fully supported by the available evidence.

## 4. Deliverables
| Deliverable | Location | Purpose |
|-------------|----------|---------|
| Live interactive application | [Streamlit App](https://churn-critical-thinking-9hcutmuurluprsw36jqqz2.streamlit.app/) | Demonstrates analysis and accepts user data (CSV or database) |
| Source repository | [GitHub](https://github.com/rajaraogurindapalli-gif/Churn-Critical-Thinking) | Full code, documentation, and notebooks |
| Background documentation | `/docs` | Problem definition, scope, critical-thinking path, recommendations |
| RAG notebook | `/notebooks` | Grounded qualitative analysis using internal evidence |
| Limitations & lessons | [docs/12_LIMITATIONS_AND_LESSONS.md](12_LIMITATIONS_AND_LESSONS.md) | Transparency on boundaries and learning outcomes |

## 5. Recommended Next Actions (for a real organisation)
1. Investigate the impact of the recent UI/product change on lower-usage customers.
2. Run a small controlled experiment (usage prompts or improved onboarding) on the highest-risk segment.
3. Use a transparent risk score for near-term targeting while further evidence is gathered.
4. Improve completeness of support and usage data.

## 6. Professional Notes
- All quantitative results in the demo are based on synthetic data designed to illustrate the analytical approach.
- The methodology (problem reframing, multi-hypothesis evaluation, preference for interpretability, explicit uncertainty) is transferable to real organisational data.
- The Streamlit application supports loading of external data via CSV upload or direct database connection.
- Limitations and lessons learned are documented separately for transparency.

---

*Prepared as a portfolio and teaching artifact demonstrating structured critical thinking in a data-science context.*
