# RAG Component – Critical Thinking Churn Project

## Purpose
Add a Retrieval-Augmented Generation layer so that hypotheses and summaries are grounded in internal evidence.

## Implementation
- **Notebook:** `notebooks/RAG_Churn_Colab_Embeddings.ipynb`
- **Embedding model:** `sentence-transformers/all-MiniLM-L6-v2`
- **LLM:** Gemini (recommended: `gemini-2.5-flash` or `gemini-flash-latest`)
- **Retrieval:** Cosine similarity over document embeddings

## How to run
1. Open the notebook in Google Colab.
2. Get a free Gemini API key from aistudio.google.com.
3. Run the cells and enter the key when prompted.

## Troubleshooting
- **Protobuf warnings** during install: ignore them.
- **Model not found** (`gemini-1.5-flash` or similar):
  - Older 1.5 model names are no longer available.
  - Use one of these instead:
    - `gemini-2.5-flash`
    - `gemini-flash-latest`
    - `gemini-3.8-flash`
  - Or list models available to your key:
    ```python
    import google.generativeai as genai
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    ```
- Restart the Colab runtime if imports fail after install.

## Relation to the main project
The Streamlit app does the quantitative analysis.  
This notebook adds grounded qualitative context via RAG.
