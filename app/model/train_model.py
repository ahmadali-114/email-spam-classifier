import pandas as pd
import re
import nltk
import os
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Download required NLTK resources
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Resolve path to dataset
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'spam.csv')

# Load dataset with correct column names
df = pd.read_csv(DATA_PATH, encoding='latin-1')[['Category', 'Message']]
df.columns = ['label', 'text']  # Rename for simplicity
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Preprocess text
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    words = [lemmatizer.lemmatize(w) for w in words if w not in stop_words]
    return ' '.join(words)

df['text'] = df['text'].apply(preprocess)

# Train-test split
X = df['text']
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build and train model
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('nb', MultinomialNB())
])
model.fit(X_train, y_train)

# Save the model
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'spam_model.pkl')
joblib.dump(model, MODEL_PATH)

print(f"✅ Model trained and saved to: {MODEL_PATH}")
