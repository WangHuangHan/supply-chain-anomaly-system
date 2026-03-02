from fastapi import FastAPI
from api.schema import AnomalyRequest
from api.service import detect_anomaly
from api.model_loader import load_model

app = FastAPI(title="Supply Chain Anomaly API")

model = load_model()

@app.get("/")
def root():
    return {"message": "Anomaly Detection API is running"}

@app.post("/detect_anomaly")
def detect(request: AnomalyRequest):
    results = detect_anomaly(model, request.records)
    return {"results": results}