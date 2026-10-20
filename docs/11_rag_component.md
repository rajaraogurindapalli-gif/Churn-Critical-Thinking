# RAG Component – Critical Thinking Churn Project

## Purpose
Add a Retrieval-Augmented Generation layer so that hypotheses and summaries are grounded in internal evidence rather than generated from general knowledge alone.

## Implementation
- **Notebook:** `notebooks/RAG_Churn_Colab_Embeddings.ipynb`
- **Embedding model:** `sentence-transformers/all-MiniLM-L6-v2` (free, runs on Colab)
- **LLM:** Gemini 1.5 Flash (free tier via Google AI Studio)
- **Retrieval:** Cosine similarity over document embeddings

## What it demonstrates
- Building a small internal knowledge base (product notes, support themes, past analyses)
- Semantic retrieval of relevant context
- Grounded generation of alternative hypotheses and executive summaries
- Alignment with the critical-thinking principle of evaluating a topic from multiple sides using available evidence

## How to run
1. Open the notebook in Google Colab.
2. Obtain a free Gemini API key from aistudio.google.com.
3. Run all cells and enter the key when prompted.

## Relation to the main project
The Streamlit app performs structured quantitative analysis.  
The RAG notebook supplements it by retrieving qualitative internal context that a pure tabular analysis would miss.
