import streamlit as st
import pandas as pd
import numpy as np
from joblib import load

# Load saved model, scaler, and column names
model = load('churn_model.joblib')
scaler = load('scaler.joblib')
model_columns = load('columns.joblib')

st.title("📞 Telecom Customer Churn Prediction")

# Sidebar input
st.sidebar.header("Enter Customer Details")

def user_input():
    gender = st.sidebar.selectbox("Gender", ['Male', 'Female'])
    SeniorCitizen = st.sidebar.selectbox("Senior Citizen", [0, 1])
    Partner = st.sidebar.selectbox("Partner", ['Yes', 'No'])
    Dependents = st.sidebar.selectbox("Dependents", ['Yes', 'No'])
    tenure = st.sidebar.slider("Tenure (months)", 0, 72, 12)
    PhoneService = st.sidebar.selectbox("Phone Service", ['Yes', 'No'])
    MultipleLines = st.sidebar.selectbox("Multiple Lines", ['Yes', 'No', 'No phone service'])
    InternetService = st.sidebar.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
    OnlineSecurity = st.sidebar.selectbox("Online Security", ['Yes', 'No', 'No internet service'])
    OnlineBackup = st.sidebar.selectbox("Online Backup", ['Yes', 'No', 'No internet service'])
    DeviceProtection = st.sidebar.selectbox("Device Protection", ['Yes', 'No', 'No internet service'])
    TechSupport = st.sidebar.selectbox("Tech Support", ['Yes', 'No', 'No internet service'])
    StreamingTV = st.sidebar.selectbox("Streaming TV", ['Yes', 'No', 'No internet service'])
    StreamingMovies = st.sidebar.selectbox("Streaming Movies", ['Yes', 'No', 'No internet service'])
    Contract = st.sidebar.selectbox("Contract", ['Month-to-month', 'One year', 'Two year'])
    PaperlessBilling = st.sidebar.selectbox("Paperless Billing", ['Yes', 'No'])
    PaymentMethod = st.sidebar.selectbox("Payment Method", [
        'Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
    MonthlyCharges = st.sidebar.slider("Monthly Charges", 0, 150, 70)
    TotalCharges = st.sidebar.slider("Total Charges", 0, 10000, 2500)

    data = {
        'gender': gender, 'SeniorCitizen': SeniorCitizen, 'Partner': Partner,
        'Dependents': Dependents, 'tenure': tenure, 'PhoneService': PhoneService,
        'MultipleLines': MultipleLines, 'InternetService': InternetService,
        'OnlineSecurity': OnlineSecurity, 'OnlineBackup': OnlineBackup,
        'DeviceProtection': DeviceProtection, 'TechSupport': TechSupport,
        'StreamingTV': StreamingTV, 'StreamingMovies': StreamingMovies,
        'Contract': Contract, 'PaperlessBilling': PaperlessBilling,
        'PaymentMethod': PaymentMethod, 'MonthlyCharges': MonthlyCharges,
        'TotalCharges': TotalCharges
    }
    return pd.DataFrame([data])

# Get user input
input_df = user_input()

# Convert categorical variables
input_encoded = pd.get_dummies(input_df)

# Align columns with training set
input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

# Scale the input
input_scaled = scaler.transform(input_encoded)

# Make prediction
prediction = model.predict(input_scaled)
prob = model.predict_proba(input_scaled)[0][1]

# Show result
st.subheader("Prediction Result")
st.write("Churn Probability: {:.2f}%".format(prob * 100))
st.success("✅ Customer is likely to stay." if prediction[0] == 0 else "⚠️ Customer is likely to churn.")
