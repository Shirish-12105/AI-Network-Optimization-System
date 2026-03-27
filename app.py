import streamlit as st

# Title
st.set_page_config(page_title="AI Network Optimization", layout="centered")
st.title("🚀 AI Network Optimization System")

st.markdown("### Enter Network Parameters")

# Inputs
users = st.number_input("👥 Number of Users", min_value=1, value=50)
bandwidth = st.number_input("📶 Bandwidth (Mbps)", min_value=1, value=100)
packet_loss = st.number_input("📉 Packet Loss (%)", min_value=0.0, max_value=100.0, value=1.0)

# Button
if st.button("⚡ Optimize Network"):
    
    # Simple optimization logic (temporary)
    optimized_score = (users * bandwidth) / (1 + packet_loss)

    # Output
    st.success(f"✅ Optimized Network Score: {optimized_score:.2f}")

    # Extra insights
    if packet_loss > 5:
        st.warning("⚠️ High packet loss detected! Consider improving network stability.")
    
    if bandwidth < 50:
        st.info("ℹ️ Low bandwidth. Increasing bandwidth may improve performance.")

# Footer
st.markdown("---")
st.caption("Built using Streamlit | AI Network Optimization Project")
