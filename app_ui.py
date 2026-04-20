import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Loan Prediction MLOps", layout="centered")

st.title("🏦 Loan Prediction System")
st.markdown("### MLOps Powered Application")

# ----------- INPUT FORM -----------

st.subheader("Enter Applicant Details")

Gender = st.selectbox("Gender", ["Male", "Female"])
Married = st.selectbox("Married", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])
ApplicantIncome = st.number_input("Applicant Income", value=5000)
CoapplicantIncome = st.number_input("Coapplicant Income", value=0)
LoanAmount = st.number_input("Loan Amount", value=100)
Loan_Amount_Term = st.number_input("Loan Term", value=360)
Credit_History = st.selectbox("Credit History", [1.0, 0.0])
Property_Area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])

# ----------- PREDICTION -----------

if st.button("Predict"):
    data = {
        "Gender": Gender,
        "Married": Married,
        "Dependents": Dependents,
        "Education": Education,
        "Self_Employed": Self_Employed,
        "ApplicantIncome": ApplicantIncome,
        "CoapplicantIncome": CoapplicantIncome,
        "LoanAmount": LoanAmount,
        "Loan_Amount_Term": Loan_Amount_Term,
        "Credit_History": Credit_History,
        "Property_Area": Property_Area
    }

    response = requests.post("http://127.0.0.1:8005/prediction_api", json=data)

    if response.status_code == 200:
        result = response.json()["status"]
        if result == "Approved":
            st.success("✅ Loan Approved")
        else:
            st.error("❌ Loan Rejected")
    else:
        st.error("Error connecting to API")

# ----------- BATCH PREDICTION -----------

st.subheader("📂 Batch Prediction")

file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    if st.button("Run Batch Prediction"):
        files = {"file": file.getvalue()}
        response = requests.post("http://127.0.0.1:8005/batch_prediction", files=files)

        if response.status_code == 200:
            st.success("Batch Prediction Completed")
            st.download_button("Download Results", response.content, "predictions.csv")
        else:
            st.error("Error processing file")

st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        height: 3em;
    }
    </style>
    """,
    unsafe_allow_html=True
)            