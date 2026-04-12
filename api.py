from fastapi import FastAPI
<<<<<<< HEAD
=======
from pydantic import BaseModel
>>>>>>> 9a47424927eaf71f7a033d8751e3381dd5e98673
from model import predict_doctor

app = FastAPI()

<<<<<<< HEAD
@app.get("/")
def home():
    return {"message": "AI Healthcare API Running"}

@app.get("/predict")
def predict(symptom: str):
    doctor = predict_doctor(symptom)
    return {"doctor": doctor}
=======
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
>>>>>>> 9a47424927eaf71f7a033d8751e3381dd5e98673
