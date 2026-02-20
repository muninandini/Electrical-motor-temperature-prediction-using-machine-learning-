# ⚡ Electric Motor Temperature Prediction using Machine Learning

## 📌 Project Overview

This project predicts the temperature of an electric motor using Machine Learning algorithms based on various motor operating parameters.

The system helps in monitoring motor health and preventing overheating by providing accurate temperature predictions through a web application.

---

## 🎯 Objectives

- Predict motor temperature using sensor data
- Compare multiple Machine Learning models
- Select the best-performing model
- Deploy a user-friendly web application
- Generate downloadable prediction reports

---

## 📊 Dataset Description

The dataset contains motor operational parameters:

| Feature | Description |
|--------|------------|
| u_q | Quadrature voltage |
| coolant | Coolant temperature |
| stator_winding | Stator winding temperature |
| u_d | Direct voltage |
| stator_tooth | Stator tooth temperature |
| motor_speed | Motor speed |
| i_d | Direct current |
| i_q | Quadrature current |
| pm | Permanent magnet temperature |
| stator_yoke | Stator yoke temperature |
| ambient | Ambient temperature |
| torque | Motor torque |
| profile_id | Profile identifier |

---

## 🤖 Machine Learning Models Used

The following models were trained and evaluated:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor ⭐ (Best Model)
- Support Vector Machine (SVM)

### 🏆 Best Model: Random Forest

Performance Metrics:

- R² Score: 0.9763
- RMSE: 2.9269

---

## 🧠 Methodology

1. Data preprocessing
2. Feature selection
3. Train-test split
4. Model training
5. Model evaluation
6. Best model selection
7. Model saving using Pickle
8. Web application deployment

---

## 🌐 Web Application (Streamlit)

A professional interactive web application was developed using Streamlit.

### 🔹 Features

- Clean input form for motor parameters
- Temperature prediction
- Result displayed on a new screen
- Status indicator (Normal / Warm / Overheating)
- Downloadable prediction report (CSV)
- Multiple predictions support
- Dashboard-style interface

---

## 🛠️ Technologies Used

- Python
- Scikit-learn
- Pandas
- NumPy
- Streamlit
- Pickle

---
## 📁 Project Structure
- electric-motor-temperature-prediction/
  - app/app.py
  - model/best_motor_model.pkl
  - train_model.py
  - requirements.txt
  - README.md
  - .gitignore


---

## 🚀 How to Run Locally

### 1️⃣ Install Dependencies

pip install -r requirements.txt

### 2️⃣ Run Application
streamlit run app/app.py


