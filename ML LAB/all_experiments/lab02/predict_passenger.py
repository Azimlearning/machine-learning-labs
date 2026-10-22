import argparse
from pathlib import Path

import joblib
import pandas as pd

# The model is saved by the Lab 2 notebook in the models folder next to this file.
MODEL = Path(__file__).resolve().parent / "models" / "titanic_survival.joblib"

parser = argparse.ArgumentParser(description="Predict Titanic survival with the saved Lab 2 model")
parser.add_argument("--pclass", type=int, required=True)
parser.add_argument("--sex", choices=["male", "female"], required=True)
parser.add_argument("--age", type=float, required=True)
parser.add_argument("--fare", type=float, required=True)
parser.add_argument("--sibsp", type=int, default=0)
parser.add_argument("--parch", type=int, default=0)
parser.add_argument("--embarked", choices=["C", "Q", "S"], default="S")
args = parser.parse_args()

passenger = pd.DataFrame([{
    "Pclass": args.pclass,
    "Sex": args.sex,
    "Age": args.age,
    "SibSp": args.sibsp,
    "Parch": args.parch,
    "Fare": args.fare,
    "Embarked": args.embarked,
}])

model = joblib.load(MODEL)
probability = model.predict_proba(passenger)[0, 1]
print(f"survival probability: {probability:.3f}")
print("prediction:", "survived" if probability >= 0.5 else "did not survive")
