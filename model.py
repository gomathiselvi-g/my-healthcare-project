<<<<<<< HEAD
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
=======
def predict_doctor(symptoms):
    symptoms = symptoms.lower()

    if "fever" in symptoms:
        return "General Physician"
    elif "skin" in symptoms:
        return "Dermatologist"
    elif "heart" in symptoms:
        return "Cardiologist"
    elif "eye" in symptoms:
        return "Ophthalmologist"
    else:
        return "General Doctor"
>>>>>>> 9a47424927eaf71f7a033d8751e3381dd5e98673
