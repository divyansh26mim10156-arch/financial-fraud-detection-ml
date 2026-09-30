# Financial Transaction Fraud Detection System

An enterprise-grade, modular Python command-line application designed to classify financial transactions as legitimate or fraudulent using machine learning algorithms. Built strictly according to modular architecture and clean code standards.

---

## Features
* **Modular Architecture:** Separated into 7 distinct classes/modules (Data Loading, Preprocessing, Model Training, Evaluation, Custom Exceptions, and Logging).
* **Supervised Machine Learning:** Implements a tuned Random Forest Classifier optimized for tabular financial data.
* **Robust Error Handling:** Custom exception framework (`FraudDetectionException`, `DataLoadingError`, `ModelTrainingError`) preventing unexpected application crashes.
* **Execution Logging:** Comprehensive tracking of operational milestones and anomalies via `logs/system.log`.

---

## Technologies Used
* **Python 3.x**
* **Scikit-Learn** (Classification, Scaler, Metrics)
* **Pandas & NumPy** (Data manipulation and matrix handling)
* **Joblib** (Model serialization support)

---
## Dataset Download & Setup

Due to GitHub's file size limits, the `creditcard.csv` dataset is not included in this repository. 

**Follow these exact steps to run the project:**
1. Download the official "Credit Card Fraud Detection" dataset from Kaggle:
   [🔗 Download Dataset Here](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
2. Extract the downloaded `.zip` file.
3. Rename the extracted file to `creditcard_sample.csv`.
4. Place `creditcard_sample.csv` directly into the root directory of this cloned repository (the exact same folder containing `main.py`).

---
## Installation & Setup

1. Clone or download this repository into your local directory.
2. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
