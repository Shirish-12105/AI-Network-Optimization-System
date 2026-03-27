import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# ---------------- PAGE SETUP ----------------
st.set_page_config(page_title="AI Network Optimization", layout="centered")

st.title("🚀 AI Network Optimization System")
st.markdown("Optimize network performance using Machine Learning")

# ---------------- LOAD DATA ----------------
try:
    df = pd.read_csv("network_data.csv")  # make sure this file is in repo
    st.success("✅ Dataset loaded successfully")

    st.subheader("📂 Dataset Preview")
    st.dataframe(df.head())

except:
    st.warning("⚠️ Dataset not found. Using sample data instead.")

    df = pd.DataFrame({
        "users": [10, 20, 30, 40, 50, 60, 70],
        "bandwidth": [50, 60, 70, 80, 90, 100, 110],
        "packet_loss": [1, 2, 1.5, 2.5, 1, 3, 2],
        "score": [500, 800, 1200, 1500, 2000, 2300, 2600]
    })

# ---------------- TRAIN MODEL ----------------
X = df[["users", "bandwidth", "packet_loss"]]
y = df["score"]

model = LinearRegression()
model.fit(X, y)

# ---------------- INPUT SECTION ----------------
st.subheader("📊 Enter Network Parameters")

users = st.number_input("👥 Number of Users", min_value=1, value=50)
bandwidth = st.number_input("📶 Bandwidth (Mbps)", min_value=1, value=100)
packet_loss = st.number_input("📉 Packet Loss (%)", min_value=0.0, max_value=100.0, value=1.0)

# ---------------- BUTTON ----------------
if st.button("⚡ Optimize Network"):

    # Prediction
    input_data = np.array([[users, bandwidth, packet_loss]])
    prediction = model.predict(input_data)[0]

    # Result
    st.success(f"✅ Predicted Network Score: {prediction:.2f}")

    # ---------------- PERFORMANCE ----------------
    st.subheader("📈 Performance Status")

    if prediction > 2000:
        st.success("🚀 Excellent Performance")
    elif prediction > 1000:
        st.warning("⚠️ Average Performance")
    else:
        st.error("❌ Poor Performance")

    # ---------------- GRAPH ----------------
    st.subheader("📊 Network Insights")

    chart_data = pd.DataFrame({
        "Metric": ["Users", "Bandwidth", "Packet Loss"],
        "Value": [users, bandwidth, packet_loss]
    })

    st.bar_chart(chart_data.set_index("Metric"))

    # ---------------- RECOMMENDATIONS ----------------
    st.subheader("🧠 AI Recommendations")

    if packet_loss > 2:
        st.error("❌ High packet loss! Improve network stability.")

    if bandwidth < 50:
        st.warning("⚠️ Increase bandwidth for better performance.")

    if users > 80:
        st.info("ℹ️ Too many users. Consider load balancing.")

    if packet_loss <= 2 and bandwidth >= 50:
        st.success("✅ Network conditions look good!")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("AI Network Optimization System | Built with Streamlit & ML")