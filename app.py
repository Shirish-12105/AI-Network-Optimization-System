import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Load Models Safely
# -------------------------------

try:
    rf_model = joblib.load("rf_model.pkl")
    rf_available = True
except:
    rf_available = False

nn_model = joblib.load("nn_model.pkl")
scaler_X = joblib.load("scaler_X.pkl")
scaler_y = joblib.load("scaler_y.pkl")

# -------------------------------
# UI
# -------------------------------

st.title("🚀 AI Network Optimization System")
st.write("Predict latency & optimize bandwidth using AI")

# Inputs
users = st.number_input("Number of Users", min_value=1, value=50)
bandwidth = st.number_input("Bandwidth", min_value=1, value=100)
packet_loss = st.number_input("Packet Loss (%)", min_value=0.0, value=1.0)

# -------------------------------
# Prediction
# -------------------------------

if st.button("Predict"):

    input_data = np.array([[users, bandwidth, packet_loss]])
    input_scaled = scaler_X.transform(input_data)

    st.subheader("📊 Model Predictions")

    # RF
    if rf_available:
        rf_pred_scaled = rf_model.predict(input_scaled)
        rf_pred = scaler_y.inverse_transform(rf_pred_scaled.reshape(-1,1))[0][0]
        st.success(f"RF Latency: {rf_pred:.2f}")
    else:
        rf_pred = None
        st.warning("RF model not available")

    # NN
    nn_pred_scaled = nn_model.predict(input_scaled)
    nn_pred = scaler_y.inverse_transform(nn_pred_scaled.reshape(-1,1))[0][0]
    st.success(f"NN Latency: {nn_pred:.2f}")

    # -------------------------------
    # Comparison Graph
    # -------------------------------

    st.subheader("📈 Model Comparison")

    labels = []
    values = []

    if rf_pred is not None:
        labels.append("Random Forest")
        values.append(rf_pred)

    labels.append("Neural Network")
    values.append(nn_pred)

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_ylabel("Latency")
    ax.set_title("Model Comparison")

    st.pyplot(fig)

    # -------------------------------
    # Optimal Bandwidth Graph
    # -------------------------------

    st.subheader("⚡ Bandwidth Optimization Graph")

    bw_range = list(range(10, 500, 10))
    latencies = []

    for bw in bw_range:
        temp_input = np.array([[users, bw, packet_loss]])
        temp_scaled = scaler_X.transform(temp_input)

        pred_scaled = nn_model.predict(temp_scaled)
        pred_latency = scaler_y.inverse_transform(pred_scaled.reshape(-1,1))[0][0]

        latencies.append(pred_latency)

    # Find best
    min_latency = min(latencies)
    optimal_bw = bw_range[latencies.index(min_latency)]

    # Plot graph
    fig2, ax2 = plt.subplots()
    ax2.plot(bw_range, latencies)
    ax2.set_xlabel("Bandwidth")
    ax2.set_ylabel("Latency")
    ax2.set_title("Bandwidth vs Latency")

    st.pyplot(fig2)

    # Result
    st.subheader("✅ Final Result")
    st.success(f"Optimal Bandwidth: {optimal_bw}")
    st.info(f"Minimum Latency: {min_latency:.2f}")
