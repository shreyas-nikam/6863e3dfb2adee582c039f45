
import streamlit as st

st.set_page_config(page_title="Capital Budgeting Dashboard", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("Capital Budgeting Dashboard")
st.divider()

markdown_text = """
### Understanding Capital Budgeting

This application helps you visualize and manage your budget by comparing your planned (budgeted) spending against your actual expenses. It provides insights into your spending habits, identifies areas of overspending, and allows you to make informed financial decisions.

#### Key Concepts:

*   **Budgeting:** Creating a financial plan that outlines expected income and expenses for a specific period.
*   **Variance Analysis:** Comparing budgeted amounts to actual amounts to identify deviations from the plan.
*   **Trend Analysis:** Examining spending patterns over time to predict future outcomes.

#### Formulae:

*   **Variance:** The difference between the actual and budgeted amount.

    $$\text{Variance} = \text{Actual} - \text{Budgeted}$$

*   **Percentage Variance:** The variance as a percentage of the budgeted amount.

    $$\text{Percentage Variance} = \frac{\text{Actual} - \text{Budgeted}}{\text{Budgeted}} \times 100$$

By using this dashboard, you can proactively manage your finances and achieve your financial goals.
"""

st.markdown(markdown_text)

# Your code starts here
page = st.sidebar.selectbox(label="Navigation", options=["Budget Overview"])

if page == "Budget Overview":
    from application_pages.page1 import run_page1
    run_page1()

# Your code ends

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity. "
           "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors")
