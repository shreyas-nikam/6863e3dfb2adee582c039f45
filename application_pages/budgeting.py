
import streamlit as st
import pandas as pd
import plotly.express as px

def calculate_variance(budgeted, actual):
    return actual - budgeted

def check_overspending(variance, threshold=0):
    return variance > threshold

def create_bar_chart(df):
    fig = px.bar(df, x="Category", y=["Budgeted", "Actual"], barmode="group")
    return fig

def run_budgeting():
    st.header("Budgeting")

    # Initialize session state
    if 'budget_data' not in st.session_state:
        st.session_state['budget_data'] = pd.DataFrame(columns=["Category", "Budgeted", "Actual", "Variance"])
    if 'expenses' not in st.session_state:
        st.session_state['expenses'] = []

    # Budget Category Input
    category = st.text_input("Category", help="Enter the budget category (e.g., Rent, Groceries)")
    budgeted_amount = st.number_input("Budgeted Amount", value=0.0, step=100.0, help="Enter the budgeted amount for this category")

    if st.button("Add Category"):
        new_row = pd.DataFrame([{"Category": category, "Budgeted": budgeted_amount, "Actual": 0.0, "Variance": 0.0}])
        st.session_state['budget_data'] = pd.concat([st.session_state['budget_data'], new_row], ignore_index=True)

    # Expense Logging Form
    with st.form("expense_form"):
        st.subheader("Log Expense")
        expense_category = st.selectbox("Expense Category", options=st.session_state['budget_data']['Category'].unique())
        expense_date = st.date_input("Date")
        expense_amount = st.number_input("Amount", value=0.0, step=10.0)
        submitted = st.form_submit_button("Add Expense")

        if submitted:
            st.session_state['expenses'].append({"Category": expense_category, "Date": expense_date, "Amount": expense_amount})

            # Update budget_data with actual expenses
            st.session_state['budget_data'].loc[st.session_state['budget_data']['Category'] == expense_category, 'Actual'] += expense_amount
            st.session_state['budget_data']['Variance'] = st.session_state['budget_data'].apply(lambda row: calculate_variance(row['Budgeted'], row['Actual']), axis=1)

    # Summary Table
    st.subheader("Budget Summary")
    st.dataframe(st.session_state['budget_data'])

    # Bar Chart
    if not st.session_state['budget_data'].empty:
        fig = create_bar_chart(st.session_state['budget_data'])
        st.plotly_chart(fig)

    # Alerts
    st.subheader("Alerts")
    for index, row in st.session_state['budget_data'].iterrows():
        if check_overspending(row['Variance']):
            st.warning(f"Overspending detected in {row['Category']}! Variance: {row['Variance']:.2f}")
