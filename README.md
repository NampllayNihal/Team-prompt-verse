# AI Medical Prescription Verifier

## Features
- Hugging Face NER for drug extraction
- Check drug interactions from CSV
- FastAPI backend + Streamlit frontend

## How to Run

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run backend (from project root):
```
set PYTHONPATH=backend
uvicorn app.main:app --reload
```

3. Run frontend:
```
streamlit run frontend/streamlit_app.py
```

4. Open http://localhost:8501 in your browser.
