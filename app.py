import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Load models (cached)
# -------------------------------
@st.cache_resource
def load_models():
    rf_model = joblib.load("rf_model.pkl")
    nn_model = joblib.load("nn_model.pkl")
    scaler_X = joblib.load("scaler_X.pkl")
    scaler_y = joblib.load("scaler_y.pkl")
    return rf_model, nn_model, scaler_X, scaler_y

rf_model, nn_model, scaler_X, scaler_y = load_models()

# -------------------------------
# UI
# -------------------------------
st.set_page_config(page_title="AI Network Optimization", layout="centered")

st.title(" AI Network Optimization System")
st.markdown("Compare Machine Learning and Deep Learning predictions")

# Inputs
col1, col2 = st.columns(2)

with col1:
    users = st.number_input("Users", min_value=1, value=50)

with col2:
    bandwidth = st.number_input("Bandwidth", min_value=1, value=100)

packet_loss = st.slider("Packet Loss (%)", 0.0, 10.0, 1.0)

# -------------------------------
# Predict
# -------------------------------
if st.button("Predict"):

    with st.spinner("Calculating..."):

        input_data = [[users, bandwidth, packet_loss]]
        input_scaled = scaler_X.transform(input_data)

        # RF Prediction
        rf_latency = rf_model.predict(input_data)[0]

        # NN Prediction
        nn_scaled = nn_model.predict(input_scaled, verbose=0)
        nn_latency = scaler_y.inverse_transform(nn_scaled)[0][0]
        nn_latency = max(0, nn_latency)

        # -------------------------------
        # Display Results
        # -------------------------------
        st.subheader("📊 Model Comparison")

        col1, col2 = st.columns(2)

        col1.metric("RF Latency", f"{round(rf_latency,2)} ms")
        col2.metric("NN Latency", f"{round(nn_latency,2)} ms")

        # -------------------------------
        # Graph: Latency vs Bandwidth
        # -------------------------------
        st.subheader("📈 Latency vs Bandwidth")

        bandwidth_range = np.linspace(10, 500, 50)
        rf_vals = []
        nn_vals = []

        for bw in bandwidth_range:
            inp = [[users, bw, packet_loss]]

            rf_vals.append(rf_model.predict(inp)[0])

            inp_scaled = scaler_X.transform(inp)
            nn_pred = nn_model.predict(inp_scaled, verbose=0)
            val = scaler_y.inverse_transform(nn_pred)[0][0]
            nn_vals.append(max(0, val))

        fig, ax = plt.subplots()
        ax.plot(bandwidth_range, rf_vals, label="Random Forest")
        ax.plot(bandwidth_range, nn_vals, label="Neural Network")

        ax.set_xlabel("Bandwidth")
        ax.set_ylabel("Latency")
        ax.set_title("Latency vs Bandwidth")
        ax.legend()

        st.pyplot(fig)
