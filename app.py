import streamlit as st
from fpdf import FPDF
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title("🏥 AI Healthcare System")

# Inputs
name = st.text_input("Enter your name")
symptoms = st.text_input("Enter your symptoms")

date = st.date_input("Select appointment date 📅")
time = st.time_input("Select appointment time ⏰")


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
    pdf.cell(200, 10, txt=f"Appointment Date: {date}", ln=True)
    pdf.cell(200, 10, txt=f"Appointment Time: {time}", ln=True)

    file_name = "report.pdf"
    pdf.output(file_name)

    return file_name


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

                # PDF generate
                pdf_file = create_pdf(name, symptoms, doctor, date, time)

                with open(pdf_file, "rb") as f:
                    st.download_button("Download PDF", f, file_name="report.pdf")

            else:
                st.error("API error! Check backend")

        except:
            st.error("API not running! Start FastAPI first.")


# 🤖 Chatbot
st.subheader("Chatbot 🤖")

user_input = st.text_input("Ask something")
def chatbot_response(text):
    text = text.lower()

    if any(word in text for word in ["hello", "hi", "hey"]):
        return """Hello 😊  
I am your healthcare assistant.  

You can ask me about:
• Symptoms (fever, headache, etc.)
• Doctor suggestions  
• Appointments  
• General health tips  

How can I help you today?"""

    elif "fever" in text:
        return """Fever usually indicates an infection in your body.  

Possible reasons:
• Viral infection  
• Bacterial infection  
• Weather changes  

What you can do:
• Drink plenty of fluids 💧  
• Take rest 🛌  
• Monitor temperature  

👉 If fever continues for more than 2 days, consult a General Physician."""

    elif "headache" in text:
        return """Headache can occur due to:  

• Stress 😓  
• Dehydration 💧  
• Lack of sleep 😴  

Try this:
• Drink water  
• Take rest  
• Avoid screen time  

👉 If pain is severe, consult a doctor."""

    elif "appointment" in text:
        return """You can easily book an appointment using this app 📅  

Steps:
1. Enter your name  
2. Enter your symptoms  
3. Select date & time  
4. Click "Predict Doctor"  

You will get:
✔ Doctor suggestion  
✔ PDF report  
✔ Appointment details"""

    elif "doctor" in text:
        return """We suggest doctors based on your symptoms 👩‍⚕️  

Examples:
• Fever → General Physician  
• Skin issues → Dermatologist  
• Heart problems → Cardiologist  

👉 Enter your symptoms above to get recommendation."""

    elif "emergency" in text:
        return """🚨 This seems like an emergency  

Please:
• Visit nearest hospital immediately  
• Do not delay treatment  
• Call emergency services if needed  

Your safety is important!"""

    elif "thank" in text:
        return """You're welcome 😊  
I'm always here to help you!"""

    elif "bye" in text:
        return """Take care 👋  
Stay healthy and safe!"""

    else:
        return """I'm not fully sure about that 🤔  

But I can help you with:
• Symptoms  
• Doctor suggestions  
• Appointments  

Try asking something like:  
"fever", "headache", or "appointment" 😊"""

if st.button("Send"):
    if user_input != "":
        response = chatbot_response(user_input)
        st.write(response)