
import streamlit as st
import pandas as pd
import plotly.express as px

def run_page1():
    st.header("Budget Overview")

    # Initialize session state for data storage
    if 'budget_data' not in st.session_state:
        st.session_state['budget_data'] = pd.DataFrame(columns=["Category", "Budgeted", "Actual"])
    if 'expenses' not in st.session_state:
        st.session_state['expenses'] = []

    # Budget Category Input
    st.subheader("Define Budget Categories")
    category_name = st.text_input("Category Name")
    budgeted_amount = st.number_input("Budgeted Amount", min_value=0.0)

    if st.button("Add Category"):
        new_category = pd.DataFrame([{"Category": category_name, "Budgeted": budgeted_amount, "Actual": 0.0}])
        st.session_state['budget_data'] = pd.concat([st.session_state['budget_data'], new_category], ignore_index=True)
        st.success(f"Category '{category_name}' added successfully!")

    # Expense Logging Form
    st.subheader("Log Expenses")
    with st.form("expense_form"):
        expense_category = st.selectbox("Expense Category", st.session_state['budget_data']["Category"].tolist())
        expense_date = st.date_input("Date of Expense")
        expense_amount = st.number_input("Expense Amount", min_value=0.0)
        submitted = st.form_submit_button("Add Expense")

        if submitted:
            st.session_state['expenses'].append({"Category": expense_category, "Date": expense_date, "Amount": expense_amount})
            #Update the actual spending in budget_data
            st.session_state['budget_data'].loc[st.session_state['budget_data']['Category'] == expense_category, 'Actual'] += expense_amount
            st.success("Expense added successfully!")


    # Data Processing and Calculations
    st.subheader("Budget Summary")
    budget_df = st.session_state['budget_data'].copy()
    budget_df["Variance"] = budget_df["Actual"] - budget_df["Budgeted"]
    budget_df["Percentage Variance"] = (budget_df["Variance"] / budget_df["Budgeted"]) * 100
    st.dataframe(budget_df)

    # Visualization Components
    st.subheader("Visualizations")
    # Bar Chart
    fig_bar = px.bar(budget_df, x="Category", y=["Budgeted", "Actual"], barmode="group", title="Budgeted vs Actual Spending")
    st.plotly_chart(fig_bar)

    # Trend Charts (basic implementation)
    st.subheader("Spending Trends")
    for category in budget_df["Category"]:
        category_expenses = [expense["Amount"] for expense in st.session_state['expenses'] if expense["Category"] == category]
        if category_expenses:
            fig_trend = px.line(x=range(len(category_expenses)), y=category_expenses, title=f"Spending Trend for {category}")
            st.plotly_chart(fig_trend)
        else:
            st.write(f"No expenses logged for {category} yet.")

    #Alert system
    st.subheader("Alerts")
    for index, row in budget_df.iterrows():
        if row["Variance"] > 0:
            st.warning(f"Overspending alert! Actual spending for {row['Category']} exceeds the budget by {row['Variance']:.2f}.")
