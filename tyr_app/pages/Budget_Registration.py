import streamlit as st
from db.connection import get_connection
from db.model import BudgetModel
import pandas as pd

st.title("Budget Registration & Records")

conn = get_connection()
st.write("Connected to database:", conn is not None)
budget_model = BudgetModel(conn) if conn else None

# --- Budget Registration Form ---
st.header("Register Budget Entry")
with st.form("budget_form"):
    name = st.text_input("Name")
    amount = st.number_input("Amount", min_value=0.0, step=0.01)
    submit = st.form_submit_button("Register")

    if submit and budget_model:
        budget_model.insert_budget(name, amount)
        st.success("Budget entry registered!")

# --- List Budget Records ---
st.header("Budget Records")
if budget_model:
    rows = budget_model.get_all_budgets()
    df = pd.DataFrame(rows, columns=["ID", "Name", "Amount"])
    st.dataframe(df)
else:
    st.warning("Database connection not available.")
