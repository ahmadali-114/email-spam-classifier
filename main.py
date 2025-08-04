import streamlit as st
from app.utils.helper import classify_message

# Custom CSS for modern look
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        max-width: 700px;
        margin: auto;
    }
    .result-box {
        padding: 20px;
        border-radius: 8px;
        margin-top: 20px;
        font-weight: bold;
        font-size: 20px;
    }
    .spam {
        background-color: #ffe6e6;
        color: #b30000;
    }
    .not-spam {
        background-color: #e6ffed;
        color: #006600;
    }
    </style>
""", unsafe_allow_html=True)

# Session state for input
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# App layout
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.markdown("## 📧 Email Spam Classifier")
st.markdown("Predict whether an email message is **Spam** or **Not Spam** using a machine learning model.")

# Input form
with st.form(key="spam_form"):
    user_input = st.text_area("🔍 Enter your message:", value=st.session_state.user_input, height=200)
    col1, col2 = st.columns([1, 1])
    with col1:
        submitted = st.form_submit_button("🚀 Classify")
    with col2:
        clear = st.form_submit_button("🧹 Clear")

    if submitted and user_input.strip() != "":
        st.session_state.user_input = user_input
        label, confidence = classify_message(user_input)
        result_class = "spam" if label == "Spam" else "not-spam"
        st.markdown(
            f"<div class='result-box {result_class}'>"
            f"Result: {label}<br>Confidence: {confidence}%</div>",
            unsafe_allow_html=True
        )

    if clear:
        st.session_state.user_input = ""
        st.experimental_rerun()

# Footer
st.markdown("---")
st.markdown(
    "Made with ❤️ by Ahmad Ali • "
    "[GitHub](https://github.com/ahmadali-114) | "
    "[LinkedIn](https://www.linkedin.com/in/ahmad-ali-473510234) | "
    "[WhatsApp](https://wa.me/message/LOBQZQGKQEK5K1)",
    unsafe_allow_html=True
)
st.markdown("</div>", unsafe_allow_html=True)
