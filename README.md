# HRONE Backend

FastAPI backend for HROne task with MongoDB.

## How to Run

1. Create virtualenv:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
uvicorn main:app --reload
```

4. Visit docs:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)