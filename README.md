# Critical Thinking Applied to Customer Churn

I built this project to demonstrate how I handle a realistic, high-pressure data science request.

## The Scenario
Leadership at a subscription SaaS company saw monthly churn rise from ~4% to 7%. They asked me to “build a churn prediction model quickly” and believed a recent price increase was the main driver.

## My Approach
Instead of immediately training a complex model, I applied critical thinking:

- Reframed the problem
- Evaluated data quality and base rates
- Tested multiple hypotheses with segment analysis
- Built a transparent risk score
- Added an interpretable Logistic Regression baseline
- Delivered clear, actionable recommendations with uncertainty stated

## Live App
**Deploying on Streamlit Community Cloud**  
*(Live link will be added here once deployment completes)*

## How to Run Locally
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

## What This Project Shows
- Problem reframing under stakeholder pressure
- Rigorous data evaluation before modeling
- Preference for interpretability when it better serves the decision
- Clear communication of findings and next steps
- End-to-end thinking (analysis → simple score → baseline model → recommendation)

## Tech Stack
- Python, Pandas, NumPy, Scikit-learn
- Streamlit

All data is synthetic and generated inside the app.
