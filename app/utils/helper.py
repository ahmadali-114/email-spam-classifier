import os
import joblib
from app.utils.preprocessing import preprocess

# Path to the trained model file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'spam_model.pkl')

# Load the model once at startup
model = joblib.load(MODEL_PATH)

def classify_message(message):
    """
    Predict whether a message is spam or not.

    Returns:
        label (str): 'Spam' or 'Not Spam'
        probability (float): Prediction confidence
    """
    cleaned_text = preprocess(message)
    prediction = model.predict([cleaned_text])[0]
    probability = model.predict_proba([cleaned_text])[0][prediction]
    
    label = "Spam" if prediction == 1 else "Not Spam"
    return label, round(probability * 100, 2)
