# Loan Approval Prediction System

A complete end-to-end **Machine Learning project** that predicts whether a loan application will be **approved or rejected** using **Logistic Regression**, enhanced with **GridSearchCV**, and deployed as a **Streamlit web application**.

---

## 📌 Project Overview

Financial institutions receive thousands of loan applications daily. Manually evaluating each application is time-consuming and prone to bias. This project automates the decision-making process by predicting loan approval based on applicant and loan-related features.

The system:

* Trains a **Logistic Regression** model
* Optimizes performance using **GridSearchCV**
* Provides real-time predictions through a **Streamlit web app**
* Is fully deployed on **Streamlit Cloud**

---

## 🧠 Machine Learning Workflow

1. **Data Understanding & Cleaning**
2. **Feature Encoding (Categorical → Numerical)**
3. **Train-Test Split**
4. **Model Training (Logistic Regression)**
5. **Hyperparameter Tuning using GridSearchCV**
6. **Model Evaluation**
7. **Model Serialization (Pickle/Joblib)**
8. **Web App Development using Streamlit**
9. **Deployment on Streamlit Cloud**

---

## 📊 Dataset Description

The dataset contains applicant personal details, financial information, and loan-related attributes.

| Feature Name      | Description                                  |
| ----------------- | -------------------------------------------- |
| Loan_ID           | Unique identifier for each applicant         |
| Gender            | Male / Female                                |
| Married           | Marital status (Yes / No)                    |
| Dependents        | Number of dependents                         |
| Education         | Graduate / Not Graduate                      |
| Self_Employed     | Self-employed status (Yes / No)              |
| ApplicantIncome   | Income of the applicant                      |
| CoapplicantIncome | Income of the co-applicant                   |
| LoanAmount        | Loan amount (in thousands)                   |
| Loan_Amount_Term  | Loan repayment term (in months)              |
| Credit_History    | Credit repayment history (0 / 1)             |
| Property_Area     | Rural / Semiurban / Urban                    |
| Loan_Status       | Target variable (0 = Approved, 1 = Rejected) |

---

## ⚙️ Model Used

### Logistic Regression

Logistic Regression is used because:

* The target variable is **binary**
* It provides **probabilistic outputs**
* It is **interpretable** and efficient

### Hyperparameter Tuning (GridSearchCV)

GridSearchCV was applied to optimize:

* `C` (Regularization strength)
* `penalty` (l1, l2,elasticnet)
* `solver` (lbfgs, liblinear, newton-cg, newton-cholesky, sag, saga)

This helped improve:

* Accuracy
* Generalization performance
* Model stability

---

## 📈 Model Evaluation

The model was evaluated using:

* Accuracy Score
* Confusion Matrix
* Classification Report

The tuned model outperformed the baseline Logistic Regression model.

---

## 🌐 Streamlit Web Application

The Streamlit app allows users to:

* Enter applicant details via UI components
* Submit data for prediction
* Instantly view loan approval status

### Key Streamlit Features Used

* `st.selectbox()` for categorical inputs
* `st.number_input()` for numerical values
* `st.button()` for prediction trigger
* `st.image()` for logo/visuals

---

## 🚀 Deployment

The application is deployed using **Streamlit Cloud**.

Deployment steps:

1. Push project to GitHub
2. Add `requirements.txt`
3. Load trained model using `pickle` or `joblib`
4. Connect repository to Streamlit Cloud
5. Deploy and test

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries:**

  * pandas
  * numpy
  * scikit-learn
  * streamlit
* **Model:** Logistic Regression
* **Hyperparameter Tuning:** GridSearchCV
* **Deployment:** Streamlit Cloud

---

## Live Link - https://nhtsfzmupkdhehidgn2fje.streamlit.app/

## 📂 Project Structure

```
├── app.py                  # Streamlit application
├── model.pkl               # Trained ML model
├── loan_data.csv            # Dataset
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
```

---

## ✅ How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🎯 Future Improvements

* Add more advanced models (Random Forest, XGBoost)
* Handle class imbalance
* Improve UI/UX
* Add probability-based explanations
* Integrate database support

---

## 👨‍💻 Author

**Guhan S**



This project is for educational purposes.
