
import pickle
import pandas as pd
import streamlit as st

# Load the trained model
with open("crop_recommendation_model.pkl", "rb") as f:
    saved = pickle.load(f)

model = saved["model"]
features = saved["features"]

# Page settings
st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌱",
    layout="centered"
)

# Custom styling
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #e8f5e9, #f1f8e9);
}

h1, h2, h3 {
    color: #1b5e20 !important;
}

p {
    color: #263238;
}

label, .stNumberInput label {
    color: #263238 !important;
    font-weight: 600 !important;
}

div.stButton > button {
    background-color: #2e7d32;
    color: white;
    width: 100%;
    border-radius: 8px;
    height: 45px;
    font-weight: bold;
    border: none;
}

div.stButton > button:hover {
    background-color: #1b5e20;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# Header
st.title("🌱 Crop Recommendation System")
st.markdown(
    '<p class="subtitle">Find the most suitable crop for your soil and climate.</p>',
    unsafe_allow_html=True
)

st.divider()

st.subheader("🌾 Enter Soil and Weather Details")

# Input fields displayed vertically
n = st.number_input("Nitrogen (N)", min_value=0.0, max_value=200.0, value=90.0)
p = st.number_input("Phosphorus (P)", min_value=0.0, max_value=200.0, value=42.0)
k = st.number_input("Potassium (K)", min_value=0.0, max_value=250.0, value=43.0)
temperature = st.number_input("Temperature (°C)", min_value=-10.0, max_value=60.0, value=25.5)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=80.0)
ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, value=6.5)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=5000.0, value=200.0)

st.divider()

# Predict crop
if st.button("Recommend Suitable Crop"):
    try:
        input_values = {
            "n": n,
            "p": p,
            "k": k,
            "temperature": temperature,
            "humidity": humidity,
            "ph": ph,
            "rainfall": rainfall
        }

        input_data = pd.DataFrame([input_values])[features]
        prediction = model.predict(input_data)[0]

        st.success("Recommended Crop")
        st.markdown(
            f"<h2 style='text-align:center;color:#1b5e20;'>{prediction.title()}</h2>",
            unsafe_allow_html=True
            )
        st.info("Recommendation generated using the trained machine learning model.")

    except Exception as e:
        st.error(f"Prediction failed: {e}")

st.divider()
