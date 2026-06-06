import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

# Create folders if not present
os.makedirs("models", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# Load dataset
df = pd.read_csv("data/news_dataset.csv")

# Features and labels
X = df["text"]
y = df["label"]

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(
    stop_words="english"
)

X_vectorized = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Naive Bayes Model
model = MultinomialNB()

# Train model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

# Save model
joblib.dump(
    model,
    "models/fake_news_model.pkl"
)

# Save vectorizer
joblib.dump(
    vectorizer,
    "models/tfidf_vectorizer.pkl"
)

print("Model and vectorizer saved successfully")

# Classification report
report = classification_report(
    y_test,
    y_pred
)

# Save evaluation report
with open(
    "reports/evaluation_report.txt",
    "w"
) as file:

    file.write(
        "Fake News Detection Model Evaluation\n\n"
    )

    file.write(
        f"Accuracy: {round(accuracy * 100, 2)}%\n\n"
    )

    file.write(report)

print("Evaluation report generated")