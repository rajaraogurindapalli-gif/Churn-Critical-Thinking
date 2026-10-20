# RAG Component – Critical Thinking Churn Project

## Purpose
Add a Retrieval-Augmented Generation layer so conclusions are grounded in internal evidence rather than a single preferred explanation.

## Status
**Verified working** (October 2026) with:
- Embedding model: `sentence-transformers/all-MiniLM-L6-v2`
- LLM: `gemini-3.8-flash`
- Retrieval: cosine similarity

Successful outputs included:
- Recognition that no direct evidence links the UI redesign to churn
- Ranked alternative hypotheses with strength of document support
- Explicit statements of what the evidence does *not* allow us to conclude

## How it supports critical thinking
- Surfaces multiple internal sources instead of only the price narrative
- Forces the model to answer only from retrieved documents
- Includes questions that ask what cannot be concluded
- Complements the quantitative analysis in the Streamlit app

## How to run
1. Open `notebooks/RAG_Churn_Colab_Embeddings.ipynb` in Google Colab.
2. Enter a free Gemini API key when prompted.
3. Run all cells.

## Troubleshooting
- Protobuf warnings on install can be ignored.
- Use `gemini-3.8-flash` (older model names are no longer available to new users).
- **Free-tier quota**: `gemini-3.8-flash` allows a limited number of requests per day (observed limit: 20). If you see `RESOURCE_EXHAUSTED`, wait for the quota to reset or use a second API key.
- Restart the Colab runtime if imports fail after the pip install.

## Relation to the main project
- Streamlit app → quantitative diagnosis and transparent score  
- RAG notebook → qualitative context and alternative hypotheses  
Both are needed for a full critical-thinking response to the original leadership request.
