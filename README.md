# 📧 Email Spam Classifier

A Machine Learning based web application that classifies messages as **Spam** or **Not Spam**.

## 🚀 Features

- Spam / Not Spam message classification
- TF-IDF text vectorization
- Multinomial Naive Bayes Machine Learning model
- Prediction confidence percentage
- Prediction history
- Dashboard with statistics
- Spam vs Not Spam chart
- Model accuracy display
- CSV-based prediction storage

## 🛠️ Technologies Used

- Python
- Flask
- Pandas
- Scikit-learn
- Joblib
- HTML
- CSS
- Bootstrap
- Chart.js

## 🤖 Machine Learning

The project uses:

1. **TF-IDF Vectorizer** – Converts text messages into numerical features.
2. **Multinomial Naive Bayes** – Classifies messages as Spam or Not Spam.

## 📊 Dataset

The project uses the **SMS Spam Collection** dataset.

The dataset contains messages labelled as:

- `spam`
- `ham` (Not Spam)

## 📁 Project Structure

```text
Email Spam Classifier/
│
├── data/
│   ├── SMSSpamCollection
│   └── predictions.csv
│
├── model/
│   ├── spam_classifier.pkl
│   ├── tfidf_vectorizer.pkl
│   └── accuracy.txt
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   └── history.html
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md