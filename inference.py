import pickle
import pandas as pd
from src.config import MODEL_PATH

def load_model():
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

def predict_single(input_dict: dict):
    model = load_model()
    df = pd.DataFrame([input_dict])
    proba = model.predict_proba(df)[0, 1]
    pred = int(proba >= 0.5)
    return {"prediction": pred, "confidence": float(proba)}
