# 💰 Finance Tracker App (Streamlit + PostgreSQL)

This is a **Financial Wellness Web App** built using **Streamlit** and **PostgreSQL**. It allows users to **track income and expenses**, view a **budget summary**, check recent transactions, and **delete all data** for resetting.

---

## 🚀 Features

- ✅ Add Income with date stamp
- 💸 Log Expenses with category and optional description
- 📊 View Budget Summary (Total Income, Expenses, and Balance)
- 🧾 View Recent Transactions (both income and expenses)
- 🗑️ One-click option to **delete all data**

---

## 🧱 Built With

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: [PostgreSQL](https://www.postgresql.org/)
- **Language**: Python

---

## 📁 Project Structure

```
FINANCE_APP_PROJECT_Streamlit/
├── main.py                # Streamlit application
├── finance_app.py         # (Optional) Extra logic or utilities
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## 🖥️ How to Run the App

### 1. 🔧 Set Up PostgreSQL

Create a PostgreSQL database called `finance_app` and the following tables:

```sql
CREATE TABLE income (
    id SERIAL PRIMARY KEY,
    source TEXT,
    amount FLOAT,
    date DATE
);

CREATE TABLE expenses (
    id SERIAL PRIMARY KEY,
    category TEXT,
    description TEXT,
    amount FLOAT,
    date DATE
);
```

### 2. 📦 Install Python Requirements

Create a virtual environment (optional but recommended):

```bash
python -m venv env
source env/bin/activate     # On Windows: env\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

> If you don’t have a `requirements.txt`, create one using:
```bash
pip freeze > requirements.txt
```

Example dependencies:
```
streamlit
pandas
psycopg2
```

### 3. ▶️ Run the App

```bash
streamlit run main.py
```

---

## 🔑 Database Connection

Your app connects to PostgreSQL using:

```python
psycopg2.connect(
    dbname="finance_app",
    user="postgres",
    password="1057",
    host="localhost",
    port="5432"
)
```

> ⚠️ Make sure PostgreSQL is installed, the database and tables exist, and credentials are correct.

---

## 📌 Future Ideas

- Add login/authentication system
- Track monthly/weekly spending trends
- Pie charts or graphs for income/expenses
- Export data as CSV or PDF
- Deploy to Streamlit Cloud or Heroku

---

## 🧑‍💻 Author

**Vaishnavi**  
Student | Developer | Finance App Creator ✨

---

## 💡 License

This project is for learning and educational purposes. Feel free to build on it, improve it, or share it!

