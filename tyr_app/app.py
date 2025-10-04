import streamlit as st
from db.connection import get_connection
from utils.helpers import calculate_budget

st.title("Sample Streamlit + PostgreSQL App")

conn = get_connection()
st.write("Connected to database:", conn is not None)

# Example usage of helpers
budget = calculate_budget([100, 200, 300])
st.write(f"Sample budget calculation: {budget}")
