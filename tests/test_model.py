from src.train import train
from src.inference import predict_single
from src.config import MODEL_PATH
import os

def test_model_training():
    train()
    assert os.path.exists(MODEL_PATH)

def test_model_inference():
    sample = {
        "age": 55,
        "sex": 1,
        "cp": 0,
        "trestbps": 140,
        "chol": 250,
        "fbs": 0,
        "restecg": 1,
        "thalach": 150,
        "exang": 0,
        "oldpeak": 1.0,
        "slope": 2,
        "ca": 0,
        "thal": 2
    }

    result = predict_single(sample)

    assert "prediction" in result
    assert "confidence" in result
    assert isinstance(result["prediction"], int)
    assert 0.0 <= result["confidence"] <= 1.0
