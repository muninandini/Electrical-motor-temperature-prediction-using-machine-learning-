import streamlit as st
import pickle
import pandas as pd
import os

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Motor Temperature Predictor",
    page_icon="⚡",
    layout="wide"
)

# ================= LOAD MODEL =================
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
model_path = os.path.join(BASE_DIR, "model", "best_motor_model.pkl")
model = pickle.load(open(model_path, "rb"))

# ================= SESSION =================
if "page" not in st.session_state:
    st.session_state.page = "form"

# ================= SIDEBAR =================
st.sidebar.title("Dashboard")
st.sidebar.markdown("### Navigation")

if st.sidebar.button("🏠 Home"):
    st.session_state.page = "form"
    st.rerun()

if st.sidebar.button("📊 Result"):
    if "prediction" in st.session_state:
        st.session_state.page = "result"
        st.rerun()

st.sidebar.markdown("---")
st.sidebar.info("ML Model: Random Forest")

# ======================================================
# 🟦 HOME PAGE — FORM
# ======================================================

if st.session_state.page == "form":

    st.markdown(
        "<h1 style='text-align:center;'>⚡ Electric Motor Temperature Prediction</h1>",
        unsafe_allow_html=True
    )

    st.markdown("## 🔧 Enter Motor Parameters")

    col1, col2, col3 = st.columns(3)

    with col1:
        u_q = st.number_input("u_q")
        coolant = st.number_input("Coolant")
        stator_winding = st.number_input("Stator Winding")
        u_d = st.number_input("u_d")

    with col2:
        stator_tooth = st.number_input("Stator Tooth")
        motor_speed = st.number_input("Motor Speed")
        i_d = st.number_input("i_d")
        i_q = st.number_input("i_q")

    with col3:
        stator_yoke = st.number_input("Stator Yoke")
        ambient = st.number_input("Ambient")
        torque = st.number_input("Torque")   # ✅ ADDED

    if st.button("🚀 Predict Temperature", use_container_width=True):

        input_data = [[
            u_q, coolant, stator_winding, u_d,
            stator_tooth, motor_speed, i_d, i_q,
            stator_yoke, ambient, torque   # ✅ NOW 11 FEATURES
        ]]

        prediction = model.predict(input_data)[0]

        st.session_state.prediction = prediction
        st.session_state.inputs = input_data
        st.session_state.page = "result"
        st.rerun()

# ======================================================
# 🟩 RESULT PAGE
# ======================================================

elif st.session_state.page == "result":

    st.markdown(
        "<h1 style='text-align:center;'>🌡️ Prediction Result</h1>",
        unsafe_allow_html=True
    )

    prediction = st.session_state.prediction
    inputs = st.session_state.inputs[0]

    st.markdown(
        f"<h2 style='text-align:center;color:#ff4b4b;'> {prediction:.2f} °C </h2>",
        unsafe_allow_html=True
    )

    if prediction < 60:
        st.success("✅ Status: Normal")
    elif prediction < 80:
        st.warning("⚠️ Status: Warm")
    else:
        st.error("🔥 Status: Overheating Risk")

    st.markdown("---")

    report = pd.DataFrame({
        "u_q": [inputs[0]],
        "coolant": [inputs[1]],
        "stator_winding": [inputs[2]],
        "u_d": [inputs[3]],
        "stator_tooth": [inputs[4]],
        "motor_speed": [inputs[5]],
        "i_d": [inputs[6]],
        "i_q": [inputs[7]],
        "stator_yoke": [inputs[8]],
        "ambient": [inputs[9]],
        "torque": [inputs[10]],
        "Predicted Temperature": [prediction]
    })

    csv = report.to_csv(index=False).encode("utf-8")

    colA, colB = st.columns(2)

    with colA:
        st.download_button(
            "📥 Download Report",
            csv,
            "motor_temperature_report.csv",
            "text/csv",
            use_container_width=True
        )

    with colB:
        if st.button("🔄 New Prediction", use_container_width=True):
            st.session_state.page = "form"
            st.rerun()
