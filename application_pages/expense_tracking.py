
import streamlit as st
import pandas as pd

def run_expense_tracking():
    st.header("Log Expenses")
    if 'expenses_df' not in st.session_state:
        st.session_state['expenses_df'] = pd.DataFrame(columns=["Category", "Date", "Amount"])

    df = st.session_state['expenses_df']
    categories = st.session_state.get('budget_df', pd.DataFrame())['Category'].tolist()

    with st.form("log_expense_form"):
        category = st.selectbox("Category", options=categories) if categories else st.warning("Please add budget categories first.")
        date = st.date_input("Date")
        amount = st.number_input("Expense Amount", min_value=0.0, format="%.2f")
        submitted = st.form_submit_button("Log Expense")
        if submitted and category:
            new_entry = pd.DataFrame([[category, date, amount]], columns=["Category", "Date", "Amount"])
            df = pd.concat([df, new_entry], ignore_index=True)
            st.session_state['expenses_df'] = df

    if not df.empty:
        st.subheader("Logged Expenses")
        st.dataframe(df)

