# Cricket Score Prediction — Public Portfolio Demo

A compact, reproducible machine-learning portfolio project for forecasting cricket innings totals from live match state.

This public repository is a lightweight demonstration derived from my larger academic cricket analytics project. The full research system, large datasets, trained artifacts, and production evidence remain private.

## What this project demonstrates

- Python data processing and feature engineering
- Live match-state transformation
- XGBoost-ready tabular features
- Leakage-aware train/test thinking
- Model evaluation with MAE and RMSE
- Clean, testable project structure
- Practical ML code that can be adapted to client datasets

## Example live features

The feature pipeline converts a match state into model-ready variables such as:

- current runs
- wickets lost
- overs completed
- current run rate
- balls remaining
- wickets remaining
- recent scoring rate
- projected baseline score

## Research results from the full private project

The completed academic system supports T20, ODI, and Test formats. On the frozen T20 historical holdout, the main model achieved:

- MAE: 16.74 runs
- RMSE: 24.03
- R²: 0.742
- 18-over checkpoint MAE: 5.75 runs

These are error measurements, not a generic accuracy percentage.

## Repository structure

```text
src/
  features.py       # match-state validation and feature engineering
  baseline.py       # transparent baseline score projection
tests/
  test_features.py  # unit tests for the feature pipeline
requirements.txt
```

## Quick start

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate

pip install -r requirements.txt
pytest -q
```

Example:

```python
from src.features import MatchState, build_features
from src.baseline import projected_total

state = MatchState(
    current_runs=128,
    wickets_lost=3,
    overs_completed=15.0,
    recent_runs=42,
    recent_balls=30,
)

features = build_features(state)
print(features)
print(projected_total(state))
```

## Notes

The public demo intentionally avoids publishing proprietary data, private model artifacts, or large research files. It is meant to show code quality, ML workflow design, and the type of delivery I can provide for data-science and machine-learning projects.

## Skills

Python · pandas · NumPy · scikit-learn · XGBoost · Feature Engineering · Data Analysis · Machine Learning · Model Evaluation
