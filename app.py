import streamlit as st

st.set_page_config(page_title="Mumzworld AI Return Classifier", layout="centered")

st.title("🤖 Mumzworld AI Return Reason Classifier")
st.caption("English + Arabic customer support prototype")

st.sidebar.header("📌 Example Inputs")
st.sidebar.write("1. Product arrived damaged")
st.sidebar.write("2. Wrong size baby shoes")
st.sidebar.write("3. Delivery was late")
st.sidebar.write("4. Missing parts in stroller")

text = st.text_area("Customer Message / رسالة العميل", height=150)

def classify_reason(msg):
    msg = msg.lower()

    if "damaged" in msg or "broken" in msg or "defect" in msg:
        return "Refund", "استرداد", 0.95, "Detected damaged product issue."

    elif "wrong size" in msg or "small" in msg or "large" in msg:
        return "Exchange", "استبدال", 0.91, "Detected size mismatch."

    elif "late" in msg or "delay" in msg:
        return "Store Credit", "رصيد متجر", 0.88, "Detected delivery delay."

    elif "missing" in msg or "parts" in msg:
        return "Escalate", "تصعيد", 0.93, "Detected missing parts issue."

    else:
        return "Manual Review", "مراجعة يدوية", 0.75, "Needs human review."

if st.button("🔍 Predict"):
    category, arabic, confidence, reason = classify_reason(text)

    st.success("Prediction Complete ✅")

    st.subheader("Result")
    st.write(f"**English:** {category}")
    st.write(f"**Arabic:** {arabic}")
    st.write(f"**Reason:** {reason}")

    st.progress(confidence)

    st.json({
        "category": category,
        "arabic_category": arabic,
        "confidence": confidence
    })