import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Simple dataset
data = {
    "text": [
        "Win money now", "Free offer available", "Click this link",
        "Hello friend", "Let's meet tomorrow", "How are you"
    ],
    "label": [1, 1, 1, 0, 0, 0]  # 1 = spam, 0 = not spam
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])

model = LogisticRegression()
model.fit(X, df["label"])

# Save model & vectorizer
joblib.dump(model, "spam_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model trained and saved!")