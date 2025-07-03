id: 6863e3dfb2adee582c039f45_documentation
summary: Capital budgeting Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Capital Budgeting Dashboard: A Developer Guide

## Introduction to Capital Budgeting Dashboard
Duration: 05:00

Welcome to this codelab focusing on building a Capital Budgeting Dashboard using Streamlit. This application serves as a practical example of how to build interactive web applications for data analysis and visualization with minimal effort.

#### Why Capital Budgeting is Important

Managing finances effectively is crucial for both individuals and organizations. Capital budgeting, in a business context, involves planning and managing long-term investments. In a personal context, it relates to managing your income and expenses over time. Tools like this dashboard empower users to:

*   Track spending against planned budgets.
*   Identify areas of overspending or underspending.
*   Make informed decisions based on financial data.
*   Visualize financial trends.

#### Key Concepts Explained

This application demonstrates several core concepts:

*   **Budgeting:** Setting financial targets for various categories of spending.
*   **Variance Analysis:** Comparing actual financial performance to the planned budget. This helps in understanding where deviations occur.
*   **Trend Analysis:** While basic in this app, it shows how to visualize spending over time to identify patterns.
*   **Session State Management:** In Streamlit, maintaining data across user interactions is handled using `st.session_state`.

#### Core Formulae

The dashboard calculates and displays variance using these simple formulas:

*   **Variance:** The absolute difference between what was actually spent and what was budgeted.

    $$\text{Variance} = \text{Actual} - \text{Budgeted}$$

    A positive variance means overspending, while a negative variance means underspending.

*   **Percentage Variance:** The variance expressed as a percentage of the budgeted amount. This helps understand the magnitude of the variance relative to the budget.

    $$\text{Percentage Variance} = \frac{\text{Actual} - \text{Budgeted}}{\text{Budgeted}} \times 100$$

    <aside class="positive">
    Understanding these concepts and formulas is fundamental to effective financial management and analysis.
    </aside>

This codelab will guide you through the application's code, explaining how each component works and how they fit together to provide a functional budgeting tool.

## Setting up the Development Environment
Duration: 05:00

Before you can run and explore the application, you need to set up your Python environment and install the necessary libraries.

1.  **Install Python:** If you don't have Python installed, download it from [python.org](https://www.python.org/). Ensure you install Python 3.7 or higher.
2.  **Install pip:** `pip` is the package installer for Python. It usually comes bundled with Python installations. You can verify its installation by running `pip --version` in your terminal.
3.  **Install Required Libraries:** Open your terminal or command prompt and run the following command:

    ```console
    pip install streamlit pandas plotly
    ```

    This command installs Streamlit (for building the web app), pandas (for data manipulation), and plotly (for creating interactive charts).

4.  **Project Structure:** Create a directory for your project. Inside this directory, create two files and one sub-directory:

    ```
    your-project-folder/
    ├── app.py
    └── application_pages/
        └── page1.py
    ```

    The `app.py` file will contain the main application logic and navigation, while `application_pages/page1.py` will contain the code for the "Budget Overview" page.

Now that your environment is set up and the project structure is ready, you can copy the provided code into the respective files.

## Understanding the Main Application File (`app.py`)
Duration: 10:00

The `app.py` file serves as the entry point for the Streamlit application. It sets up the basic page configuration, displays introductory information, handles navigation, and includes common elements like the header and footer.

Open your `app.py` file and paste the following code:

```python
import streamlit as st

# Set basic page configuration
st.set_page_config(page_title="Capital Budgeting Dashboard", layout="wide")

# Add a sidebar image and a divider
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()

# Set the main title of the application
st.title("Capital Budgeting Dashboard")
st.divider()

# Define and display the introductory markdown text
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
# Sidebar navigation
page = st.sidebar.selectbox(label="Navigation", options=["Budget Overview"])

#  Page Routing 
# Based on the selected page, import and run the corresponding page script
if page == "Budget Overview":
    from application_pages.page1 import run_page1
    run_page1()
# Your code ends

# Add a footer and caption
st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity. "
           "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors")

```

Let's break down the key parts:

*   `st.set_page_config()`: Configures the browser tab title and layout (set to `wide` here to use more screen space).
*   `st.sidebar.image()` and `st.sidebar.divider()`: Add an image and a visual separator to the left sidebar.
*   `st.title()` and `st.divider()`: Set the main title of the app on the page body and add a separator.
*   `st.markdown(markdown_text)`: Displays the introductory text, including headers, lists, and the mathematical formulas using Markdown and LaTeX syntax.
*   `st.sidebar.selectbox()`: Creates a dropdown in the sidebar for navigation. Currently, it only has one option, "Budget Overview".
*   **Page Routing:** The `if page == "Budget Overview":` block is where the application logic for different pages is handled. It dynamically imports and calls the `run_page1()` function from `application_pages.page1`. This pattern allows you to easily add more pages later.
*   `st.write()` and `st.caption()`: Add a footer with copyright information and a disclaimer.

This `app.py` acts primarily as a router and setup script, delegating the main application logic to the page-specific modules.

## Deep Dive into the Budget Overview Page (`page1.py`)
Duration: 20:00

The `application_pages/page1.py` file contains the core functionality of the Capital Budgeting Dashboard. It handles data input, storage, calculations, and visualizations for the budget overview.

Create the `application_pages` directory if you haven't already, and inside it, create `page1.py`. Paste the following code into `application_pages/page1.py`:

```python
import streamlit as st
import pandas as pd
import plotly.express as px

def run_page1():
    st.header("Budget Overview")

    # Initialize session state for data storage
    # Check if 'budget_data' DataFrame exists in session state, otherwise create it
    if 'budget_data' not in st.session_state:
        st.session_state['budget_data'] = pd.DataFrame(columns=["Category", "Budgeted", "Actual"])
    # Check if 'expenses' list exists in session state, otherwise create it
    if 'expenses' not in st.session_state:
        st.session_state['expenses'] = []

    #  Budget Category Input Section 
    st.subheader("Define Budget Categories")
    category_name = st.text_input("Category Name") # Input for category name
    budgeted_amount = st.number_input("Budgeted Amount", min_value=0.0) # Input for budgeted amount (positive values only)

    # Button to add a new category
    if st.button("Add Category"):
        # Create a new DataFrame row for the category
        new_category = pd.DataFrame([{"Category": category_name, "Budgeted": budgeted_amount, "Actual": 0.0}])
        # Concatenate the new category to the existing budget_data in session state
        st.session_state['budget_data'] = pd.concat([st.session_state['budget_data'], new_category], ignore_index=True)
        st.success(f"Category '{category_name}' added successfully!") # Display success message

    #  Expense Logging Form Section 
    st.subheader("Log Expenses")
    # Use a form to group expense inputs and the submit button
    with st.form("expense_form"):
        # Dropdown to select the category for the expense (populated from existing categories)
        expense_category = st.selectbox("Expense Category", st.session_state['budget_data']["Category"].tolist())
        expense_date = st.date_input("Date of Expense") # Input for the expense date
        expense_amount = st.number_input("Expense Amount", min_value=0.0) # Input for the expense amount (positive values only)
        submitted = st.form_submit_button("Add Expense") # Submit button for the form

        # Process the form submission
        if submitted:
            # Append the new expense details to the expenses list in session state
            st.session_state['expenses'].append({"Category": expense_category, "Date": expense_date, "Amount": expense_amount})
            # Update the 'Actual' spending for the selected category in budget_data
            # Use .loc for label-based indexing to find the row and update the 'Actual' column
            st.session_state['budget_data'].loc[st.session_state['budget_data']['Category'] == expense_category, 'Actual'] += expense_amount
            st.success("Expense added successfully!") # Display success message

    #  Data Processing and Summary Section 
    st.subheader("Budget Summary")
    # Create a copy of the budget data to perform calculations
    budget_df = st.session_state['budget_data'].copy()
    # Calculate Variance
    budget_df["Variance"] = budget_df["Actual"] - budget_df["Budgeted"]
    # Calculate Percentage Variance (handle division by zero if Budgeted is 0)
    budget_df["Percentage Variance"] = (budget_df["Variance"] / budget_df["Budgeted"].replace(0, pd.NA)) * 100
    # Display the summary DataFrame
    st.dataframe(budget_df)

    #  Visualization Section 
    st.subheader("Visualizations")
    # Create a grouped bar chart comparing Budgeted and Actual spending by Category
    fig_bar = px.bar(budget_df, x="Category", y=["Budgeted", "Actual"], barmode="group", title="Budgeted vs Actual Spending")
    st.plotly_chart(fig_bar) # Display the bar chart

    #  Trend Analysis Section (Basic) 
    st.subheader("Spending Trends")
    # Loop through each defined category
    for category in budget_df["Category"]:
        # Filter the raw expenses list for the current category and extract amounts
        category_expenses = [expense["Amount"] for expense in st.session_state['expenses'] if expense["Category"] == category]
        if category_expenses:
            # If there are expenses, create a simple line chart (index as x-axis, amount as y-axis)
            fig_trend = px.line(x=range(len(category_expenses)), y=category_expenses, title=f"Spending Trend for {category}")
            st.plotly_chart(fig_trend) # Display the trend chart
        else:
            st.write(f"No expenses logged for {category} yet.") # Indicate if no expenses for a category

    #  Alert System Section 
    st.subheader("Alerts")
    # Iterate through the budget summary DataFrame rows
    for index, row in budget_df.iterrows():
        # Check if Variance is positive (overspending)
        if row["Variance"] > 0:
            # Display a warning message for overspending
            st.warning(f"Overspending alert! Actual spending for {row['Category']} exceeds the budget by {row['Variance']:.2f}.")
        # Add an optional alert for significant underspending (e.g., >50% below budget)
        # You could add more complex alert logic here
        # elif row["Variance"] < 0 and row["Percentage Variance"] < -50:
        #     st.info(f"Underspending alert! Actual spending for {row['Category']} is significantly below budget by {-row['Variance']:.2f}.")

```

Let's explore the key components in `page1.py`:

*   **Session State Initialization:**
    ```python
    if 'budget_data' not in st.session_state:
        st.session_state['budget_data'] = pd.DataFrame(columns=["Category", "Budgeted", "Actual"])
    if 'expenses' not in st.session_state:
        st.session_state['expenses'] = []
    ```
    Streamlit reruns the script from top to bottom every time a user interacts with the app. `st.session_state` is used to persist data (like our budget table and list of expenses) across these reruns. These lines ensure that `budget_data` (a pandas DataFrame) and `expenses` ( a list of dictionaries) are initialized the first time the app runs or when the session state is cleared.

*   **Define Budget Categories:**
    ```python
    st.subheader("Define Budget Categories")
    category_name = st.text_input("Category Name")
    budgeted_amount = st.number_input("Budgeted Amount", min_value=0.0)
    if st.button("Add Category"):
        # ... add category logic ...
    ```
    This section provides inputs (`st.text_input`, `st.number_input`) for the user to define a budget category and its corresponding budgeted amount. The "Add Category" button triggers the logic to create a new row in the `st.session_state['budget_data']` DataFrame using `pd.concat`.

*   **Log Expenses Form:**
    ```python
    st.subheader("Log Expenses")
    with st.form("expense_form"):
        # ... form inputs ...
        submitted = st.form_submit_button("Add Expense")
        if submitted:
            # ... add expense logic ...
    ```
    Using `with st.form("expense_form"):` groups several input widgets (`st.selectbox`, `st.date_input`, `st.number_input`) and a submit button (`st.form_submit_button`) together. When the form is submitted, all values are available, and the code inside the `if submitted:` block is executed. The selected category for the expense is chosen from the categories already defined in `st.session_state['budget_data']`. The expense is added to the `st.session_state['expenses']` list, and importantly, the `Actual` column in `st.session_state['budget_data']` for the relevant category is updated using `.loc`.

*   **Budget Summary:**
    ```python
    st.subheader("Budget Summary")
    budget_df = st.session_state['budget_data'].copy()
    budget_df["Variance"] = budget_df["Actual"] - budget_df["Budgeted"]
    # ... calculate percentage variance ...
    st.dataframe(budget_df)
    ```
    Here, a copy of the current `budget_data` is made. Variance and Percentage Variance columns are calculated based on the formulas discussed earlier. `replace(0, pd.NA)` is used in the percentage variance calculation to avoid division by zero errors if a category has a budgeted amount of 0. `st.dataframe()` displays the resulting table.

*   **Visualizations:**
    ```python
    st.subheader("Visualizations")
    fig_bar = px.bar(...)
    st.plotly_chart(fig_bar)

    st.subheader("Spending Trends")
    for category in budget_df["Category"]:
        # ... trend chart logic ...
    ```
    This section uses the `plotly.express` library to create visualizations. A grouped bar chart (`px.bar`) compares budgeted vs actual spending for each category. A basic trend analysis is shown by looping through categories, filtering expenses for each, and plotting a line chart (`px.line`) showing the amount of each expense logged for that category in the order they were added.

*   **Alerts:**
    ```python
    st.subheader("Alerts")
    for index, row in budget_df.iterrows():
        if row["Variance"] > 0:
            st.warning(f"Overspending alert! ...")
    ```
    The code iterates through the calculated budget summary DataFrame. If the `Variance` for any category is greater than 0 (indicating overspending), a warning message is displayed using `st.warning()`.

This detailed look at `page1.py` shows how Streamlit components, pandas for data handling, and plotly for visualization are integrated to create an interactive dashboard page.

## Running and Interacting with the Application
Duration: 05:00

Now that you have the code for both `app.py` and `application_pages/page1.py` in the correct locations, you can run the application.

1.  **Open your terminal or command prompt.**
2.  **Navigate to your project directory** (the folder containing `app.py`).
3.  **Run the Streamlit application** using the following command:

    ```console
    streamlit run app.py
    ```

4.  Streamlit will start a local web server and open the application in your default web browser. If it doesn't open automatically, navigate to the local URL displayed in your terminal (usually `http://localhost:8501`).

**Interacting with the Dashboard:**

*   **Define Budget Categories:** Use the inputs under "Define Budget Categories" to add budget items. For example:
    *   Category Name: `Groceries`, Budgeted Amount: `400.00`
    *   Category Name: `Utilities`, Budgeted Amount: `150.00`
    *   Click "Add Category" after each entry.
*   **Log Expenses:** Use the "Log Expenses" form.
    *   Select a category from the dropdown (e.g., `Groceries`).
    *   Choose a date.
    *   Enter an amount (e.g., `55.75`).
    *   Click "Add Expense".
    *   Log a few more expenses for different categories.
*   **View Summary and Visualizations:** As you add categories and log expenses, the "Budget Summary" table and the charts under "Visualizations" and "Spending Trends" will update automatically, showing the comparison between budgeted and actual amounts, variance, and trends.
*   **Check Alerts:** The "Alerts" section will show warnings if your actual spending in any category exceeds the budgeted amount.

<aside class="positive">
Experiment by adding various categories and logging different expenses. Observe how the table, charts, and alerts update in real-time based on your input.
</aside>

This interaction demonstrates the dynamic nature of Streamlit applications and how user input drives data updates and visualizations.

## Extending the Application (Optional)
Duration: 15:00

This application provides a solid foundation for capital budgeting. Here are some ideas for how you could extend and improve it:

1.  **Save and Load Data:** Currently, all data is stored in session state and is lost when the app is closed. Implement functionality to save the `budget_data` and `expenses` to a file (like CSV, JSON, or a simple database) and load it when the app starts. Streamlit's file uploader (`st.file_uploader`) and downloader (`st.download_button`) components could be useful here.
2.  **More Detailed Trend Analysis:**
    *   Allow users to filter trend charts by date range.
    *   Aggregate expenses by month or week to show trends over time intervals instead of just sequential expense logging.
    *   Plot cumulative spending over time for each category.
3.  **Additional Visualizations:**
    *   A pie chart showing the distribution of budgeted amounts across categories.
    *   A variance chart highlighting which categories have the largest positive or negative variances.
4.  **Edit and Delete Functionality:** Add options to edit existing budget categories or logged expenses, or to delete them. This would require more complex state management and UI elements (e.g., displaying expenses in a table with edit/delete buttons).
5.  **User Authentication:** For a multi-user application, implement a simple authentication system to separate user data.
6.  **Export Data:** Allow users to export the budget summary or raw expenses data to a CSV or Excel file.

Implementing these features would involve adding new functions or modifying existing ones in `page1.py`, and potentially adding new components to the Streamlit layout.

<aside class="positive">
Consider picking one or two extensions that seem most interesting to you and try to implement them. This is a great way to further practice your Streamlit and Python skills!
</aside>

This concludes the codelab on the Capital Budgeting Dashboard. You have learned how the application is structured, how it handles data input, processing, and visualization, and how to run it. You also have ideas on how to take it further.

