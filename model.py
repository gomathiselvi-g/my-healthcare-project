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
