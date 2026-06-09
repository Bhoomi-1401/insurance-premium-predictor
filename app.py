import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🏥 Insurance Premium Predictor")
st.subheader("Find out your premium category!")

# Input fields
age = st.slider("Age", 18, 64, 30)
sex = st.selectbox("Sex", ["Male", "Female"])
bmi = st.slider("BMI", 15.0, 55.0, 30.0)
children = st.slider("Number of Children", 0, 5, 0)
smoker = st.selectbox("Smoker?", ["Yes", "No"])
region = st.selectbox("Region", ["Northeast", "Northwest", "Southeast", "Southwest"])

# Encode inputs
sex = 1 if sex == "Male" else 0
smoker_val = 1 if smoker == "Yes" else 0
smoker_obese = 1 if (smoker == "Yes" and bmi >= 30) else 0

region_northeast = 1 if region == "Northeast" else 0
region_northwest = 1 if region == "Northwest" else 0
region_southeast = 1 if region == "Southeast" else 0
region_southwest = 1 if region == "Southwest" else 0

# Predict
if st.button("Predict Premium Category"):
    input_data = np.array([[age, sex, bmi, children, smoker_val,
                            smoker_obese, region_northeast,
                            region_northwest, region_southeast,
                            region_northwest]])
    
    prediction = model.predict(input_data)[0]
    mapping = {0: "High 🔴", 1: "Low 🟢", 2: "Medium 🟡"}
    result = mapping[prediction]
    st.success(f"Your Premium Category is: **{result}**")