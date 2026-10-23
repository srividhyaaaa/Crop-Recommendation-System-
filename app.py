
import streamlit as st

st.set_page_config(
    page_title="Crop Recommendation",
    page_icon="🌱",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background-color: #f3f8f0;
    color: #243b2a;
}

h1, h2, h3, p, label {
    color: #243b2a !important;
}

[data-testid="stMarkdownContainer"] {
    color: #243b2a !important;
}

.stNumberInput label {
    color: #243b2a !important;
}

.stButton button {
    background-color: #287a3d !important;
    color: white !important;
    border-radius: 10px;
    height: 45px;
    width: 100%;
    border: none;
    font-weight: bold;
}

.stButton button p {
    color: white !important;
}

.stButton button:hover {
    background-color: #1c5e2d !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

st.title("🌱 Crop Recommendation System")

st.subheader("Smart farming starts with the right crop.")

st.write(
    "Enter your soil and weather conditions "
    "to find a suitable crop."
)

st.divider()

st.subheader("🌿 Soil Nutrients")

nitrogen = st.number_input(
    "Nitrogen (N)",
    min_value=0.0,
    max_value=200.0,
    value=50.0
)

phosphorus = st.number_input(
    "Phosphorus (P)",
    min_value=0.0,
    max_value=200.0,
    value=50.0
)

potassium = st.number_input(
    "Potassium (K)",
    min_value=0.0,
    max_value=200.0,
    value=50.0
)

st.divider()

st.subheader("🌤️ Weather and Soil Conditions")

temperature = st.number_input(
    "Temperature (°C)",
    min_value=0.0,
    max_value=55.0,
    value=25.0
)

humidity = st.number_input(
    "Humidity (%)",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

ph = st.number_input(
    "Soil pH",
    min_value=0.0,
    max_value=14.0,
    value=6.5
)

rainfall = st.number_input(
    "Rainfall (mm)",
    min_value=0.0,
    max_value=500.0,
    value=100.0
)

st.divider()

st.subheader("🌾 Crop Recommendation")

if st.button("Recommend Suitable Crop", use_container_width=True):
    st.markdown("""
    <div style="
        background-color: #e2f3df;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #b7d9ae;
    ">
        <h3 style="color: #245c35;">
            🌱 Your Recommendation
        </h3>
        <p style="color: #356b43;">
            The crop prediction will appear here
            once the ML model is connected.
        </p>
        <b style="color: #245c35;">
            Status: Awaiting ML Model
        </b>
    </div>
    """, unsafe_allow_html=True)
