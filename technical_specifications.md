
# Technical Specifications for Budget vs. Actual Spending Dashboard

## Overview

This Streamlit application will provide users with a visual representation of their budgeting progress by comparing budgeted spending against actual expenses. The app will allow users to input budget categories and log expenses, generating summaries and alerts to highlight overspending. This application simplifies personal budgeting, illustrating the core concept of comparing planned financial behavior against actual outcomes, fostering proactive money management.

## Step-by-Step Development Process

1.  **Setup and Initialization:**
    *   Create a new Python project and install the Streamlit library: `pip install streamlit`
    *   Create a new Python file (e.g., `budget_dashboard.py`) and import the necessary libraries, including `streamlit`, `pandas`, and `plotly.express`.

2.  **Data Input Components:**
    *   Implement Streamlit input widgets (e.g., `st.text_input`, `st.number_input`) to allow users to define budget categories and their budgeted amounts. Store this information in a data structure like a Pandas DataFrame or a dictionary.
    *   Create input forms for logging actual expenses, enabling users to enter the category, date, and amount spent. Update the data structure to reflect these expenses.

3.  **Data Processing and Calculations:**
    *   Calculate the difference between budgeted and actual amounts for each category.
    *   Implement logic to determine if overspending has occurred in any category.

4.  **Visualization Components:**
    *   Use Plotly Express (`plotly.express`) to create a bar chart showing budgeted vs. actual spending for each category.
    *   Implement mini line charts using Plotly Express or similar libraries to display spending trends over time for each category.

5.  **Alert System:**
    *   Develop a function that checks for overspending based on a threshold (e.g., actual spending exceeding budgeted amount).
    *   Display alerts using `st.warning` or `st.error` to highlight categories where overspending has occurred.

6.  **User Interface Assembly:**
    *   Organize all the components within the Streamlit app using layouts (e.g., `st.columns`, `st.expander`) to create a clean and intuitive user interface.
    *   Add inline help and tooltips to guide users through the app's functionality.

## Core Concepts and Mathematical Foundations

### Budgeting
Budgeting is the process of creating a plan to spend your money. A budget is a financial plan that outlines expected income and expenses for a specific period. It helps individuals and organizations manage their finances effectively by controlling spending and saving habits.

Example: A monthly personal budget could include categories like Rent (\$1200), Groceries (\$400), Transportation (\$150), Entertainment (\$100), and Savings (\$200).

### Variance Analysis
Variance analysis is the process of comparing budgeted amounts to actual amounts to identify deviations from the plan.
$$
Variance = Actual - Budgeted
$$
Where:

*   $Variance$: The difference between the actual and budgeted amount.
*   $Actual$: The actual amount spent or earned.
*   $Budgeted$: The planned or expected amount.

This formula calculates the difference between the actual result and the planned or expected result. In this application, it will specifically show the difference between actual expenses and the budgeted amount for each category, helping users identify areas of overspending or underspending.

### Percentage Variance
The percentage variance provides a relative measure of the difference between actual and budgeted amounts.
$$
Percentage\ Variance = \\frac{Actual - Budgeted}{Budgeted} \times 100
$$
Where:

*   $Percentage\ Variance$: The variance as a percentage of the budgeted amount.
*   $Actual$: The actual amount spent or earned.
*   $Budgeted$: The planned or expected amount.

This formula shows the relative magnitude of the variance compared to the original budget, which provides context for evaluating the significance of the variance. For instance, a variance of \$50 on a budget of \$100 is more significant than a variance of \$50 on a budget of \$1000.

### Trend Analysis
Trend analysis involves examining data over time to identify patterns and predict future outcomes.  In the context of this application, we're looking at spending trends over time.

*Example:* If a user's entertainment expenses have been steadily increasing over the past three months, trend analysis would highlight this upward trend.

## Required Libraries and Dependencies

*   **Streamlit (version >= 1.0):**  The core library for building the int\fractive web application.
    ```python
    import streamlit as st
    ```
*   **Pandas (version >= 1.0):** Used for data manipulation and storage (e.g., storing budget categories and expenses).
    ```python
    import pandas as pd
    ```
*   **Plotly Express (version >= 4.0):**  For creating int\fractive charts, such as bar charts and line charts.
    ```python
    import plotly.express as px
    ```

## Implementation Details

1.  **Data Structures:**

    *   A Pandas DataFrame will store the budget categories, budgeted amounts, and actual expenses. Each row will represent a category, and columns will include "Category", "Budgeted", "Actual", and "Variance".
    *   A dictionary or list will be used to store the history of expenses for trend analysis, with the date as the key and expenses as the value.

2.  **Functions:**

    *   `calculate_variance(budgeted, actual)`:  Calculates the difference between the budgeted and actual amounts.
        ```python
        def calculate_variance(budgeted, actual):
            return actual - budgeted
        ```
    *   `check_overspending(variance, threshold=0)`:  Checks if the variance exceeds a threshold (default 0) to identify overspending.
        ```python
        def check_overspending(variance, threshold=0):
            return variance > threshold
        ```
    *   `create_bar_chart(df)`: Creates a bar chart of budgeted vs. actual spending.
        ```python
        def create_bar_chart(df):
            fig = px.bar(df, x="Category", y=["Budgeted", "Actual"], barmode="group")
            return fig
        ```
    *   `create_trend_chart(category_data)`: Creates a line chart of spending trends over time for a given category.
        ```python
        def create_trend_chart(category_data):
            #category_data should be a Pandas Series with dates as index
            fig = px.line(category_data, x=category_data.index, y=category_data.values, title="Spending Trend")
            return fig
        ```

## User Interface Components

1.  **Budget Category Input:** Text input fields (`st.text_input`) for users to define budget categories (e.g., "Rent", "Groceries").
2.  **Budgeted Amount Input:** Numerical input fields (`st.number_input`) for users to specify the budgeted amount for each category.
3.  **Expense Logging Form:**
    *   Dropdown selection (`st.selectbox`) to choose the expense category.
    *   Date input (`st.date_input`) to record the date of the expense.
    *   Numerical input (`st.number_input`) to enter the expense amount.
    *   Submit button (`st.form_submit_button`) to add the expense to the data.
4.  **Summary Table:** A table displayed using `st.dataframe` showing the budget categories, budgeted amounts, actual expenses, and variances.
5.  **Bar Chart:** A bar chart displayed using `st.plotly_chart` visualizing budgeted vs. actual spending.
6.  **Trend Charts:**  Mini line charts displayed using `st.plotly_chart`, one for each budget category, visualizing spending trends over time.
7.  **Alerts:** Text alerts displayed using `st.warning` or `st.error` to highlight categories where overspending has occurred.
8.  **Inline Help/Tooltips:**  `st.help` and `help` parameters within Streamlit components to explain each section.
