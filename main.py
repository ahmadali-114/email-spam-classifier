import streamlit as st
from app.utils.helper import classify_message
import re

# ========== SETTINGS ==========
SPAM_KEYWORDS = ["free", "win", "winner", "cash", "click", "offer", "buy", "buy now", "congratulations", "urgent"]

# ========== CUSTOM CSS ==========
st.markdown("""
    <style>
    .main {
        background-color: #fdfdfd;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.08);
        max-width: 750px;
        margin: auto;
        font-family: 'Segoe UI', sans-serif;
    }
    .result-box {
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        font-weight: bold;
        font-size: 18px;
    }
    .spam {
        background-color: #ffe6e6;
        color: #b30000;
    }
    .not-spam {
        background-color: #e6ffed;
        color: #006600;
    }
    .highlight {
        background-color: #fffd8c;
        padding: 2px 6px;
        border-radius: 6px;
        font-weight: bold;
    }
    .footer {
        font-size: 14px;
        color: #666;
        text-align: center;
        margin-top: 50px;
        padding-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ========== SESSION INIT ==========
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# ========== HEADER ==========
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.markdown("## 📧 Email Spam Classifier")
st.markdown("Enter a message below and find out whether it's **Spam** or **Not Spam** using a trained machine learning model.")

# ========== FORM ==========
with st.form(key="spam_form"):
    user_input = st.text_area("🔍 Type your message:", value=st.session_state.user_input, height=200)
    classify = st.form_submit_button("🚀 Classify")

    if classify and user_input.strip() != "":
        st.session_state.user_input = user_input
        label, confidence = classify_message(user_input)
        result_class = "spam" if label == "Spam" else "not-spam"

        # Confidence Bar
        st.markdown("### 🔍 Result")
        st.progress(confidence / 100)

        # Highlight spam keywords in text
        highlighted = user_input
        for word in SPAM_KEYWORDS:
            highlighted = re.sub(fr"\b({re.escape(word)})\b", r"<span class='highlight'>\1</span>", highlighted, flags=re.IGNORECASE)

        st.markdown(
            f"<div class='result-box {result_class}'>"
            f"Prediction: {label}<br>Confidence: {confidence}%</div>",
            unsafe_allow_html=True
        )
        st.markdown("#### ✨ Keyword Highlights")
        st.markdown(f"<div style='line-height:1.6'>{highlighted}</div>", unsafe_allow_html=True)

# ========== MODEL INFO ==========
st.markdown("---")
st.markdown("#### ⚙️ Model Info")
st.markdown("""
- **Algorithm:** Multinomial Naive Bayes  
- **Vectorizer:** TF-IDF  
- **Dataset:** Email/SMS Spam Collection  
- **Accuracy:** ~98%
""")

# ========== FOOTER ==========
st.markdown("<div class='footer'>", unsafe_allow_html=True)
st.markdown(
    "Made with ❤️ by Ahmad Ali • "
    "[GitHub](https://github.com/ahmadali-114) | "
    "[LinkedIn](https://www.linkedin.com/in/ahmad-ali-473510234) | "
    "[WhatsApp](https://wa.me/message/LOBQZQGKQEK5K1)",
    unsafe_allow_html=True
)
st.markdown("</div></div>", unsafe_allow_html=True)
