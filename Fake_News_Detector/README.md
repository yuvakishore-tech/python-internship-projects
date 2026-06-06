# Fake News Detector using Machine Learning

## Project Overview

Fake News Detector is a Machine Learning and Natural Language Processing based Python project designed to classify news headlines as REAL or FAKE. The application uses TF-IDF vectorization and a Multinomial Naive Bayes classification model to analyze textual patterns and predict news authenticity.

The project demonstrates practical implementation of:

* Text preprocessing
* Natural Language Processing
* Machine Learning model training
* Classification analysis
* Model serialization
* Streamlit web application development

---

## Features

* Detect fake and real news headlines
* Single headline prediction
* Confidence score generation
* Batch CSV prediction support
* Download prediction results as CSV
* TF-IDF text preprocessing
* Machine Learning model training and evaluation
* Streamlit-based graphical interface
* Evaluation report generation

---

## Technologies Used

| Technology        | Purpose                   |
| ----------------- | ------------------------- |
| Python            | Programming Language      |
| Pandas            | Data Processing           |
| Scikit-learn      | Machine Learning          |
| TF-IDF Vectorizer | Text Feature Extraction   |
| Streamlit         | Web Application Interface |
| Joblib            | Model Saving and Loading  |

---

## Project Structure

```text
Fake_News_Detector/

│
├── data/
│   └── news_dataset.csv
│
├── models/
│   ├── fake_news_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── reports/
│   └── evaluation_report.txt
│
├── train_model.py
├── app.py
├── README.md
└── requirements.txt
```

---

## Installation

Install the required libraries before running the project.

```bash
pip install -r requirements.txt
```

OR

```bash
pip install pandas scikit-learn streamlit joblib
```

---

## How to Run

### Step 1 - Train the Model

Run:

```bash
python train_model.py
```

This generates:

* Trained Machine Learning model
* TF-IDF vectorizer
* Evaluation report

---

### Step 2 - Launch Streamlit Application

Run:

```bash
python -m streamlit run app.py
```

The application will open automatically in the browser.

---

## Input Dataset

The project uses a CSV dataset containing:

* News headlines
* Classification labels

Example Dataset:

```csv
text,label
"Government launches healthcare reform program",REAL
"Aliens secretly controlling world governments",FAKE
```

---

## Core Functionalities

### Text Preprocessing

The system preprocesses textual data using:

* Lowercasing
* Tokenization
* TF-IDF Vectorization
* Stop-word removal

---

### TF-IDF Feature Extraction

TF-IDF converts text data into numerical vectors that help the Machine Learning model identify important word patterns.

---

### Machine Learning Classification

The project uses:

* Multinomial Naive Bayes

for classifying news headlines into:

* REAL
* FAKE

---

### Batch Prediction

Users can upload CSV files containing multiple news headlines for large-scale prediction analysis.

---

## Generated Outputs

### Trained Model

```text
models/fake_news_model.pkl
```

Stores the trained Machine Learning model.

---

### TF-IDF Vectorizer

```text
models/tfidf_vectorizer.pkl
```

Stores the text vectorization model.

---

### Evaluation Report

```text
reports/evaluation_report.txt
```

Contains:

* Accuracy score
* Precision
* Recall
* F1-score

---

## Model Workflow

### Step 1 - Dataset Loading

Dataset is loaded using Pandas.

### Step 2 - Text Vectorization

TF-IDF converts headlines into numerical vectors.

### Step 3 - Dataset Splitting

Dataset is divided into:

* Training data
* Testing data

### Step 4 - Model Training

Multinomial Naive Bayes model is trained on processed text data.

### Step 5 - Prediction

The model predicts whether the input headline is:

* REAL
* FAKE

### Step 6 - Evaluation

Accuracy and classification reports are generated for performance analysis.

---

## Streamlit Application Features

### Single Headline Prediction

Users can:

* Enter a news headline
* Predict authenticity
* View confidence score

---

### CSV Upload Prediction

Users can:

* Upload CSV files
* Predict multiple headlines
* Download prediction results

---

## Model Accuracy

The project achieves approximately:

```text
80% to 90% accuracy
```

depending on dataset size and training configuration.

---

## Learning Outcomes

This project demonstrates:

* Natural Language Processing
* Text Classification
* Machine Learning workflow
* TF-IDF feature extraction
* Streamlit web application development
* Model serialization using Joblib
* Batch prediction handling
* Git and GitHub project management

---

## License

This project is intended for educational and learning purposes.
