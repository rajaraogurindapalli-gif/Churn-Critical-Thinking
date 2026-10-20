# RAG Component – Critical Thinking Churn Project

## Purpose
Add a Retrieval-Augmented Generation layer so conclusions are grounded in internal evidence rather than a single preferred explanation.

## Status
**Verified working** (October 2026) with:
- Embedding model: `sentence-transformers/all-MiniLM-L6-v2`
- LLM: `gemini-3.8-flash`
- Retrieval: cosine similarity

## How it supports critical thinking
- Surfaces multiple internal sources (UI changes, support themes, past analyses, onboarding) instead of only the price narrative.
- Forces the model to answer only from retrieved documents.
- Includes questions that explicitly ask what the evidence does *not* support.
- Complements the quantitative segment analysis in the Streamlit app.

## How to run
1. Open `notebooks/RAG_Churn_Colab_Embeddings.ipynb` in Google Colab.
2. Enter a free Gemini API key when prompted.
3. Run all cells.

## Troubleshooting
- Protobuf warnings on install can be ignored.
- Use `gemini-3.8-flash` (older model names are no longer available to new users).
- Restart the Colab runtime if imports fail after the pip install.

## Relation to the main project
- Streamlit app → quantitative diagnosis and transparent score  
- RAG notebook → qualitative context and alternative hypotheses  
Both are needed for a full critical-thinking response to the original leadership request.
