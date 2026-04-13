import streamlit as st
from fpdf import FPDF
import requests
from datetime import datetime

# FastAPI URL
API_URL = "http://127.0.0.1:8000/predict"

st.title("🏥 AI Healthcare System")

# Inputs
name = st.text_input("Enter your name")
symptoms = st.text_input("Enter your symptoms")


# PDF Function
def create_pdf(name, symptoms, doctor, date, time):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Healthcare Report", ln=True, align='C')
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Symptoms: {symptoms}", ln=True)
    pdf.cell(200, 10, txt=f"Recommended Doctor: {doctor}", ln=True)

    # 🔥 NEW
    pdf.cell(200, 10, txt=f"Appointment Date: {date}", ln=True)
    pdf.cell(200, 10, txt=f"Appointment Time: {time}", ln=True)

    file_name = "report.pdf"
    pdf.output(file_name)

    return file_name

date = st.date_input("Select appointment date 📅")
time = st.time_input("Select appointment time ⏰")

# 🔥 ONLY ONE BUTTON
if st.button("Predict Doctor"):

    if name == "" or symptoms == "":
        st.warning("Please fill all fields")
    else:
        try:
            response = requests.post(API_URL, json={
                "name": name,
                "symptoms": symptoms
            })

            if response.status_code == 200:
                data = response.json()
                doctor = data["recommended_doctor"]

                st.success(f"Doctor: {doctor}")

                # ✅ FIXED HERE
                pdf_file = create_pdf(name, symptoms, doctor, date, time)

                with open(pdf_file, "rb") as f:
                    st.download_button("Download PDF", f, file_name="report.pdf")

            else:
                st.error("API error! Check backend")

        except:
            st.error("API not running! Start FastAPI first.")
if response.status_code == 200:
    data = response.json()
    doctor = data["recommended_doctor"]
else:
    st.error("API error! Check backend")

            # Generate PDF
            pdf_file = create_pdf(name, symptoms, doctor, date, time)

            with open(pdf_file, "rb") as f:
                st.download_button("Download PDF", f, file_name="report.pdf")

        except:
            st.error("API not running! Start FastAPI first.")


# 🤖 Chatbot Section
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
    if user_input != "":
        response = chatbot_response(user_input)
        st.write(response)