import streamlit as st
import requests

st.set_page_config(page_title="AI Prescription Verifier", layout="wide")
st.title("💊 AI Prescription Verifier")

# Tabs for two functionalities
tab1, tab2 = st.tabs(["Drug Interaction Checker", "Dosage & Alternatives"])

# Backend URL
BASE_URL = "http://127.0.0.1:8000"

# ---------------- Drug Interaction Checker ----------------
with tab1:
    st.subheader("Check for Drug Interactions")
    prescription_text = st.text_area(
        "Enter prescription medicines (comma-separated):",
        "Paracetamol, Amoxicillin",
        key="interaction_text"
    )

    if st.button("Check Interactions", key="interaction_button"):
        if prescription_text.strip():
            try:
                response = requests.post(f"{BASE_URL}/check_interactions", json={"text": prescription_text})
                if response.status_code == 200:
                    data = response.json()
                    st.success("✅ Results:")
                    for item in data["interactions"]:
                        st.write(item)
                else:
                    st.error("❌ Error contacting backend.")
            except Exception as e:
                st.error(f"❌ Exception: {e}")

# ---------------- Dosage & Alternatives ----------------
with tab2:
    st.subheader("Check Dosage & Alternatives")
    prescription_text2 = st.text_area(
        "Enter prescription medicines (comma-separated):",
        "Paracetamol, Amoxicillin",
        key="dosage_text"
    )
    age = st.number_input(
        "Enter patient age:", min_value=0, max_value=120, value=25, key="age_input"
    )

    if st.button("Check Dosage & Alternatives", key="dosage_button"):
        if prescription_text2.strip():
            try:
                response = requests.post(
                    f"{BASE_URL}/check_dosage_alternatives",
                    json={"text": prescription_text2, "age": age}
                )
                if response.status_code == 200:
                    data = response.json()
                    st.success("✅ Dosage & Alternatives:")
                    for med, info in data["dosage_info"].items():
                        st.write(f"**{med}**: {info['dosage']}, Alternatives: {', '.join(info['alternatives'])}")
                else:
                    st.error("❌ Error contacting backend.")
            except Exception as e:
                st.error(f"❌ Exception: {e}")
