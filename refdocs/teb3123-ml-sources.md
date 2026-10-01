# TEB3123 Machine Learning — Sources & References

> Raw research and external dependencies. The PRD is the *decided* view; this file is the *considered* view — including things that were looked at and rejected, which is often the more useful half.
> Record a source when it's chosen, and again when it's rejected. "We already tried that and here's why it didn't fit" is the single most expensive fact to re-derive.

Last updated: 2026-10-01

---

## Founding context documents

The documents this project was scaffolded from. Kept because the PRD paraphrases them and paraphrase loses detail. All local-only.

- `ML LECTURE/Lecture 1 Introduction to Machine Learning.pdf` (56 pp) — course admin, grading, dates, ML fundamentals.
- `ML LECTURE/Lecture 2 Machine Learning Pipeline.pdf` (109 pp) — CRISP-DM, pipeline, data formats, pandas wrangling, missing values, encoding, scaling, visualisation.
- `ML LECTURE/Lecture 3-4 Feature Engineering (Part A-Updated).pdf` (163 pp) — numeric, categorical, text, temporal and image features.
- `ML LAB/ML-Python-Datasets.pdf` (4 pp) — project layout, dataset list with Kaggle links, environment setup. Same content as `chapter-01.pdf`; only the chapter number differs (2 vs 1).
- `ML LAB/chapter-01.pdf` (4 pp) — identical environment-setup chapter, numbered 1.
- `ML LAB/chapter-02.pdf` (4 pp) — "Where to Begin": ML vocabulary, workflow, learning settings, error costs.
- `ML LAB/chapter-03.pdf` (8 pp) — "Understanding and Preparing Data": quality checks, splits, leakage, missing values, encoding, scaling, pipelines.
- Class WhatsApp messages pasted 2026-10-01 (GitHub SSH task, repo layout, upcoming lab).

Note: the lecture decks and lab notes number chapters differently (Lecture "Chapter 3: Feature Engineering" vs lab notes "Chapter 3: Understanding and Preparing Data"). Say which one you mean.

---

## External code & libraries

Versions are unpinned in `requirements.txt`. Licenses were not checked.

| Name | What it does for us | Link | License | Status |
|---|---|---|---|---|
| numpy | Arrays | https://numpy.org | not checked | Chosen (lab notes) |
| pandas | Tabular data | https://pandas.pydata.org | not checked | Chosen |
| matplotlib | Plots | https://matplotlib.org | not checked | Chosen |
| scikit-learn | Models, pipelines, metrics | https://scikit-learn.org | not checked | Chosen |
| joblib | Saving models | https://joblib.readthedocs.io | not checked | Chosen |
| jupyter | Notebooks | https://jupyter.org | not checked | Chosen |
| torch | CNN/LSTM, Labs 7–8 (CPU) | https://pytorch.org | not checked | Chosen; not installed yet |

Observed in Anaconda base on 2026-10-01: numpy 2.4.6, pandas 3.0.3, matplotlib 3.11.0, scikit-learn 1.9.0, joblib 1.5.3, jupyter 1.1.1. These are base-env facts, not what `ml` will resolve.

---

## APIs & services

| Service | Used for | Pricing model | Auth / key location | Status |
|---|---|---|---|---|
| GitHub | Lab and project submission | Free | SSH key in `~/.ssh` (not in repo) | To set up (P0) |
| Kaggle | Dataset downloads (manual, via browser) | Free | Kaggle login in browser; no API token used | In use |

---

## Reference material

Datasets (from lab notes §2.2):

| Dataset | Used in | Link |
|---|---|---|
| Breast Cancer Wisconsin | Labs 1, 2, 3, 5 | https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data |
| Medical Cost Personal Data | Labs 1, 2 | https://www.kaggle.com/datasets/mirichoi0218/insurance |
| Student Performance | Lab 1 | https://www.kaggle.com/datasets/larsen0966/student-performance-data-set |
| Titanic Dataset | Labs 1, 2, 3 | https://www.kaggle.com/datasets/yasserh/titanic-dataset |
| Bike Sharing | Labs 2, 8 | https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset |
| Heart Failure Prediction | Lab 2 try-it | https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction |
| Ames Housing | Lab 3 | https://www.kaggle.com/datasets/shashanknecrothapa/ames-housing-dataset |
| Red Wine Quality | Lab 3 | https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009 |
| Mall Customers | Lab 4 | https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python |
| Optical Recognition of Handwritten Digits | Labs 4, 7 | https://www.kaggle.com/datasets/yadavhim/optical-recognition-of-handwritten-digits |
| Credit Card Fraud Detection | Lab 5 | https://www.kaggle.com/datasets/miadul/credit-card-fraud-detection-dataset |

Setup links: Python https://www.python.org/downloads/ · venv docs https://docs.python.org/3/library/venv.html · Miniconda https://docs.anaconda.com/miniconda/ · Anaconda https://www.anaconda.com/download

GitHub SSH videos from the TA's playlist (https://www.youtube.com/playlist?list=PLinUrn8TVRE8TakJwrFYdOsH1i1GBBdVN). Not watched by this tooling; assignment of videos to OS is inferred (A-09):
- General: https://www.youtube.com/watch?v=AOM8CEyu3Ug
- Windows (likely): https://www.youtube.com/watch?v=YT5YimhyX18
- macOS (likely): https://www.youtube.com/watch?v=ACvE5Uy7ZB0

TA's reference repo layout: https://github.com/reeyan-afzal-khan/MACHINE-LEARNING (returned 404 to the GitHub API on 2026-10-01).

Recommended texts (Lecture 1): Müller & Guido, *Introduction to Machine Learning with Python* (2017); Albon, *Python Machine Learning Cookbook* (2018); Swamynathan, *Mastering Machine Learning with Python in Six Steps* (2017); Géron, *Hands-On Machine Learning with Scikit-Learn & TensorFlow* (2017); Sarkar, *Practical Machine Learning with Python* (2018); Mukhopadhyay, *Advanced Data Analytics using Python* (2018).

Course contacts (Lecture 1): AP Ts Dr Shuhaida M Shuhidan (coordinator), Muhammad Hamza Azam (lecturer, mhamza.azam@utp.edu.my), TAs Reeyan Afzal Khan and Abdul Muiz Fayyaz. Announcements on uLearn and the WhatsApp group.

---

## Considered and rejected

| Option | Why it looked good | Why it lost | Recorded in |
|---|---|---|---|
| venv on Python 3.12 | Lab notes Route A; lightweight | Needs a separate Python 3.12 install when Anaconda is already present | D-02 |
| Anaconda `base` env | Already has most packages | No torch, Python 3.14, and the lab notes say never install into base | D-02 |
| Python 3.13 (installed) | Zero setup | Lab notes pin 3.12 for library support; torch wheel availability for 3.13 not verified | D-02 |
