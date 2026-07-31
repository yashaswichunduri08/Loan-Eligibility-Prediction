# 🏦 Loan Eligibility Prediction System

A Machine Learning-based web application that predicts whether a loan application is likely to be **Approved** or **Rejected** based on applicant details. The application provides an intuitive web interface, prediction probability, analytics dashboard, and stores prediction history using SQLite.

---

## 📌 Project Overview

Financial institutions receive thousands of loan applications. Evaluating each application manually is time-consuming and can lead to inconsistencies.

This project uses a trained Machine Learning model to predict loan eligibility based on applicant information such as income, credit history, education, marital status, and property area.

The application is built using **Flask**, **Scikit-learn**, **SQLite**, **HTML**, **CSS**, and **Chart.js**.

---

## ✨ Features

- ✅ Loan Eligibility Prediction
- 📊 Approval Probability
- 📈 Analytics Dashboard
- 📜 Prediction History
- 💾 SQLite Database Integration
- 📱 Responsive User Interface
- 🎨 Professional Dashboard Design
- 📉 Interactive Charts using Chart.js

---

## 🛠️ Tech Stack

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

---

## 📂 Project Structure

```text
Loan-Eligibility-Prediction
│
├── app.py
├── database.py
├── train_model.py
├── model.pkl
├── requirements.txt
├── README.md
│
├── dataset/
│   └── loan_data.csv
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   ├── result.html
│   ├── history.html
│   └── about.html
│
└── screenshots/
    ├── home.png
    ├── dashboard.png
    ├── approved.png
    └── rejected.png
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yashaswichunduri08/Loan-Eligibility-Prediction.git
```

### Move into the project folder

```bash
cd Loan-Eligibility-Prediction
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📝 Input Features

The model predicts loan eligibility using the following applicant details:

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

## 📊 Dashboard

The History Dashboard includes:

- Total Predictions
- Approved Loans
- Rejected Loans
- Approval Rate
- Approval vs Rejection Pie Chart
- Loan Amount Bar Chart
- Prediction History Table

---

## 🧠 Machine Learning Model

The model was trained using a supervised Machine Learning algorithm.

### Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Engineering
4. Model Training
5. Model Evaluation
6. Model Serialization using Joblib
7. Flask Deployment

---

## 📸 Screenshots

### Home Page

> Add screenshot here

### Prediction Result

> Add screenshot here

### Analytics Dashboard

> Add screenshot here

### About Page

> Add screenshot here

---

## 🚀 Future Enhancements

- 🔐 User Authentication
- 👤 Admin Dashboard
- 📄 Export Prediction History to PDF/Excel
- 📧 Email Notification
- ☁️ Cloud Deployment (Render/AWS)
- 🤖 Explainable AI (Prediction Reasons)
- 🌙 Dark Mode
- 📱 Mobile App Integration

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Flask Web Development
- Machine Learning Model Deployment
- SQLite Database Integration
- Data Preprocessing
- Dashboard Design
- Git & GitHub
- Responsive UI Development

---

## 👨‍💻 Author

**Yashaswi Chunduri**

- GitHub: https://github.com/yashaswichunduri08
- LinkedIn: https://linkedin.com/in/yashaswichunduri

---

## 📄 License

This project is intended for educational and portfolio purposes.

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
