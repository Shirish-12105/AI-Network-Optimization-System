import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="AI Network Optimization", layout="centered")

# Title
st.title("🚀 AI Network Optimization System")
st.markdown("### Enter Network Parameters")

# Inputs
users = st.number_input("👥 Number of Users", min_value=1, value=50)
bandwidth = st.number_input("📶 Bandwidth (Mbps)", min_value=1, value=100)
packet_loss = st.number_input("📉 Packet Loss (%)", min_value=0.0, max_value=100.0, value=1.0)

# Button
if st.button("⚡ Optimize Network"):

    # Simple logic
    optimized_score = (users * bandwidth) / (1 + packet_loss)

    # Result
    st.success(f"✅ Optimized Network Score: {optimized_score:.2f}")

    # Show inputs
    st.subheader("📊 Network Insights")
    st.write(f"Users: {users}")
    st.write(f"Bandwidth: {bandwidth} Mbps")
    st.write(f"Packet Loss: {packet_loss}%")

    # Graph
    data = pd.DataFrame({
        "Metric": ["Users", "Bandwidth", "Packet Loss"],
        "Value": [users, bandwidth, packet_loss]
    })

    st.bar_chart(data.set_index("Metric"))

    # Smart recommendations
    st.subheader("🧠 Recommendations")

    if packet_loss > 2:
        st.error("❌ High packet loss! Improve connection quality.")

    elif bandwidth < 50:
        st.warning("⚠️ Low bandwidth. Consider upgrading.")

    else:
        st.success("✅ Network is performing well!")

# Footer
st.markdown("---")
st.caption("Built using Streamlit | AI Network Optimization Project")
