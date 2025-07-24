
import streamlit as st
import plotly.graph_objects as go

def run_budget_actual():
    st.title("Budget vs. Actual Spending")
    st.markdown("""
    This page allows you to compare your budgeted spending against your actual expenses. Understanding the variance between these two is crucial for effective financial management.
    """)
    st.markdown("""
    The core concept demonstrated here is **budget variance**, which is the difference between your budgeted spending and your actual expenses. The formula for calculating variance is:

    $$Variance = Actual - Budgeted$$

    A positive variance indicates that you spent more than you budgeted (overspending), while a negative variance indicates that you spent less than you budgeted (underspending). Understanding variance is essential for effective personal finance management. This aligns with the post-audit phase of capital budgeting, comparing planned vs. actual results.
    """)

    # ... (Add interactive components for budget input, expense logging, and visualization here using Plotly) ...

    budgeted = [1000, 500, 300]
    actual = [1200, 400, 350]
    categories = ["Rent", "Groceries", "Utilities"]

    fig = go.Figure(data=[
        go.Bar(name='Budgeted', x=categories, y=budgeted),
        go.Bar(name='Actual', x=categories, y=actual)
    ])
    st.plotly_chart(fig)

