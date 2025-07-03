
import streamlit as st

st.set_page_config(page_title="Capital Budgeting Dashboard", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("Capital Budgeting")
st.divider()

st.markdown("""
# Capital Budgeting Dashboard

This application helps you manage your budget by comparing your planned spending (budget) with your actual expenses.  It provides visual summaries and alerts to help you identify areas where you might be overspending.

**Core Concepts:**

*   **Budgeting:** Creating a financial plan that outlines expected income and expenses.
*   **Variance Analysis:** Comparing budgeted amounts to actual amounts to identify deviations.
*   ****Percentage Variance:**** The variance as a percentage of the budgeted amount.
*   **Trend Analysis:** Examining spending patterns over time.

**Mathematical Formulas:**

*   **Variance:**
    $$
    Variance = Actual - Budgeted
    $$
*   **Percentage Variance:**
    $$
    Percentage\\ Variance = \\frac{Actual - Budgeted}{Budgeted} \\times 100
    $$
""")

# Navigation
page = st.sidebar.selectbox(label="Navigation", options=["Budget Input", "Expense Tracking", "Summary"])

if page == "Budget Input":
    from application_pages.budget_input import run_budget_input
    run_budget_input()
elif page == "Expense Tracking":
    from application_pages.expense_tracking import run_expense_tracking
    run_expense_tracking()
elif page == "Summary":
    from application_pages.summary import run_summary
    run_summary()

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity. "
           "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors")
