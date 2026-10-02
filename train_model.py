import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

DATA_PATH = "data/SMSSpamCollection"

# Load dataset
data = pd.read_csv(
    DATA_PATH,
    sep="\t",
    header=None,
    names=["label", "message"]
)

print("Dataset loaded successfully!")
print("Total messages:", len(data))

# Convert labels
data["label"] = data["label"].map({
    "ham": 0,
    "spam": 1
})

X = data["message"]
y = data["label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# TF-IDF
vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english"
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train Naive Bayes model
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Test model
y_pred = model.predict(X_test_tfidf)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel trained successfully!")
print("Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=["Not Spam", "Spam"]
))

# Create model folder
os.makedirs("model", exist_ok=True)

# Save model
joblib.dump(
    model,
    "model/spam_classifier.pkl"
)

# Save vectorizer
joblib.dump(
    vectorizer,
    "model/tfidf_vectorizer.pkl"
)

# Save accuracy
with open("model/accuracy.txt", "w") as file:
    file.write(str(round(accuracy * 100, 2)))

print("\nModel saved successfully!")
print("Files created:")
print("- model/spam_classifier.pkl")
print("- model/tfidf_vectorizer.pkl")
print("- model/accuracy.txt")