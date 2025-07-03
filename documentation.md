id: 6863e3dfb2adee582c039f45_documentation
summary: Capital budgeting Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Capital Budgeting Dashboard Codelab

## Introduction to the Capital Budgeting Dashboard
Duration: 05:00

Welcome to the Capital Budgeting Dashboard codelab! In this lab, you will explore a Streamlit application designed to help users manage finances by tracking budget versus actual spending. While the name "Capital Budgeting" typically applies to long-term investment decisions for large projects in finance, this application uses similar principles of planning, tracking, and variance analysis but is implemented for personal or small-scale budget management.

Understanding and managing your finances is crucial for achieving financial goals, whether personal or for a small business. This application provides a practical way to:

1.  **Plan:** Define expected spending across different categories.
2.  **Track:** Log actual expenses as they occur.
3.  **Analyze:** Compare planned (budgeted) amounts with actual spending to identify deviations (variances).
4.  **Visualize:** See your spending patterns and budget adherence graphically.

This process helps in identifying areas of potential overspending, understanding where money is going, and making informed decisions for future budgeting.

The application is built using Streamlit, a powerful Python library that allows you to create interactive web applications with minimal code. It demonstrates several core financial concepts applied to budgeting:

*   **Budgeting:** The process of creating a financial plan for a defined period, outlining expected income and expenses for different categories.
*   **Variance Analysis:** The technique of comparing planned or budgeted outcomes with actual results. A variance is the difference between the two.
*   **Percentage Variance:** The variance expressed as a percentage of the budgeted amount, providing a relative measure of deviation.
*   **Trend Analysis:** Examining financial data over time to identify patterns, increases, or decreases in spending for specific categories.

Let's look at the key formulas used in this application:

*   **Variance:** The simple difference between what was spent and what was budgeted.
    $$
    Variance = Budgeted - Actual
    $$
    (Note: The code calculates `Actual - Budgeted`. Both definitions are used in practice; `Budgeted - Actual` shows a positive variance for underspending and negative for overspending, while `Actual - Budgeted` shows positive for overspending and negative for underspending. This app uses the latter, where a positive variance means you spent more than budgeted).

*   **Percentage Variance:** The variance relative to the initial budget, indicating the magnitude of the deviation.
    $$
    Percentage\\ Variance = \\frac{Budgeted - Actual}{Budgeted} \\times 100
    $$
    (Again, note the formula aligns with `Budgeted - Actual`. The code uses `(Variance / Budgeted) * 100` based on its `Actual - Budgeted` variance, so a positive percentage means overspending relative to budget).

In the following steps, you will learn how this application is structured, how to set it up, and how each part works together to provide a comprehensive budgeting tool.

## Application Structure and Setup
Duration: 07:00

The application you'll be working with is structured into a main entry point (`app.py`) and several functional pages located in a subdirectory (`application_pages`). This modular structure helps in organizing the code and keeping the main file clean.

Here's a breakdown of the files:

*   `app.py`: This is the main file that sets up the Streamlit page configuration, displays the title and introductory markdown, and handles the navigation between different sections (pages) of the application using a sidebar selectbox. It imports functions from the `application_pages` directory based on the user's selection.
*   `application_pages/budget_input.py`: Contains the Streamlit code for the "Budget Input" page. This page allows the user to define spending categories and set their initial budgeted amounts.
*   `application_pages/expense_tracking.py`: Contains the Streamlit code for the "Expense Tracking" page. This page allows the user to log individual expenses against the defined categories.
*   `application_pages/summary.py`: Contains the Streamlit code for the "Summary" page. This page processes the budget and expense data, calculates variances, displays summary tables, and generates visualizations (bar charts and trend lines).

To run this application, you need to have Python installed, preferably Python 3.6 or newer. You also need to install the required libraries: `streamlit`, `pandas`, and `plotly`.

1.  **Save the code:** Create a directory for your project. Inside this directory, create the `app.py` file and an `application_pages` subdirectory. Save the provided code snippets into the corresponding files:
    *   `app.py`
    *   `application_pages/budget_input.py`
    *   `application_pages/expense_tracking.py`
    *   `application_pages/summary.py`

2.  **Install dependencies:** Open your terminal or command prompt, navigate to your project directory, and install the libraries using pip:

    ```bash
    pip install streamlit pandas plotly
    ```

    <aside class="positive">
    It's often a good practice to use a virtual environment to manage dependencies for different projects.
    </aside>

Now you are ready to run the application.

## Running the Application
Duration: 02:00

Once you have saved the code and installed the dependencies, running the Streamlit application is straightforward.

1.  Open your terminal or command prompt.
2.  Navigate to the directory where you saved `app.py`.
3.  Run the following command:

    ```console
    streamlit run app.py
    ```

Streamlit will start a local web server, and your default web browser will open automatically, displaying the application. If your browser doesn't open, look for the `Local URL` in the terminal output (usually `http://localhost:8501`) and open it manually in your browser.

You should now see the main page of the Capital Budgeting Dashboard, including the title, introductory text, and a sidebar navigation menu.

## Defining Your Budget
Duration: 05:00

The first step in using the application is to define your budget categories and the amount you plan to spend on each. This is handled by the code in `application_pages/budget_input.py`.

Navigate to the "Budget Input" page using the sidebar navigation.

You will see a form with fields for "Category Name" and "Budgeted Amount".

<aside class="positive">
The `st.form` construct is used here to group input widgets. When the "Add/Update Category" button is clicked, all inputs within the form are processed at once, and the state of the form is cleared if `clear_on_submit=True`.
</aside>

Let's look at the core logic in `application_pages/budget_input.py`:

```python
import streamlit as st
import pandas as pd

def run_budget_input():
    st.header("Input Budget Categories and Amounts")
    # Initialize DataFrame to store budget data
    if 'budget_df' not in st.session_state:
        st.session_state['budget_df'] = pd.DataFrame(columns=["Category", "Budgeted"])

    df = st.session_state['budget_df']

    with st.form("add_category_form", clear_on_submit=True):
        category = st.text_input("Category Name")
        amount = st.number_input("Budgeted Amount", min_value=0.0, format="%.2f")
        submitted = st.form_submit_button("Add/Update Category")
        if submitted and category:
            # Check if category already exists
            if category in df['Category'].values:
                # Update existing category
                df.loc[df['Category'] == category, 'Budgeted'] = amount
            else:
                # Add new category
                new_row = pd.DataFrame([[category, amount]], columns=["Category", "Budgeted"])
                df = pd.concat([df, new_row], ignore_index=True)
            # Update session state
            st.session_state['budget_df'] = df

    # Display the current budget
    if not df.empty:
        st.subheader("Current Budget Plan")
        st.dataframe(df.set_index('Category'))
```

<aside class="positive">
Notice the use of `st.session_state['budget_df']`. This is how data (the budget DataFrame) is stored and persisted across user interactions and page changes within a single user's session. Without session state, the DataFrame would reset every time an input changes or a button is clicked.
</aside>

Enter a category name (e.g., "Groceries") and a budgeted amount (e.g., "500.00"). Click "Add/Update Category". Repeat this process for other categories like "Rent", "Utilities", "Entertainment", etc.

As you add categories, the "Current Budget Plan" table below the form will update, showing your defined budget. This table is a `pandas` DataFrame displayed using `st.dataframe`.

## Logging Expenses
Duration: 05:00

Once you have defined your budget, you can start logging your actual expenses. This is handled by the code in `application_pages/expense_tracking.py`.

Navigate to the "Expense Tracking" page using the sidebar navigation.

You will find a form to log individual expenses.

```python
import streamlit as st
import pandas as pd

def run_expense_tracking():
    st.header("Log Expenses")
    # Initialize DataFrame to store expenses data
    if 'expenses_df' not in st.session_state:
        st.session_state['expenses_df'] = pd.DataFrame(columns=["Category", "Date", "Amount"])

    df = st.session_state['expenses_df']
    # Get categories from the budget DataFrame stored in session state
    categories = st.session_state.get('budget_df', pd.DataFrame())['Category'].tolist()

    with st.form("log_expense_form"):
        # Select box for categories - options come from the budget data
        category = st.selectbox("Category", options=categories) if categories else st.warning("Please add budget categories first.")
        date = st.date_input("Date")
        amount = st.number_input("Expense Amount", min_value=0.0, format="%.2f")
        submitted = st.form_submit_button("Log Expense")
        if submitted and category:
            # Add the new expense to the expenses DataFrame
            new_entry = pd.DataFrame([[category, date, amount]], columns=["Category", "Date", "Amount"])
            df = pd.concat([df, new_entry], ignore_index=True)
            # Update session state
            st.session_state['expenses_df'] = df

    # Display the logged expenses
    if not df.empty:
        st.subheader("Logged Expenses")
        st.dataframe(df)
```

Notice that the "Category" selectbox is populated dynamically from the categories you defined in the "Budget Input" step. This demonstrates how `st.session_state` allows data to be shared between different pages (or different runs of the script). If you haven't added any categories yet, you'll see a warning message prompting you to do so.

Use the form to log some expenses. Select a category, pick a date, and enter the amount spent. Click "Log Expense".

Just like the budget page, the logged expenses are stored in `st.session_state['expenses_df']` and displayed in a table below the form. Log a few expenses across different categories and dates to see how it works.

## Analyzing Budget vs. Actual
Duration: 07:00

The "Summary" page is where the magic happens – you can see how your actual spending compares to your budget. This functionality is implemented in `application_pages/summary.py`.

Navigate to the "Summary" page using the sidebar navigation.

If you haven't added budget categories or logged any expenses, you will see informational messages prompting you to do so.

The `summary.py` script retrieves the budget and expense data from session state, performs calculations, and displays the results.

```python
import streamlit as st
import pandas as pd
import plotly.express as px

def run_summary():
    st.header("Budget vs. Actual Expenses Summary")
    # Retrieve data from session state
    budget_df = st.session_state.get('budget_df', pd.DataFrame())
    expenses_df = st.session_state.get('expenses_df', pd.DataFrame())

    if budget_df.empty:
        st.info("Please define your budget categories first.")
        return
    if expenses_df.empty:
        st.info("No expenses logged yet.")
        return

    # Aggregate expenses per category
    expense_sum = expenses_df.groupby('Category')['Amount'].sum().reset_index()

    # Merge budget and expenses data
    merged = pd.merge(budget_df, expense_sum, on='Category', how='left')
    # Fill NaN values (categories with no expenses) with 0
    merged['Amount'] = merged['Amount'].fillna(0)
    # Calculate Variance (Budgeted - Actual in this calculation, opposite of app.py intro)
    # Let's align with the app.py intro formula: Actual - Budgeted
    merged['Variance'] = merged['Amount'] - merged['Budgeted']
    # Calculate Percentage Variance
    merged['Percent Variance'] = (merged['Variance'] / merged['Budgeted']) * 100

    st.subheader("Budget and Expenses Comparison")
    # Display the summary table
    st.dataframe(merged.set_index('Category'))

    # Visualization: Budget vs. Actual Bar Chart
    fig = px.bar(merged, x='Category', y=['Budgeted', 'Amount'], barmode='group',
                 labels={'Amount':'Amount', 'variable':'Type'}, title='Budget vs. Actual Spending')
    # Rename 'Amount' in the legend for clarity
    fig.for_each_trace(lambda t: t.update(name='Actual' if t.name == 'Amount' else t.name))
    st.plotly_chart(fig)

    # Highlight overspending categories
    overspent = merged[merged['Variance'] > 0] # Using Variance = Actual - Budgeted
    if not overspent.empty:
        st.warning("Over-spent in the following categories:")
        st.dataframe(overspent.set_index('Category'))

    # Trends over time per category - Line Charts
    st.subheader("Spending Trends Over Time")
    expenses_df['Date'] = pd.to_datetime(expenses_df['Date'])
    categories = merged['Category'].tolist()
    for cat in categories:
        cat_data = expenses_df[expenses_df['Category'] == cat].sort_values('Date')
        if not cat_data.empty:
            fig_trend = px.line(cat_data, x='Date', y='Amount', title=f"Spending Trend: {cat}")
            st.plotly_chart(fig_trend)
```

**Calculations:**

1.  The code first aggregates the expenses logged in `expenses_df` by 'Category' to get the total actual spending for each category.
2.  It then merges this aggregated expense data with the `budget_df` based on the 'Category'.
3.  Any categories from the budget with no logged expenses will have a missing value (`NaN`) for actual spending; these are filled with `0`.
4.  **Variance** is calculated as `Actual - Budgeted`. A positive variance means you spent more than budgeted (overspending). A negative variance means you spent less (underspending).
5.  **Percentage Variance** is calculated as `(Variance / Budgeted) * 100`. A positive percentage indicates the percentage by which you overspent relative to the budget. A negative percentage indicates the percentage by which you underspent.

**Output:**

*   **Budget and Expenses Comparison Table:** Displays the budget amount, actual spending, calculated variance, and percentage variance for each category.
*   **Budget vs. Actual Spending Bar Chart:** A visual comparison of the budgeted and actual amounts side-by-side for each category. This uses the `plotly.express` library, which `streamlit` integrates seamlessly with.
*   **Overspending Alerts:** If any category has a positive variance (Actual > Budgeted), a warning box appears listing these categories.
*   **Spending Trends Over Time:** For each category with logged expenses, a line chart shows how the spending accumulated over the dates expenses were logged. This helps visualize spending patterns and trends within specific categories.

Explore the summary page after entering some budget data and logging several expenses. Observe how the tables and charts update, helping you understand your spending habits and budget performance.

## Understanding Session State
Duration: 03:00

As you've seen in the code snippets for `budget_input.py`, `expense_tracking.py`, and `summary.py`, the application heavily relies on `st.session_state`.

```python
if 'budget_df' not in st.session_state:
    st.session_state['budget_df'] = pd.DataFrame(columns=["Category", "Budgeted"])
# ... later in the code ...
st.session_state['budget_df'] = df # Updating the state
```

```python
categories = st.session_state.get('budget_df', pd.DataFrame())['Category'].tolist() # Reading from state
```

In a typical web application, when a user interacts with a form or clicks a button, the entire page might reload, causing any in-memory data (like variables or DataFrames) to be lost. Streamlit's execution model reruns the script from top to bottom whenever there's an interaction. Without a mechanism to preserve state, the budget and expense data would disappear on every interaction.

`st.session_state` solves this problem. It is a dictionary-like object that persists across reruns of the script within a single user's browser session.

*   You can store any Python object in `st.session_state`.
*   You access and modify it like a dictionary: `st.session_state['key'] = value`.
*   You can check if a key exists using `if 'key' in st.session_state:`.
*   `st.session_state.get('key', default_value)` is a safe way to retrieve a value, providing a default if the key doesn't exist.

In this application:
*   `st.session_state['budget_df']` stores the DataFrame containing the budget categories and amounts.
*   `st.session_state['expenses_df']` stores the DataFrame containing the logged expenses.

This allows you to define your budget on one page, navigate to another page to log expenses (which uses the budget categories from the state), and then go to a third page to view a summary that combines both sets of data from the state. The data remains available as long as the user's session is active in the browser.

<aside class="negative">
Data stored in `st.session_state` is **not** persistent across different users or across closing and reopening the application. If you need to save data permanently, you would need to integrate file storage, a database, or cloud storage.
</aside>

## Exploring the Navigation
Duration: 02:00

The core navigation logic is handled in the main `app.py` file. Let's look at the relevant snippet:

```python
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
```

`st.sidebar.selectbox` creates a dropdown menu in the Streamlit sidebar. The `label` is the text displayed next to the selectbox, and `options` is a list of strings representing the choices available to the user.

When the user selects an option from the dropdown, the Streamlit script reruns. The `page` variable is updated with the selected string ("Budget Input", "Expense Tracking", or "Summary").

The subsequent `if/elif/else` block checks the value of the `page` variable and imports and calls the corresponding function (`run_budget_input`, `run_expense_tracking`, or `run_summary`) from the `application_pages` module. Each of these functions contains the Streamlit code specific to that page's layout and functionality.

This is a common pattern in Streamlit for creating multi-page applications without needing complex routing frameworks. Each "page" is essentially a function that gets called when selected via the sidebar.

## Conclusion and Enhancements
Duration: 03:00

Congratulations! You have successfully explored the Capital Budgeting Dashboard application built with Streamlit.

You've learned how the application allows users to:
*   Define budget categories and amounts.
*   Log individual expenses.
*   View a summary comparing budgeted vs. actual spending.
*   Analyze variances and identify overspending categories.
*   Visualize budget adherence and spending trends.

You've also gained insight into:
*   The modular structure using separate files for different functionalities.
*   How `st.session_state` is used to maintain data persistence across interactions and "pages".
*   How Streamlit's sidebar and `selectbox` can be used for simple application navigation.
*   Using `pandas` for data handling and calculations.
*   Using `plotly.express` for creating interactive visualizations within Streamlit.

This application provides a solid foundation for a personal budgeting tool. Here are some potential enhancements you could consider:

*   **Data Persistence:** Implement functionality to save and load budget and expense data to a file (like CSV or JSON) or a database so that the data is available across different sessions.
*   **Editing/Deleting Entries:** Add features to modify or remove existing budget categories or expense entries.
*   **Recurring Budgets/Expenses:** Allow users to set up recurring budget items or automatically log recurring expenses.
*   **More Advanced Reporting:** Add filters (e.g., by date range), more detailed reports, or additional chart types (e.g., pie charts for spending breakdown).
*   **Income Tracking:** Extend the application to also track income and provide a net financial position.
*   **User Accounts:** For a multi-user application, you would need a system for user authentication and separating data.

Experiment with the code, add new features, or modify existing ones to further enhance your understanding of building interactive data applications with Streamlit.

Thank you for completing this codelab!

