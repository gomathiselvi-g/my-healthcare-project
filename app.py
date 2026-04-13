import streamlit as st
from fpdf import FPDF
from model import predict_doctor

st.title("AI Healthcare System")

# Inputs
name = st.text_input("Enter your name")
symptoms = st.text_input("Enter your symptoms")

# PDF Function
def create_pdf(name, symptoms, doctor):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Healthcare Report", ln=True, align='C')
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Symptoms: {symptoms}", ln=True)
    pdf.cell(200, 10, txt=f"Recommended Doctor: {doctor}", ln=True)

    file_name = "report.pdf"
    pdf.output(file_name)

    return file_name


# Predict Button (ONLY ONCE)
if st.button("Predict Doctor"):
    doctor = predict_doctor(symptoms)
    st.success(f"Doctor: {doctor}")

    pdf_file = create_pdf(name, symptoms, doctor)

    with open(pdf_file, "rb") as f:
        st.download_button("Download PDF", f, file_name="report.pdf")


# Chatbot Section
st.subheader("Chatbot 🤖")

user_input = st.text_input("Ask something")

def chatbot_response(text):
    text = text.lower()

    if "hello" in text:
        return "Hi! How can I help you?"
    elif "fever" in text:
        return "You should consult a General Physician."
    elif "skin" in text:
        return "Consult a Dermatologist."
    elif "heart" in text:
        return "Consult a Cardiologist."
    elif "bye" in text:
        return "Take care! 👋"
    else:
        return "Sorry, I didn't understand."

if st.button("Send"):
    response = chatbot_response(user_input)
    st.write(response)