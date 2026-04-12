from fastapi import FastAPI
from model import predict_doctor

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Healthcare API Running"}

@app.get("/predict")
def predict(symptom: str):
    doctor = predict_doctor(symptom)
    return {"doctor": doctor}