from fastapi import FastAPI
import joblib

app = FastAPI(title="Text Intelligence API")

# Load model
spam_model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.get("/")
def home():
    return {"message": "Text Intelligence API is running"}

# 🔹 Spam Detection
@app.post("/spam")
def detect_spam(text: str):
    X = vectorizer.transform([text])
    pred = spam_model.predict(X)[0]
    return {"spam": int(pred)}

# 🔹 Sentiment Analysis (simple logic)
@app.post("/sentiment")
def sentiment(text: str):
    positive_words = ["good", "great", "happy", "excellent"]
    result = "positive" if any(word in text.lower() for word in positive_words) else "negative"
    return {"sentiment": result}

# 🔹 Keyword Extraction
@app.post("/keywords")
def keywords(text: str):
    words = text.split()
    return {"keywords": words[:3]}