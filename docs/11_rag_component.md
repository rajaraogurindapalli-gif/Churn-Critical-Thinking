# RAG Component – Critical Thinking Churn Project

## Purpose
Add a Retrieval-Augmented Generation layer so that hypotheses and summaries are grounded in internal evidence.

## Implementation
- **Notebook:** `notebooks/RAG_Churn_Colab_Embeddings.ipynb`
- **Embedding model:** `sentence-transformers/all-MiniLM-L6-v2`
- **LLM:** `gemini-3.8-flash` (current recommended model)
- **Retrieval:** Cosine similarity over document embeddings

## How to run
1. Open the notebook in Google Colab.
2. Get a free Gemini API key from aistudio.google.com.
3. Run the cells and enter the key when prompted.

## Troubleshooting
- Protobuf warnings during install can be ignored.
- Older model names (`gemini-1.5-flash`, `gemini-2.5-flash`, etc.) are no longer available to new users.
- Use **`gemini-3.8-flash`** (as recommended by the API error message).
- To list models available to your key:
  ```python
  import google.generativeai as genai
  for m in genai.list_models():
      if 'generateContent' in m.supported_generation_methods:
          print(m.name)
  ```

## Relation to the main project
The Streamlit app performs the quantitative analysis.  
This notebook adds grounded qualitative context via RAG.
