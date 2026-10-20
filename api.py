from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_client import Counter, Histogram
import time

from src.inference import predict_single

app = FastAPI(title="Heart Disease API")

REQUEST_COUNT = Counter("request_count", "Total API requests")
LATENCY = Histogram("request_latency_seconds", "Request latency")

class PatientData(BaseModel):
    age: float
    sex: int
    cp: int
    trestbps: float
    chol: float
    fbs: int
    restecg: int
    thalach: float
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

@app.middleware("http")
async def metrics_middleware(request, call_next):
    start = time.time()
    response = await call_next(request)
    LATENCY.observe(time.time() - start)
    REQUEST_COUNT.inc()
    return response

@app.post("/predict")
def predict(data: PatientData):
    return predict_single(data.dict())

@app.get("/health")
def health():
    return {"status": "ok"}
