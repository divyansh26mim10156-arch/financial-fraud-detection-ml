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

## Installation & Setup

1. Clone or download this repository into your local directory.
2. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt