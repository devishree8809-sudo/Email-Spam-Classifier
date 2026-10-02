from flask import Flask, render_template, request
import joblib
import csv
import os
from datetime import datetime

app = Flask(__name__)

# Load trained model
model = joblib.load("model/spam_classifier.pkl")

# Load TF-IDF vectorizer
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

HISTORY_FILE = "data/predictions.csv"


# Save prediction to CSV
def save_prediction(message, result, confidence):

    file_exists = (
        os.path.exists(HISTORY_FILE)
        and os.path.getsize(HISTORY_FILE) > 0
    )

    with open(
        HISTORY_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Message",
                "Prediction",
                "Confidence",
                "DateTime"
            ])

        writer.writerow([
            message,
            result,
            f"{confidence}%",
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        ])


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction
@app.route("/predict", methods=["POST"])
def predict():

    message = request.form.get(
        "message",
        ""
    ).strip()

    if not message:
        return render_template(
            "index.html",
            error="Please enter a message."
        )

    # Convert message into TF-IDF
    message_vector = vectorizer.transform([
        message
    ])

    # Predict
    prediction = model.predict(
        message_vector
    )[0]

    # Prediction probability
    probability = model.predict_proba(
        message_vector
    )[0]

    confidence = round(
        max(probability) * 100,
        2
    )

    # Result
    if prediction == 1:
        result = "SPAM"
    else:
        result = "NOT SPAM"

    # Save prediction
    save_prediction(
        message,
        result,
        confidence
    )

    return render_template(
        "index.html",
        message=message,
        result=result,
        confidence=confidence
    )


# Dashboard
@app.route("/dashboard")
def dashboard():

    total = 0
    spam_count = 0
    ham_count = 0

    # Read prediction history
    if os.path.exists(HISTORY_FILE):

        with open(
            HISTORY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for record in reader:

                total += 1

                if record["Prediction"] == "SPAM":
                    spam_count += 1
                else:
                    ham_count += 1

    # Read model accuracy
    accuracy = "N/A"

    accuracy_file = "model/accuracy.txt"

    if os.path.exists(accuracy_file):

        with open(
            accuracy_file,
            "r"
        ) as file:

            accuracy = file.read().strip()

    return render_template(
        "dashboard.html",
        total=total,
        spam_count=spam_count,
        ham_count=ham_count,
        accuracy=accuracy
    )


# History page
@app.route("/history")
def history():

    records = []

    if os.path.exists(HISTORY_FILE):

        with open(
            HISTORY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            records = list(reader)

    # Latest prediction first
    records.reverse()

    return render_template(
        "history.html",
        records=records
    )


# Run Flask
if __name__ == "__main__":
    app.run(debug=True)