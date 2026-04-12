def predict_doctor(symptom):
    symptom = symptom.lower()

    if "fever" in symptom:
        return "General Physician"
    elif "skin" in symptom:
        return "Dermatologist"
    elif "heart" in symptom:
        return "Cardiologist"
    else:
        return "Consult General Doctor"