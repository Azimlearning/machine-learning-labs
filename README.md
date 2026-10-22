# Machine Learning Labs

Lab work for TEB3123 Machine Learning, Universiti Teknologi PETRONAS (September 2026).

Name: Fakhrul Azim bin Ahmed Mardzukie
Student ID: 22012087
Email: fakhrul_22012087@utp.edu.my

## Labs

| Lab | Topic | Notebook | Status |
|---|---|---|---|
| 1 | Feature engineering and feature selection | `ML LAB/all_experiments/lab01/lab01_features_worked.ipynb` | Done |
| 2 | Supervised learning workflow | `ML LAB/all_experiments/lab02/lab02_supervised_workflow.ipynb` | Done |
| 3 | Supervised learning models | `ML LAB/all_experiments/lab03/lab03_model_families.ipynb` | Done |
| 4 | Clustering and PCA | `ML LAB/all_experiments/lab04/lab04_clustering_pca.ipynb` | Done |
| 5 | Anomaly detection and limited labels | | |
| 6 | Reinforcement learning | | |
| 7 | Deep learning: CNN | | |
| 8 | Deep learning: LSTM | | |

## Setup

```
conda create -n ml python=3.12
conda activate ml
pip install -r "ML LAB/requirements.txt"
```

Download the datasets into `ML LAB/all_datasets/` (list in `ML LAB/all_datasets/README.md`).

## Running

```
conda activate ml
cd "ML LAB"
jupyter notebook
```

Open a notebook in its `all_experiments/labNN/` folder and run all cells. The notebooks also open in VS Code with the Jupyter extension, using the `ml` environment as the kernel.

## Folder layout

```
ML LAB/
  all_datasets/      datasets (not uploaded)
  all_experiments/   one folder per lab (labNN/), each with its notebook
                     and the models that lab saves (labNN/models/)
  requirements.txt
```
