# 🚀 CI/CD Demo with GitHub Actions

A simple calculator app that demonstrates **Continuous Integration & Continuous Deployment** using GitHub Actions.

-----

## 📁 Project Structure

```
cicd-demo/
├── .github/
│   └── workflows/
│       └── pipeline.yml    ← The CI/CD magic happens here!
├── src/
│   └── calculator.py       ← Our "application"
├── tests/
│   └── test_calculator.py  ← Automated tests
└── README.md
```

---

## 🔄 How the Pipeline Works

Every time you push code to GitHub, this happens **automatically**:

```
Push code → GitHub Actions triggers
               ↓
    ┌──────────────────┐    ┌──────────────────┐
    │  JOB 1: Tests    │    │  JOB 2: Lint     │
    │  (3 Python vers) │    │  (code quality)  │
    └────────┬─────────┘    └────────┬─────────┘
             └──────────┬────────────┘
                        ↓  (only if BOTH pass)
             ┌──────────────────────┐
             │  JOB 3: Deploy 🚀    │
             │  (only on 'main')    │
             └──────────────────────┘
```

---

## 🎯 Demo Steps

### Step 1: Show the passing pipeline
Push any change to `main` and watch the pipeline go green ✅

### Step 2: Break a test (introduce a bug)
Edit `src/calculator.py` — change `add` to return `a - b`:
```python
def add(a, b):
    return a - b  # BUG! This is wrong!
```
Push to GitHub → watch the pipeline **fail** 🔴 before it can deploy!

### Step 3: Fix the bug
Revert the change, push again → pipeline goes green, deploys ✅

### Key Points to Explain:
- **No human approval needed** — it's fully automated
- **Multiple Python versions** tested simultaneously (matrix strategy)
- **Deploy only happens if tests pass** — the `needs:` keyword
- **Deploy only on `main`** — feature branches don't deploy
- **Every commit is traceable** — SHA in deployment summary

---

## 🏃 Run Tests Locally

```bash
pip install pytest pytest-cov
pytest tests/ -v --cov=src
```
