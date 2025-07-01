import streamlit as st
import pandas as pd
import joblib
import os

# Load model
model_path = os.path.join(os.path.dirname(__file__), "best_diabetes_logreg_model.pkl")
model = joblib.load(model_path)

# Set page configuration
st.set_page_config(
    page_title="Diabetes Prediction App",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# App title
st.title("🩺 Diabetes Prediction App")
st.markdown("Enter patient details below to predict diabetes risk.")

# Input sliders
pregnancies = st.slider("Pregnancies", 0, 17, 2)
glucose = st.slider("Glucose", 0, 200, 140)
blood_pressure = st.slider("Blood Pressure", 0, 122, 70)
skin_thickness = st.slider("Skin Thickness", 0, 99, 30)
insulin = st.slider("Insulin", 0, 846, 120)
bmi = st.slider("BMI", 0.0, 67.1, 32.0)
dpf = st.slider("Diabetes Pedigree Function", 0.0, 2.5, 0.5)
age = st.slider("Age", 21, 81, 35)

# Create input data
input_data = pd.DataFrame([{
    'Pregnancies': pregnancies,
    'Glucose': glucose,
    'BloodPressure': blood_pressure,
    'SkinThickness': skin_thickness,
    'Insulin': insulin,
    'BMI': bmi,
    'DiabetesPedigreeFunction': dpf,
    'Age': age
}])

# Predict button
if st.button("🔍 Predict"):
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]
    result = "🧬 **Diabetic**" if prediction[0] == 1 else "✅ **Not Diabetic**"
    st.markdown(f"### Prediction: {result}")
    st.markdown(f"**Confidence Score**: `{probability:.2f}`")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit & Scikit-learn")
