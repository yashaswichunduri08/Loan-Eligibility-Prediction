from flask import Flask, render_template, request
import pandas as pd
import joblib
import sqlite3
from database import init_db, save_prediction

app = Flask(__name__)

# Load trained ML model
model = joblib.load("model.pkl")

# Initialize database
init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Get form values
        gender = request.form["Gender"]
        married = request.form["Married"]
        dependents = request.form["Dependents"]
        education = request.form["Education"]
        self_employed = request.form["Self_Employed"]

        applicant_income = float(request.form["ApplicantIncome"])
        coapplicant_income = float(request.form["CoapplicantIncome"])
        loan_amount = float(request.form["LoanAmount"])
        loan_amount_term = float(request.form["Loan_Amount_Term"])
        credit_history = float(request.form["Credit_History"])

        property_area = request.form["Property_Area"]

        # Create dataframe
        data = pd.DataFrame({
            "Gender": [gender],
            "Married": [married],
            "Dependents": [dependents],
            "Education": [education],
            "Self_Employed": [self_employed],
            "ApplicantIncome": [applicant_income],
            "CoapplicantIncome": [coapplicant_income],
            "LoanAmount": [loan_amount],
            "Loan_Amount_Term": [loan_amount_term],
            "Credit_History": [credit_history],
            "Property_Area": [property_area]
        })

        # Prediction
        prediction = model.predict(data)[0]

        # Probability (RandomForest, Logistic Regression etc.)
        probability = model.predict_proba(data)[0]

        approval_probability = round(probability[1] * 100, 2)

        if prediction == 1:
            result = "Loan Approved ✅"
        else:
            result = "Loan Rejected ❌"

        # Save to database
        save_prediction((
            gender,
            married,
            dependents,
            education,
            self_employed,
            applicant_income,
            coapplicant_income,
            loan_amount,
            credit_history,
            property_area,
            result
        ))

        return render_template(
            "result.html",
            prediction=result,
            probability=approval_probability
        )

    except Exception as e:
        return f"<h2>Error</h2><br>{e}"


@app.route("/history")
def history():

    conn = sqlite3.connect("loan.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM predictions ORDER BY id DESC")

    rows = cursor.fetchall()

    total = len(rows)

    approved = sum(1 for row in rows if "Approved" in row[11])
    rejected = total - approved

    approval_rate = round((approved / total) * 100, 2) if total else 0

    loan_amounts = [row[8] for row in rows]

    conn.close()

    return render_template(
        "history.html",
        rows=rows,
        total=total,
        approved=approved,
        rejected=rejected,
        approval_rate=approval_rate,
        loan_amounts=loan_amounts
    )


@app.route("/about")
def about():

    return render_template("about.html")


@app.route("/clear")
def clear():

    conn = sqlite3.connect("loan.db")

    cursor = conn.cursor()

    cursor.execute("DELETE FROM predictions")

    conn.commit()

    conn.close()

    return """
    <h3>History Cleared Successfully</h3>

    <a href='/history'>View History</a>
    """


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )