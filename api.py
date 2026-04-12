from fastapi import FastAPI
from pydantic import BaseModel
from model import predict_doctor

app = FastAPI()

class Patient(BaseModel):
    name: str
    symptoms: str

@app.get("/")
def home():
    return {"message": "API Running"}

@app.post("/predict")
def predict(data: Patient):
    doctor = predict_doctor(data.symptoms)
    return {
        "patient": data.name,
        "recommended_doctor": doctor
    }