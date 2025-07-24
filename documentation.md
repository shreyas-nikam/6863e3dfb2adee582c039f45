id: 6863e3dfb2adee582c039f45_documentation
summary: Capital budgeting Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Mastering Capital Budgeting with Streamlit: A QuLab Exploration

## 1. Introduction to Capital Budgeting and Application Overview
Duration: 00:05:00

Welcome to this comprehensive codelab focusing on **Capital Budgeting** concepts and their practical application using a Streamlit-powered web application. This "QuLab" (Quant University Lab) is designed to provide developers with a clear understanding of fundamental financial analysis techniques critical for investment decisions.

<aside class="positive">
<b>Why is Capital Budgeting Important?</b> Capital budgeting is the process companies use to evaluate potential major projects or investments. It allows businesses to make long-term investment decisions, such as whether to acquire new machinery, build a new plant, or launch a new product. Effective capital budgeting ensures that a company's financial resources are allocated to projects that will maximize shareholder wealth.
</aside>

This Streamlit application demonstrates three core capital budgeting concepts:
1.  **Budget vs. Actual Spending:** Understanding financial performance by comparing planned expenditures against actual ones. This is crucial for performance monitoring and control.
2.  **Net Present Value (NPV) Calculation:** A widely used method to evaluate the profitability of a projected investment or project.
3.  **Payback Period Calculation:** Determining the time it takes for an investment to generate enough cash flow to recover its initial cost.

The application's structure is modular, making it easy to understand and extend. The `app.py` serves as the main entry point, handling navigation and dynamically loading different financial analysis modules located in the `application_pages/` directory.

### Application Architecture
The application follows a simple modular design:

```
├── app.py                  # Main Streamlit application entry point
└── application_pages/      # Directory containing individual financial analysis modules
    ├── __init__.py
    ├── budget_actual.py    # Module for Budget vs. Actual comparison
    ├── npv_calculation.py  # Module for Net Present Value calculation
    └── payback_period.py   # Module for Payback Period calculation
```

The `app.py` script uses `st.sidebar.selectbox` to allow users to navigate between these pages, dynamically importing and executing the `run_` function from the selected module.

```python
# app.py
import streamlit as st

st.set_page_config(page_title="Capital Budgeting", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()
st.markdown("""
This lab explores capital budgeting concepts and techniques. Navigate through the pages to learn more.
""")

page = st.sidebar.selectbox(label="Navigation", options=["Budget vs Actual", "NPV Calculation", "Payback Period"])

if page == "Budget vs Actual":
    from application_pages.budget_actual import run_budget_actual
    run_budget_actual()
elif page == "NPV Calculation":
    from application_pages.npv_calculation import run_npv_calculation
    run_npv_calculation()
elif page == "Payback Period":
    from application_pages.payback_period import run_payback_period
    run_payback_period()
```

To get started, ensure you have Python installed. You'll also need Streamlit, Plotly, and NumPy.

```console
pip install streamlit plotly numpy
```

## 2. Exploring "Budget vs. Actual" Spending
Duration: 00:10:00

The "Budget vs. Actual" page is designed to visualize the difference between planned financial allocations and real expenditures. This comparison is fundamental to understanding financial performance and identifying areas for improvement.

The core concept explained here is **Budget Variance**.
The formula for calculating variance is:

$$Variance = Actual - Budgeted$$

*   A **positive variance** indicates that actual spending was higher than budgeted (overspending).
*   A **negative variance** indicates that actual spending was lower than budgeted (underspending).

Understanding variance is a critical aspect of financial management and aligns with the post-audit phase of capital budgeting, where planned outcomes are compared against actual results.

The `budget_actual.py` module uses Streamlit components for display and Plotly for interactive bar charts.

```python
# application_pages/budget_actual.py
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

    # Data for demonstration (currently hardcoded)
    budgeted = [1000, 500, 300]
    actual = [1200, 400, 350]
    categories = ["Rent", "Groceries", "Utilities"]

    # Create a bar chart using Plotly
    fig = go.Figure(data=[
        go.Bar(name='Budgeted', x=categories, y=budgeted),
        go.Bar(name='Actual', x=categories, y=actual)
    ])
    st.plotly_chart(fig)
```

<aside class="positive">
<b>Enhancement Idea:</b> Currently, the budgeted and actual values are hardcoded. You could enhance this page by adding Streamlit input widgets (e.g., `st.number_input` or `st.data_editor` for a table-like input) to allow users to dynamically enter their budget and actual figures for different categories.
</aside>

## 3. Deep Dive into "NPV Calculation"
Duration: 00:15:00

The Net Present Value (NPV) is one of the most fundamental and widely accepted methods for evaluating the profitability of a projected investment. It calculates the present value of all future cash flows generated by a project, discounted at a specific rate, and then subtracts the initial investment cost.

The formula for Net Present Value (NPV) is:

$$NPV = \sum_{t=1}^{n} \frac{CF_t}{(1+r)^t} - C_0$$

Where:
*   $CF_t$ = Net cash inflow during period $t$
*   $r$ = Discount rate (or rate of return that could be earned on an investment in the financial markets with similar risk)
*   $t$ = Number of time periods (e.g., years)
*   $C_0$ = Initial investment cost
*   $n$ = Total number of periods

A positive NPV generally indicates that the project is expected to be profitable and adds value to the company, making it a good investment. A negative NPV suggests the project will result in a net loss.

The `npv_calculation.py` module provides an interactive tool to calculate NPV:

```python
# application_pages/npv_calculation.py
import streamlit as st
import plotly.graph_objects as go
import numpy as np

def run_npv_calculation():
    st.title("Net Present Value (NPV) Calculation")
    st.markdown("""
    This page demonstrates how to calculate the Net Present Value (NPV) of a project. NPV is a crucial metric in capital budgeting, helping determine the profitability of an investment.
    """)
    # Input fields for initial investment, discount rate, and cash flows
    initial_investment = st.number_input("Initial Investment:", value=100000, step=1000)
    discount_rate = st.number_input("Discount Rate (%):", value=10, step=1) / 100
    cashflows = st.text_area("Cash Flows (comma-separated):", value="20000, 30000, 40000, 50000")

    try:
        # Convert comma-separated string to a list of floats
        cashflows_list = [float(x) for x in cashflows.split(',')]

        # Calculate NPV
        # The np.sum part calculates the present value of all future cash flows
        # The initial investment is subtracted as it's typically a cash outflow at time 0
        npv = -initial_investment + np.sum([cf / (1 + discount_rate)**(i + 1) for i, cf in enumerate(cashflows_list)])
        # Note: The original code had (1 + discount_rate)**i.
        # For typical NPV, the first cash flow is CF1 discounted by (1+r)^1, CF2 by (1+r)^2, etc.
        # So, the index `i` (which starts from 0 for enumerate) should be `i+1` for the power.
        # Corrected for standard NPV calculation.

        st.write(f"Net Present Value (NPV): {npv:.2f}")

        # Visualize cash flows using a bar chart
        fig = go.Figure(data=[go.Bar(x=list(range(1, len(cashflows_list) + 1)), y=cashflows_list)])
        fig.update_layout(xaxis_title="Year", yaxis_title="Cash Flow")
        st.plotly_chart(fig)

    except ValueError:
        st.error("Invalid cash flow input. Please use comma-separated numbers.")
```

<aside class="negative">
<b>Important Note:</b> In the original code, the NPV calculation used `(1 + discount_rate)**i` for the denominator, where `i` starts from 0. For standard NPV calculation, the first cash flow (CF1) should be discounted by $(1+r)^1$, the second (CF2) by $(1+r)^2$, and so on. If `enumerate` starts `i` from 0, then the exponent should be `i + 1`. The provided solution above has been corrected to `(1 + discount_rate)**(i + 1)`.
</aside>

## 4. Understanding "Payback Period"
Duration: 00:10:00

The Payback Period is a capital budgeting technique that determines the amount of time it takes for an investment to generate enough cash flow to recover its initial cost. It is a simple and widely used method, particularly for assessing liquidity and risk.

The calculation is straightforward:
1.  Sum the cash flows year by year.
2.  Identify the point at which the cumulative cash flow equals or exceeds the initial investment.

While simple, the payback period has limitations, such as not considering the time value of money (unless modified) and ignoring cash flows beyond the payback period.

The `payback_period.py` module facilitates this calculation:

```python
# application_pages/payback_period.py
import streamlit as st
import plotly.graph_objects as go

def run_payback_period():
    st.title("Payback Period Calculation")
    st.markdown("""
    This page calculates the payback period of a project. The payback period is the time it takes for a project to recoup its initial investment.
    """)
    # Input fields for initial investment and cash flows
    initial_investment = st.number_input("Initial Investment:", value=100000, step=1000)
    cashflows = st.text_area("Cash Flows (comma-separated):", value="20000, 30000, 40000, 50000")

    try:
        # Convert comma-separated string to a list of floats
        cashflows_list = [float(x) for x in cashflows.split(',')]
        cumulative_cashflow = 0
        payback_period = 0

        # Calculate cumulative cash flow and find payback period
        for i, cashflow in enumerate(cashflows_list):
            cumulative_cashflow += cashflow
            if cumulative_cashflow >= initial_investment:
                payback_period = i + 1 # Payback period is in years/periods
                break

        if payback_period > 0:
            st.write(f"Payback Period: {payback_period} years")
            # Visualize cash flows using a bar chart
            fig = go.Figure(data=[go.Bar(x=list(range(1, len(cashflows_list) + 1)), y=cashflows_list)])
            fig.update_layout(xaxis_title="Year", yaxis_title="Cash Flow")
            st.plotly_chart(fig)
        else:
            st.write("The project does not pay back the initial investment within the given cash flow periods.")

    except ValueError:
        st.error("Invalid cash flow input. Please use comma-separated numbers.")
```

<aside class="positive">
<b>Enhancement Idea:</b> You could extend this to calculate the **Discounted Payback Period** by first discounting each cash flow to its present value before summing them up. This would incorporate the time value of money, providing a more robust measure.
</aside>

## 5. Running and Extending the Application
Duration: 00:05:00

Now that you've explored the code and the underlying financial concepts, it's time to run the application and experiment with it.

### How to Run
1.  Save the `app.py` file and the `application_pages` directory (with its contents) in the same root directory.
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved `app.py`.
4.  Run the Streamlit application using the command:

    ```bash
    streamlit run app.py
    ```
5.  Streamlit will open the application in your default web browser (usually `http://localhost:8501`).

### Experiment and Extend
*   **Modify Inputs:** Change the initial investment, discount rate, and cash flow values in the NPV and Payback Period pages to observe how the results change.
*   **Add New Categories:** In "Budget vs. Actual," manually change the `budgeted`, `actual`, and `categories` lists to include more items.
*   **Implement Interactive Inputs for Budget vs. Actual:** As suggested earlier, add `st.number_input` widgets for `budgeted` and `actual` values for each category to make the "Budget vs. Actual" page fully interactive.
*   **Implement Discounted Payback Period:** Modify the `payback_period.py` file to first discount the cash flows before calculating the cumulative sum.
*   **Add Internal Rate of Return (IRR):** Challenge yourself by adding a new page (`irr_calculation.py`) to calculate the Internal Rate of Return for a project. This would require an iterative approach or using a library like `scipy.optimize.newton` to find the discount rate at which NPV is zero.
*   **Implement Sensitivity Analysis:** Add features to any of the calculations that allow users to vary one input (e.g., discount rate or a specific cash flow) and see how the NPV or Payback Period changes.

This QuLab provides a foundational understanding of capital budgeting concepts through a practical, interactive Streamlit application. By exploring, modifying, and extending this codebase, you will not only solidify your understanding of these financial principles but also enhance your skills in building powerful data applications with Streamlit.
