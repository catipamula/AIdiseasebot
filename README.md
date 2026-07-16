

# 🚀 AI Disease Prediction Chatbot (Django + Hugging Face)

An AI-powered medical chatbot built using **Django** and **HUgging Face (LLM)** that predicts possible diseases based on user symptoms and provides intelligent health suggestions.

---

## 📌 Features

* 🤖 Hugging Face powered chatbot
* 🧠 Symptom-based disease prediction
* 💬 Real-time conversational interface
* ⚡ Django-based backend
* 🌐 Responsive and clean UI
* 🔐 Secure API integration

---

## 🛠️ Tech Stack

| Layer    | Technology                                       |
| -------- | -------------------------------------------------|
| Frontend | HTML, CSS, JavaScript                            |
| Backend  | Django (Python)                                  |
| AI Model | meta-llama/Llama-3.1-8B-Instruct(Hugging face )  |
| Database | MySQL                                            |
  

---

## 🧠 Architecture Explanation

### 1️⃣ User Layer

* User interacts with the chatbot interface
* Inputs symptoms as text

### 2️⃣ Frontend Layer

* Built using HTML, CSS, JavaScript
* Sends HTTP requests to the Django backend

### 3️⃣ Backend (Django)

* Handles routing and business logic
* Performs **prompt engineering**
* Communicates with meta-llama/Llama-3.1-8B-Instruct

### 4️⃣ AI Layer (Huggingface)

* Processes symptoms using NLP
* Generates:

  * Disease prediction
  * Explanation
  * Precautions

### 5️⃣ Database Layer

* SQLite database
* Stores user data and chat history (optional)

---

## 📸 Output Screenshots

### ⚙️ Backend / Terminal

![Backend Screenshot](/outputshots/cmdshot.png)


### 🔐 Login Page

![Login](/outputshots/login.png)

### 💬 Chat Interface

![Chat Page](/outputshots/chatpage.png)


### 🧠 Prediction Output - 1

![Prediction 1](/outputshots/botprediction.png)

### 🧠 Prediction Output - 2

![Prediction 2](/outputshots/botprediction2.png)

---

## ⚙️ Setup Instructions

```bash
# Clone repository
git clone https://github.com/catipamula/AIdiseasebot.git
cd AIdiseasebot

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
daphne symptom_checker.asgi:application 🧠
```
