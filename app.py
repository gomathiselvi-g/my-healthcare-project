import streamlit as st
from model import predict_doctor

st.title("AI Healthcare System")

name = st.text_input("Enter your name")
symptoms = st.text_input("Enter your symptoms")

if st.button("Predict Doctor"):
    doctor = predict_doctor(symptoms)
    st.success(f"Doctor: {doctor}")