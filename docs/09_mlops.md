# 09 – MLOps Considerations

Even with a simple score, basic MLOps thinking applies:

- Version the risk-score logic.
- Validate on hold-out or later data.
- Monitor score distribution and actual churn in high-score groups.
- Document assumptions and limitations.
- Prefer interpretability when it better serves the decision under time pressure.

The live Streamlit app makes the analysis inspectable and allows users to supply their own data for further validation.
