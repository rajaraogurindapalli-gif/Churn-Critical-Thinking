# RAG Component – Critical Thinking Churn Project

## Purpose
Add a Retrieval-Augmented Generation layer so that hypotheses and summaries are grounded in internal evidence rather than generated from general knowledge alone.

## Implementation
- **Notebook:** `notebooks/RAG_Churn_Colab_Embeddings.ipynb`
- **Embedding model:** `sentence-transformers/all-MiniLM-L6-v2` (free, runs on Colab)
- **LLM:** Gemini (use `gemini-1.5-flash-latest` or `gemini-2.0-flash`)
- **Retrieval:** Cosine similarity over document embeddings

## What it demonstrates
- Building a small internal knowledge base
- Semantic retrieval of relevant context
- Grounded generation of alternative hypotheses and executive summaries
- Alignment with critical thinking (evaluate from multiple sides using available evidence)

## How to run
1. Open the notebook in Google Colab.
2. Obtain a free Gemini API key from aistudio.google.com.
3. Run all cells and enter the key when prompted.

## Troubleshooting
- **Protobuf dependency warnings** during `pip install` are common in Colab and can be ignored.
- **Model not found error** (`models/gemini-1.5-flash is not found`):
  - Change the model name in the notebook to one of:
    - `gemini-1.5-flash-latest`
    - `gemini-2.0-flash`
    - `gemini-flash-latest`
  - Re-run the cell after the change.
- If imports fail after install, restart the Colab runtime and run from the top.

## Relation to the main project
The Streamlit app performs structured quantitative analysis.  
The RAG notebook supplements it by retrieving qualitative internal context.
