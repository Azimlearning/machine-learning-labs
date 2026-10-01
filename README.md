# Machine Learning Labs

Lab notebooks, saved models, results and course project for **TEB3123 Machine Learning**, Universiti Teknologi PETRONAS (UTP), September 2026 semester.

## Student

| | |
|---|---|
| **Name** | Fakhrul Azim bin Ahmed Mardzukie |
| **Student ID** | 22012087 |
| **Email** | fakhrul_22012087@utp.edu.my |
| **Course** | TEB3123 Machine Learning |
| **University** | Universiti Teknologi PETRONAS |

## What this repo contains

Eight weekly labs, each with one worked notebook, plus the course project. Models are saved with joblib into `models/` and evidence is written to `results/labNN/` by the notebooks.

| Lab | Topic | Datasets | Status |
|---|---|---|---|
| 1 | Feature engineering: scaling, pipelines, data quality, feature selection | Breast Cancer, Medical Cost, Student Performance, Titanic | Not started |
| 2 | Supervised workflow: baselines, thresholds, linear/ridge regression, tuning, saving, time splits | Breast Cancer, Medical Cost, Titanic, Bike Sharing, Heart Failure | Not started |
| 3 | Supervised models: KNN, naive Bayes, SVM, trees, random forests, gradient boosting | Breast Cancer, Titanic, Ames Housing, Red Wine | Not started |
| 4 | Clustering and PCA: K-means, DBSCAN | Mall Customers, Handwritten Digits | Not started |
| 5 | Anomaly detection and limited labels, imbalanced evaluation | Credit Card Fraud, Breast Cancer | Not started |
| 6 | Reinforcement learning | none listed | Not started |
| 7 | Deep learning: CNN | Handwritten Digits | Not started |
| 8 | Deep learning: LSTM forecasting | Bike Sharing | Not started |
| Project | Course project (briefing week 6, due week 10) | TBA | Not started |

Status is updated as labs are completed; the live version is in [`refdocs/STATUS.md`](refdocs/STATUS.md).

## Setup

Requires Anaconda or Miniconda. In *Anaconda PowerShell Prompt* (Windows) or any shell with conda:

```bash
conda create -n ml python=3.12
conda activate ml
cd "ML LAB"
pip install -r requirements.txt
```

Dependencies: numpy, pandas, matplotlib, scikit-learn, joblib, jupyter, torch (CPU is sufficient).

Datasets are not stored in the repo. Download them from the Kaggle links in [`ML LAB/all_datasets/README.md`](ML%20LAB/all_datasets/README.md) into `ML LAB/all_datasets/`.

## Usage

```bash
conda activate ml
cd "ML LAB/all_experiments"
jupyter notebook
```

Run each lab notebook from top to bottom. Preprocessing is fitted on training data only, inside a scikit-learn `Pipeline`, and the test set is used once at the end.

## Project layout

```
.
├── CLAUDE.md                 operating brief for AI-assisted sessions
├── README.md
├── .claude/                  settings, subagents, commands
├── refdocs/                  PRD, status, plans, changelog, guides
└── ML LAB/
    ├── all_datasets/         Kaggle CSVs (not committed)
    ├── all_experiments/      lab01 ... lab08 notebooks, predict_passenger.py
    ├── models/               written by the notebooks
    ├── results/labNN/        written by the notebooks
    └── requirements.txt
```

## Documentation

| Doc | What's in it |
|---|---|
| [`refdocs/STATUS.md`](refdocs/STATUS.md) | Where the work actually is right now |
| [`refdocs/teb3123-ml-PRD.md`](refdocs/teb3123-ml-PRD.md) | Scope, roadmap, decision log |
| [`refdocs/changelog/CHANGELOG.md`](refdocs/changelog/CHANGELOG.md) | Session-by-session history |
| [`refdocs/changelog/DECISIONS.md`](refdocs/changelog/DECISIONS.md) | Why things are the way they are |
| [`refdocs/guides/env_setup.md`](refdocs/guides/env_setup.md) | Conda env and GitHub SSH |
| [`refdocs/guides/checklist.md`](refdocs/guides/checklist.md) | Pre-push checklist |
