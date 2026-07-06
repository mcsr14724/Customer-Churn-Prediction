# 🚀 Customer Churn Prediction using Artificial Neural Network (ANN)

An end-to-end Machine Learning project that predicts customer churn using an Artificial Neural Network (ANN) built with TensorFlow/Keras. The project includes data preprocessing, feature engineering, model training, TensorBoard visualization, model serialization, and an application for making predictions on new customer data.

---

## 📖 Project Overview

Customer churn prediction helps businesses identify customers who are likely to leave their services. By predicting churn in advance, companies can take proactive measures to improve customer retention.

This project implements an ANN classifier trained on the **Churn Modelling Dataset** and demonstrates the complete machine learning workflow from preprocessing to deployment-ready prediction.

---

## ✨ Features

- Data preprocessing using **ColumnTransformer**
- Feature scaling with **StandardScaler**
- Artificial Neural Network built using **TensorFlow/Keras**
- Binary classification (Churn / No Churn)
- Model serialization using **.keras** and **Pickle**
- TensorBoard visualization
- Prediction application for new customer data

---

## 🛠️ Tech Stack

- Python
- TensorFlow / Keras
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- TensorBoard
- Pickle

---

## 📂 Project Structure

```
Customer-Churn-Prediction/
│
├── app.py
├── ann.keras
├── columntransformer.pkl
├── standardscaler.pkl
├── Churn_Modelling.csv
├── data_processing.ipynb
├── requirements.txt
├── logs/
└── README.md
```

---

## 📊 Dataset

The project uses the **Churn Modelling Dataset** containing customer information such as:

- Credit Score
- Geography
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Has Credit Card
- Is Active Member
- Estimated Salary

**Target Variable**

- `0` → Customer will stay
- `1` → Customer will churn

---

## ⚙️ Data Preprocessing

- Removed unnecessary columns
- One-Hot Encoding of categorical variables
- Feature scaling using StandardScaler
- Train-Test Split
- Saved preprocessing pipeline using Pickle

---

## 🧠 Model Architecture

```
Input Layer
      │
      ▼
Dense Layer (ReLU)
      │
      ▼
Dense Layer (ReLU)
      │
      ▼
Output Layer (Sigmoid)
```

**Loss Function:** Binary Crossentropy

**Optimizer:** Adam

**Evaluation Metric:** Accuracy

---

## 📈 Training

Training progress was monitored using **TensorBoard**.

Launch TensorBoard with:

```bash
tensorboard --logdir logs/fit
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/customer-churn-prediction.git
```

Navigate to the project directory

```bash
cd customer-churn-prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 🔄 Workflow

```
Customer Data
      │
      ▼
ColumnTransformer
      │
      ▼
StandardScaler
      │
      ▼
Artificial Neural Network
      │
      ▼
Prediction
```

---

## 📌 Future Improvements

- Hyperparameter tuning
- Early stopping
- Dropout regularization
- Cross-validation
- Streamlit web interface
- FastAPI deployment
- Docker support
- Cloud deployment (AWS/Render)

---

## 👨‍💻 Author

**MADHASANI CHANDRA SEKHARA REDDY**

---

⭐ If you found this project useful, consider giving it a star!