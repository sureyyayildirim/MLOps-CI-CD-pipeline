from fastapi import FastAPI
from pydantic import BaseModel
from app.feature_engineering import stable_hash_bucket

app = FastAPI(title="MLOps CI/CD Demo Service")

class PredictIn(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(inp: PredictIn):
    bucket = stable_hash_bucket(inp.text, 100)
    return {"bucket": bucket}
