# Limitations and Lessons Learned

## Limitations of the Current Artifact
1. **Synthetic data**  
   All quantitative results are generated from a controlled synthetic dataset. While the data-generating process is documented, findings cannot be treated as organisational truth.

2. **Limited internal knowledge base for RAG**  
   The retrieval corpus contains only five short documents. In a real setting the knowledge base would be substantially larger and continuously updated.

3. **Free-tier constraints**  
   The Gemini free tier imposes daily request limits. This affected the ability to run the full set of RAG examples in a single session.

4. **Scope of modelling**  
   The delivered model is an interpretable Logistic Regression baseline plus a transparent rule-based score. More complex models were deliberately deprioritised under the simulated time pressure.

5. **No production monitoring**  
   The Streamlit application is a demonstration interface. It does not include production-grade monitoring, model registry, or automated retraining pipelines.

## Lessons Learned
1. **Reframing is high-leverage**  
   Spending time to restate the problem prevented premature commitment to a single solution and a single hypothesis.

2. **Interpretability has practical value under time pressure**  
   A transparent score that stakeholders can inspect and challenge is often more useful in the short term than a higher-accuracy black-box model.

3. **Evidence boundaries must be stated**  
   Explicitly documenting what the data does *not* support is as important as reporting what it does support.

4. **Complementary methods strengthen the analysis**  
   Quantitative segment analysis (Streamlit) and qualitative retrieval (RAG) together provide a more complete picture than either method alone.

5. **Documentation is part of the deliverable**  
   Clear, structured documentation increases the reusability and professional credibility of the work.

## Recommendations for Organisational Transfer
- Replace synthetic data with production extracts under appropriate governance.
- Expand the RAG knowledge base with real product, support, and historical analysis documents.
- Add basic monitoring around any deployed risk score (score distribution, outcome rates in high-score cohorts).
- Maintain the practice of stating uncertainty and proposing small, testable next actions.

---

*This section is included to meet professional standards of transparency regarding the boundaries and learning outcomes of the project.*
