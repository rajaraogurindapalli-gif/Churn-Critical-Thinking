# Critical Thinking Applied to Customer Churn

**Portfolio Project**  
Demonstrates structured critical thinking in a high-pressure data-science scenario.

## Executive Summary
Leadership requested a rapid churn prediction model after observing a rise from ~4% to 7%, attributing the increase primarily to a recent price change.  
The analysis reframed the problem, evaluated multiple competing hypotheses, and delivered a transparent risk score together with an interpretable baseline model rather than a complex black-box solution.

**Full executive brief:** [docs/00_EXECUTIVE_BRIEF.md](docs/00_EXECUTIVE_BRIEF.md)

## Live Application
**[Open the interactive app](https://churn-critical-thinking-9hcutmuurluprsw36jqqz2.streamlit.app/)**

The application supports:
- Synthetic demonstration data
- CSV upload
- Direct database connection (PostgreSQL, MySQL, SQLite)

## Repository Structure
```
├── app.py                          # Streamlit application
├── requirements.txt                 # Dependencies
├── docs/                           # Professional documentation
│   ├── 00_EXECUTIVE_BRIEF.md
│   ├── 01_problem_definition.md
│   ├── 11_rag_component.md
│   └── recommendation.md
└── notebooks/                      # RAG analysis (Google Colab)
    └── RAG_Churn_Colab_Embeddings.ipynb
```

## Local Execution
```bash
git clone https://github.com/rajaraogurindapalli-gif/Churn-Critical-Thinking.git
cd Churn-Critical-Thinking
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

## What This Project Demonstrates
- Problem reframing under stakeholder pressure and time constraints
- Rigorous data evaluation and multi-hypothesis testing
- Preference for interpretability when it better serves the decision
- Clear communication of findings, uncertainty, and next actions
- End-to-end delivery (analysis → transparent score → baseline model → interactive application)
- Complementary qualitative analysis via Retrieval-Augmented Generation

## Technology
Python · Pandas · NumPy · Scikit-learn · Streamlit  
Google Colab · Gemini API · sentence-transformers (RAG component)

---

*All demonstration data is synthetic. The methodology is designed for transfer to organisational datasets.*
