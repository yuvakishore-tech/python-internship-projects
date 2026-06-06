import os
import streamlit as st
import pandas as pd
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Model paths
model_path = os.path.join(
    BASE_DIR,
    "models",
    "fake_news_model.pkl"
)

vectorizer_path = os.path.join(
    BASE_DIR,
    "models",
    "tfidf_vectorizer.pkl"
)

# Load model and vectorizer
model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# App title
st.title("Fake News Detector")

# Single prediction section
st.header("Single Headline Prediction")

headline = st.text_input("Enter News Headline")

if st.button("Predict"):

    if headline.strip() == "":
        st.warning("Please enter a news headline")

    else:
        # Convert text to vector
        vector = vectorizer.transform([headline])

        # Predict
        prediction = model.predict(vector)[0]

        # Confidence
        confidence = model.predict_proba(vector).max() * 100

        # Display result
        st.subheader("Prediction Result")

        st.success(f"Prediction: {prediction}")

        st.write(f"Confidence: {confidence:.2f}%")

# Divider
st.divider()

# Batch prediction section
st.header("Batch CSV Upload")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    # Read CSV
    batch_df = pd.read_csv(uploaded_file)

    # Check required column
    if "text" not in batch_df.columns:
        st.error("CSV file must contain a 'text' column")

    else:
        # Convert headlines to vectors
        vectors = vectorizer.transform(batch_df["text"])

        # Predictions
        predictions = model.predict(vectors)

        # Add prediction column
        batch_df["Prediction"] = predictions

        # Display dataframe
        st.dataframe(batch_df)

        # Download results
        csv = batch_df.to_csv(index=False)

        st.download_button(
            "Download Results",
            csv,
            "predictions.csv",
            "text/csv"
        )