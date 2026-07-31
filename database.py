import sqlite3


def init_db():
    conn = sqlite3.connect("loan.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        gender TEXT,
        married TEXT,
        dependents TEXT,
        education TEXT,
        self_employed TEXT,
        applicant_income REAL,
        coapplicant_income REAL,
        loan_amount REAL,
        credit_history REAL,
        property_area TEXT,
        prediction TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_prediction(data):

    conn = sqlite3.connect("loan.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO predictions(
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
        prediction
    )
    VALUES(?,?,?,?,?,?,?,?,?,?,?)
    """, data)

    conn.commit()
    conn.close()