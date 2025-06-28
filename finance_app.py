import streamlit as st
import pandas as pd
import psycopg2

def connect_db():
    conn = psycopg2.connect(
        dbname="finance_app",
        user="postgres",
        password="1057",
        host="localhost",
        port="5432"
    )
    return conn

#App Layout
st.title("💰 Financial Wellness App")
#sidebar
tab1, tab2, tab3, tab4 , tab5= st.tabs(["Add Income", "Add Expense", "View Budget", "View Transactions","Delete all data"])

#Add income

with tab1:
    st.header("Add Income")
    source = st.text_input("Source")
    amount = st.number_input("Amount", min_value=0.0, step=0.1,key="income_amount")
    if st.button("Add Income"):

        conn=connect_db()
        cur=conn.cursor()
        cur.execute('''INSERT INTO income(source,amount,date) VALUES(%s,%s,CURRENT_DATE)''', (source, amount))
        conn.commit()
        cur.close()
        conn.close()
        st.success(f"Income added:{source} - Rs.{amount}")

#Add expense
with tab2:
        st.header("Add Expense")
        category= st.text_input("Category")
        desc = st.text_input("Description")
        amount = st.number_input("Amount", min_value=0.0, step=0.1,key="expense_amount")
        if st.button("Add Expense"):
            desc=desc if desc.strip()!="" else "NONE"

            conn=connect_db()
            cur=conn.cursor()
            cur.execute('''INSERT INTO expenses(category,description,amount,date) VALUES(%s,%s,%s,CURRENT_DATE)''', (category,desc,amount))
            conn.commit()
            cur.close()
            conn.close()
            st.success(f"Expense added:{category} - Rs.{amount}")

with tab3:
    st.header("Budget Summary")
    conn=connect_db()
    cur=conn.cursor()
    cur.execute("SELECT COALESCE(SUM(amount),0) FROM income")
    total_income=cur.fetchone()[0]
    cur.execute("SELECT COALESCE(SUM(amount),0) FROM expenses")
    total_expense=cur.fetchone()[0]
    cur.close()
    conn.close()

    balance=total_income-total_expense
    st.metric("Total Income",f"{total_income}")
    st.metric("Total Expenses",f"{total_expense}")
    st.metric("Balance",f"{balance}")



with tab4:
    st.header("Recent Transactions")
    conn=connect_db()
    cur=conn.cursor()
    cur.execute("SELECT id,source,amount,date FROM income ORDER BY date DESC LIMIT 10")
    income_rows=cur.fetchall()
    cur.execute("SELECT id,category,amount,date FROM expenses ORDER BY date DESC LIMIT 10")
    expense_rows=cur.fetchall()
    cur.close()
    conn.close()

    st.subheader("Income")
    st.dataframe(pd.DataFrame(income_rows, columns=["ID", "Source", "Amount", "Date"]))
    st.subheader("Expense")
    st.dataframe(pd.DataFrame(expense_rows, columns=["ID", "Description", "Amount", "Date"]))

with tab5:
    st.header("⚠️ Reset / Delete All Data")

    if st.button("Delete ALL Income and Expense Data"):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM income;")
        cur.execute("DELETE FROM expenses;")
        conn.commit()
        cur.close()
        conn.close()

        st.success("✅ All data has been deleted!")
        st.info("🔄 Please refresh or rerun the app to see the cleared tables.")






