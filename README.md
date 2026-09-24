# Fake News Detection System

[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Flask%20%2F%20Streamlit-red.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An end-to-end machine learning and natural language processing (NLP) application designed to classify news articles as **Real** or **Fake**. This system processes raw text inputs, extracts syntactic and semantic features, and leverages trained classification models to predict authenticity with high confidence.

---

## Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Project Architecture](#project-architecture)
- [Dataset](#dataset)
- [Model Performance](#model-performance)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Overview

Disinformation spreads rapidly across digital media platforms. This project automates the detection of misleading or fabricated news stories using NLP text processing pipelines and supervised classification algorithms. The tool can be used via a clean web interface or as a modular Python package for automated pipelines.

---

## Key Features

- **Robust Text Preprocessing:** Cleans raw text using lowercasing, punctuation/URL removal, tokenization, stop-word elimination, and lemmatization/stemming.
- **Feature Extraction:** Vectorization using TF-IDF (Term Frequency-Inverse Document Frequency) and word n-grams (unigrams + bigrams).
- **Multiple Classifiers Evaluated:** Benchmarked against Passive-Aggressive Classifier, Multinomial Naïve Bayes, Logistic Regression, and Bidirectional LSTM/Transformers.
- **Interactive UI:** Web dashboard built with [Streamlit / Flask] for real-time article verification and prediction probability scores.
- **Explainability:** Highlights key influential terms contributing to the classification verdict.

---

## Project Architecture

Raw News Text
│
▼
[ Text Preprocessing Pipeline ]
├── Regex Noise Cleaning (URLs, Mentions, Punctuation)
├── Tokenization & Stop-Word Removal (NLTK/spaCy)
└── Lemmatization / Stemming
│
▼
[ Feature Engineering ]
└── TF-IDF Vectorization / Word Embeddings
│
▼
[ Model Inference Engine ]
└── Passive-Aggressive / Logistic Regression / BERT
│
▼
[ Final Output: Real vs. Fake (Confidence Score) ]


---

## Dataset

This project is trained and evaluated using standard public fake news benchmarks:
- **Source:** [ISOT Fake News Dataset / Kaggle Fake News Dataset / LIAR Dataset]
- **Size:** ~40,000 labeled articles
- **Classes:** Binary (`1 = Fake`, `0 = Real`)
- **Key Columns:** `title`, `text`, `subject`, `date`, `label`

---

## Model Performance

Cross-validated metrics on the held-out test split (80/20 train-test ratio):

| Model | Accuracy | Precision | Recall | F1-Score |
| :--- | :--- | :--- | :--- | :--- |
| **Passive-Aggressive Classifier** | **94.2%** | **94.0%** | **94.5%** | **94.2%** |
| Logistic Regression | 92.8% | 93.1% | 92.4% | 92.7% |
| Multinomial Naïve Bayes | 89.5% | 88.7% | 90.2% | 89.4% |
| Support Vector Machine (Linear) | 93.6% | 93.4% | 93.9% | 93.6% |

---

## Installation & Setup

### Prerequisites
- Python 3.9 or higher
- Git

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/fake-news-detection.git](https://github.com/yourusername/fake-news-detection.git)
cd fake-news-detection
2. Create and Activate a Virtual Environment
Bash
# On macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# On Windows:
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
Bash
pip install --upgrade pip
pip install -r requirements.txt
4. Download NLP Corpora
Bash
python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt'); nltk.download('wordnet')"
Usage
Run via Command Line / Script
To train the model from scratch:

Bash
python src/train.py --data data/news.csv --model passive_aggressive
To predict a single text snippet via CLI:

Bash
python src/predict.py --text "Breaking: Scientists discover cure for all viruses using orange juice."
Launch the Web Interface
If running a Streamlit frontend:

Bash
streamlit run app.py
If running a Flask application:

Bash
python app.py
Open your browser and navigate to http://127.0.0.1:5000 (or http://localhost:8501).

Project Structure
Plaintext
fake-news-detection/
├── data/
│   ├── raw/                  # Original raw datasets
│   └── processed/            # Cleaned, tokenized text files
├── models/
│   ├── vectorizer.pkl        # Serialized TF-IDF vectorizer
│   └── classifier.pkl        # Saved trained model artifact
├── notebooks/
│   └── exploratory_data_analysis.ipynb
├── src/
│   ├── __init__.py
│   ├── preprocess.py         # Text cleaning and tokenization logic
│   ├── train.py              # Model training and evaluation script
│   └── predict.py            # Inference utilities
├── app.py                    # Web application entry point
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── LICENSE                   # License details
Future Improvements
[ ] Fine-tune domain-specific transformer models (e.g., RoBERTa, DeBERTa, or FakeBERT).

[ ] Add URL metadata and domain-reputation scraping to supplement body text.

[ ] Support multilingual classification (e.g., Hindi, Spanish, French).

[ ] Implement source attribution and fact-checking API integration (e.g., Google Fact Check Tools API).

License
Distributed under the MIT License. See LICENSE for more information.

Author
Your Name - GitHub Profile - LinkedIn Profile


---

### What to customize immediately:
1. **Repository Links & Author:** Update `yourusername` and profile links.
2. **Model Metrics:** Replace the placeholder percentages in the **Model Performance** table with your actual evaluation metrics.
3. **Web Framework:** Keep either Streamlit or Flask in the commands section depending on what you used to build the front end.
