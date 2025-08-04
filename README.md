# 📧 Email Spam Classifier (Streamlit Web App)

This is a modern, user-friendly **Email Spam Classifier** web application built using **Python**, **Streamlit**, and **machine learning**. It detects whether a message is **Spam** or **Not Spam**, highlights spam keywords, and shows confidence levels.

## 🔍 Features

- ✅ Classifies any message as **Spam** or **Not Spam**
- 🎯 Displays **prediction confidence** with a progress bar
- ✨ Highlights common spam keywords
- 🌐 Designed for **global + Pakistan-specific** spam phrases
- 💬 Modern UI built with Streamlit and custom CSS
- 📱 Responsive layout and contact links

## 🧠 Machine Learning Model

- **Algorithm:** Multinomial Naive Bayes
- **Vectorizer:** TF-IDF
- **Dataset:** SMS Spam Collection (UCI ML Repo)
- **Accuracy:** ~98%

## 🚀 How to Run the App Locally

```bash
# 1. Clone the repo
git clone https://github.com/your-username/email-spam-classifier.git
cd email-spam-classifier

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app/main.py
```

## 📁 Project Structure

```
email-spam-classifier/
│
├── app/
│   ├── main.py               ← Streamlit app
│   ├── model/
│   │   ├── spam_model.pkl    ← Trained model
│   │   └── train_model.py    ← Model training script
│   ├── utils/
│   │   ├── helper.py         ← classify_message() function
│   │   └── preprocessing.py  ← text cleaner functions
│   └── data/
│       └── spam.csv          ← Dataset
│
├── requirements.txt
├── README.md
```

## 🌍 Live Demo

🔗 [View the Live App on Streamlit Cloud](https://your-streamlit-url)

## 👨‍💻 Developer Info

Made with ❤️ by **Ahmad Ali**  
- [GitHub](https://github.com/ahmadali-114)  
- [LinkedIn](https://www.linkedin.com/in/ahmad-ali-473510234)  
- [WhatsApp](https://wa.me/message/LOBQZQGKQEK5K1)

---

> 💡 Tip: Add this project to your portfolio or resume to show practical machine learning deployment skills.