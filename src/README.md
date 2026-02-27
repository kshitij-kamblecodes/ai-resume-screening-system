# 🚀 AI Resume Screening System

<p align="center">
  <img src="images/home.png" width="800">
</p>

---

## 📌 Overview

The **AI Resume Screening System** is an NLP-based web application that evaluates resumes against a given job description and generates a semantic match score.

This project simulates a basic **Applicant Tracking System (ATS)** using:

- TF-IDF Vectorization  
- Cosine Similarity  
- Text Preprocessing (NLTK)  
- Streamlit Web Interface  

It allows users to upload resumes and instantly analyze how well they match a job role.

---

## 🎯 Problem Statement

Manual resume screening is:

- Time-consuming  
- Inconsistent  
- Prone to human bias  

This project automates first-level resume filtering by ranking resumes based on textual similarity with job requirements.

---

## 🧠 How It Works

### 1️⃣ Text Preprocessing
- Convert text to lowercase  
- Remove punctuation  
- Remove stopwords  

### 2️⃣ Feature Extraction
- Convert resume & job description into numerical vectors using **TF-IDF**

### 3️⃣ Similarity Calculation
- Calculate semantic similarity using **Cosine Similarity**

### 4️⃣ Match Score
- Generate percentage match score  
- Classify result into:
  - 🟢 Strong Match
  - 🟡 Moderate Match
  - 🔴 Weak Match

---

## 🖥️ Application Interface

### 🟢 Strong Match Example
<p align="center">
  <img src="images/strong_match.png" width="800">
</p>

### 🔴 Weak Match Example
<p align="center">
  <img src="images/weak_match.png" width="800">
</p>

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Scikit-learn  
- NLTK  
- Pandas  
- TF-IDF  
- Cosine Similarity  

---

## 📂 Project Structure

```
resume-screening-ai/
│
├── data/
│   ├── resumes.csv
│   └── job_description.txt
│
├── src/
│   ├── preprocess.py
│   ├── vectorize.py
│   ├── similarity.py
│   ├── main.py
│   └── app.py
│
├── images/
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run Locally

### 1️⃣ Clone Repository

```
git clone https://github.com/kshitij-kamblecodes/ai-resume-screening-system.git
cd ai-resume-screening-system
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run Streamlit App

```
streamlit run src/app.py
```

---

## 📊 Key Features

✔ Resume Upload (TXT format)  
✔ Job Description Input  
✔ Semantic Similarity Score  
✔ Modern Streamlit UI  
✔ Modular Project Architecture  
✔ GitHub Ready  

---

## 📈 Future Improvements

- PDF Resume Upload Support  
- Skill Gap Detection  
- Sentence-BERT Embeddings  
- Multi-Resume Ranking  
- Cloud Deployment  

---

## 👨‍💻 Author

**Kshitij Kamble**  
PG-DAI Student | Machine Learning Enthusiast  

---

## 🎤 Interview Explanation (Short Version)

> Built an NLP-based resume screening system using TF-IDF vectorization and cosine similarity, deployed with a Streamlit interface for real-time resume evaluation.