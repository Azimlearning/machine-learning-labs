# all_datasets/

Raw Kaggle datasets for the labs. **Read-only**: never edit these files; clean via code or a copy. The data files are git-ignored (only this README is committed), so every machine downloads them itself.

## Download steps

1. Open the link, click Download, and extract the archive.
2. Copy the required CSV files or images into this folder.
3. Check that the notebook's file paths match the filenames, including capitalisation.

For `FileNotFoundError`, fix the working directory or the path — don't move files into the project root. Keep the digits ZIP intact.

## Expected files (from lab notes §2.1)

| File | Dataset | Used in | Link |
|---|---|---|---|
| `breast_cancer_dataset.csv` | Breast Cancer Wisconsin | Labs 1, 2, 3, 5 | https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data |
| `medical_cost_personal_dataset.csv` | Medical Cost Personal Data | Labs 1, 2 | https://www.kaggle.com/datasets/mirichoi0218/insurance |
| `student_performance_dataset.csv` | Student Performance | Lab 1 | https://www.kaggle.com/datasets/larsen0966/student-performance-data-set |
| `titanic_dataset.csv` | Titanic Dataset | Labs 1, 2, 3 | https://www.kaggle.com/datasets/yasserh/titanic-dataset |
| `bike_sharing_dataset_day.csv`, `bike_sharing_dataset_hour.csv` | Bike Sharing | Labs 2, 8 | https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset |
| `heart_failure_dataset.csv` | Heart Failure Prediction | Lab 2 try-it | https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction |
| `ames_housing_dataset.csv` | Ames Housing | Lab 3 | https://www.kaggle.com/datasets/shashanknecrothapa/ames-housing-dataset |
| `red_wine_quality_dataset.csv` | Red Wine Quality | Lab 3 | https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009 |
| `mall_customers_dataset.csv` | Mall Customers | Lab 4 | https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python |
| `optical_recognition_handwritten_digits.zip` | Optical Recognition of Handwritten Digits | Labs 4, 7 | https://www.kaggle.com/datasets/yadavhim/optical-recognition-of-handwritten-digits |
| `credit_card_fraud_dataset.csv` | Credit Card Fraud Detection | Lab 5 | https://www.kaggle.com/datasets/miadul/credit-card-fraud-detection-dataset |

Kaggle's own filenames may differ from the ones above; rename to match the lab notes and say so here.
