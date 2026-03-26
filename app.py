import streamlit as st

st.title("AI Network Optimization System 🚀")

# Inputs
users = st.number_input("Number of Users", min_value=1, value=50)
bandwidth = st.number_input("Bandwidth", min_value=1, value=100)
packet_loss = st.number_input("Packet Loss (%)", min_value=0.0, value=1.0)

# Button
if st.button("Predict"):
    # Simple logic (temporary)
    result = (users * bandwidth) / (1 + packet_loss)
    
    st.success(f"Optimized Network Score: {result:.2f}")

st.title("AI Network Optimization System 🚀")

# Inputs
users = st.number_input("Number of Users", min_value=1, value=50)
bandwidth = st.number_input("Bandwidth", min_value=1, value=100)
packet_loss = st.number_input("Packet Loss (%)", min_value=0.0, value=1.0)

if st.button("Predict"):
    input_data = [[users, bandwidth, packet_loss]]

    # Scale
    input_scaled = scaler_X.transform(input_data)

    # RF prediction
    rf_latency = rf_model.predict(input_data)[0]

    # NN prediction
    nn_scaled = nn_model.predict(input_scaled)
    nn_latency = scaler_y.inverse_transform(nn_scaled.reshape(-1,1))[0][0]

    st.write(f"RF Predicted Latency: {round(rf_latency,2)}")
    st.write(f"NN Predicted Latency: {round(nn_latency,2)}")
