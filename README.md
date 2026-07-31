# 🏦 Loan Eligibility Prediction System

## 📌 Overview

The **Loan Eligibility Prediction System** is a Machine Learning web application that predicts whether a loan application is likely to be **Approved** or **Rejected** based on the applicant's personal and financial information.

The application is built using **Python**, **Flask**, and **Scikit-learn**, with **SQLite** used for storing prediction history. It also includes an analytics dashboard with interactive charts to help visualize prediction statistics.

This project demonstrates the integration of Machine Learning models into a web application with a user-friendly interface.

---

## 🚀 Features

- Predict loan eligibility using a trained Machine Learning model
- Display loan approval probability
- Store prediction history in SQLite database
- View previous predictions through a history page
- Analytics dashboard with statistics and charts
- Responsive and easy-to-use interface
- About page describing the project

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Joblib

### Backend
- Flask

### Frontend
- HTML5
- CSS3
- JavaScript
- Chart.js

### Database
- SQLite

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```
Loan-Eligibility-Prediction/
│
├── app.py
├── database.py
├── train_model.py
├── requirements.txt
├── README.md
│
├── dataset/
│   └── loan_data.csv
│
├── static/
│   └── style.css
│
├──templates/
   ├── index.html
   ├── result.html
   ├── history.html
   └── about.html
```

---

## ⚙️ How It Works

1. The user enters loan applicant details through the web form.
2. Flask receives the input data.
3. The data is converted into the required format using Pandas.
4. The trained Machine Learning model predicts whether the loan will be approved or rejected.
5. The prediction probability is displayed to the user.
6. The prediction details are saved into the SQLite database.
7. The History Dashboard displays previous predictions along with charts and statistics.

---

## 📋 Input Features

The prediction model uses the following information:

- Gender
- Married
- Dependents
- Education
- Self Employed
- Applicant Income
- Co-Applicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area

---

## 📊 Dashboard Features

The History Dashboard provides:

- Total Predictions
- Approved Applications
- Rejected Applications
- Approval Rate
- Approval vs Rejection Pie Chart
- Loan Amount Bar Chart
- Prediction History Table

---

## ▶️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yashaswichunduri08/Loan-Eligibility-Prediction.git
```

### 2. Navigate to the project folder

```bash
cd Loan-Eligibility-Prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask application

```bash
python app.py
```

### 5. Open the application

Visit the following URL in your browser:

```
http://127.0.0.1:5000
```

---

## 🧠 Machine Learning Workflow

- Data Collection
- Data Preprocessing
- Feature Selection
- Model Training
- Model Evaluation
- Model Saving using Joblib
- Flask Integration
- Web Deployment

---

## 🎯 Project Objectives

- Develop a Machine Learning model for loan prediction.
- Integrate the model into a Flask web application.
- Store prediction history in a database.
- Create an interactive analytics dashboard.
- Provide a simple and responsive user interface.

---

## 🔮 Future Enhancements

- User Authentication (Login & Registration)
- Admin Dashboard
- Export Prediction Reports (PDF/Excel)
- Email Notifications
- Cloud Deployment (Render/AWS)
- Explainable AI for Prediction Reasons
- Dark Mode Support
- Mobile-Friendly Improvements

---

## 📚 Learning Outcomes

This project helped me gain practical experience in:

- Machine Learning model development
- Flask web application development
- Database management using SQLite
- Data preprocessing with Pandas
- Dashboard and frontend development
- Git and GitHub version control
- Deploying Machine Learning models

---

## 👨‍💻 Author

**Yashaswi Chunduri**

- GitHub: https://github.com/yashaswichunduri08
- LinkedIn: https://linkedin.com/in/yashaswichunduri
