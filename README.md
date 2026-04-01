# 🚀 Text Intelligence API

## 📌 Overview

A **multi-model NLP system** that provides real-time text analysis through REST APIs.
The application supports **spam detection, sentiment analysis, and keyword extraction**, designed with a scalable backend architecture.

---

## ✨ Features

* 🔍 Spam Detection using Machine Learning (TF-IDF + Logistic Regression)
* 😊 Sentiment Analysis (lightweight rule-based approach)
* 🏷️ Keyword Extraction from input text
* ⚡ FastAPI-based RESTful endpoints
* 🐳 Dockerized for portable deployment
* ☁️ Cloud-ready (deployed on Render / AWS compatible)

---

## 🛠️ Tech Stack

* **Backend:** Python, FastAPI
* **Machine Learning:** Scikit-learn
* **Containerization:** Docker
* **Deployment:** Cloud (Render / AWS EC2)

---

## 📂 Project Structure

```
text-intelligence-api/
│── app.py              # FastAPI application
│── train.py            # Model training script
│── requirements.txt    # Dependencies
│── Dockerfile          # Container setup
│── spam_model.pkl      # Trained ML model
│── vectorizer.pkl      # TF-IDF vectorizer
```

---

## 🔌 API Endpoints

### 🏠 Health Check

```
GET /
```

---

### 📩 Spam Detection

```
POST /spam
```

**Input:**

```json
"Win free money now"
```

**Output:**

```json
{
  "spam": 1
}
```

---

### 😊 Sentiment Analysis

```
POST /sentiment
```

**Input:**

```json
"I feel great today"
```

**Output:**

```json
{
  "sentiment": "positive"
}
```

---

### 🏷️ Keyword Extraction

```
POST /keywords
```

**Input:**

```json
"AI is transforming the world rapidly"
```

**Output:**

```json
{
  "keywords": ["AI", "is", "transforming"]
}
```

---

## ▶️ Run Locally

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Train model

```
python train.py
```

### 3. Start server

```
uvicorn app:app --reload
```

### 4. Open API docs

```
http://127.0.0.1:8000/docs
```

---

## 🐳 Run with Docker

### Build image

```
docker build -t text-api .
```

### Run container

```
docker run -p 8000:8000 text-api
```

---

## 🌐 Deployment

The application is deployed on cloud platforms and can be accessed publicly:

👉 **Live API:** *(Add your Render link here)*

---

## 🧠 Architecture

```
User Input → FastAPI → ML Model → Response
           ↓
        Docker Container → Cloud Deployment
```

---

## 📈 Future Improvements

* Add deep learning models (BERT, LSTM)
* Improve keyword extraction using NLP libraries
* Add authentication & rate limiting
* Deploy using Kubernetes for scalability

---

## 👩‍💻 Author

**Nitika Chauhan**

* GitHub: https://github.com/nitikachauhann
