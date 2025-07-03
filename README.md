# Capital Budgeting and Budget Tracking Dashboard

This repository contains the code for a Streamlit-based web application designed as a lab project for exploring financial concepts related to budgeting and variance analysis, particularly within the context of capital budgeting principles. While the broader topic is Capital Budgeting, this specific application focuses on managing and analyzing a budget by tracking planned (budgeted) versus actual expenses.

The application allows users to define budget categories, log expenses against these categories, and view a summary comparing the planned budget to actual spending. It highlights variances, calculates percentage variances, and provides visual aids to understand spending patterns.

## Features

*   **Budget Input:** Define different spending categories and set a budgeted amount for each.
*   **Expense Tracking:** Log individual expenses, associating them with a specific category and date.
*   **Budget Summary:** View a table comparing the budgeted amount, actual spent amount, variance (Budgeted - Actual), and percentage variance for each category.
*   **Budget vs. Actual Visualization:** A bar chart visually comparing budgeted versus actual spending per category.
*   **Overspending Alerts:** Highlights categories where actual spending exceeds the budgeted amount.
*   **Spending Trend Analysis:** Line charts showing the trend of expenses over time for each category.
*   **Navigation:** Easy navigation between the Budget Input, Expense Tracking, and Summary sections via a sidebar.

## Getting Started

### Prerequisites

*   Python 3.7 or higher
*   `pip` (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url> # Replace with the actual repository URL
    cd <repository_name>
    ```
2.  **Install dependencies:**
    Create a `requirements.txt` file in the root directory of the project with the following content:
    ```
    streamlit
    pandas
    plotly
    ```
    Then, install the libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the application:**
    Navigate to the project's root directory in your terminal and run the following command:
    ```bash
    streamlit run app.py
    ```
2.  **Access the application:**
    Your web browser should automatically open to the application's local address (usually `http://localhost:8501`). If not, open your browser and go to that address.
3.  **Navigate:**
    Use the sidebar on the left to switch between different sections: "Budget Input", "Expense Tracking", and "Summary".
4.  **Define Budget:**
    Go to the "Budget Input" page to add your spending categories and their budgeted amounts.
5.  **Log Expenses:**
    Go to the "Expense Tracking" page to record your actual expenses, selecting the relevant category and entering the amount and date.
6.  **View Summary & Analysis:**
    Go to the "Summary" page to see the comparison between your budget and actual spending, including variances, visualizations, and overspending alerts.

## Project Structure

```
.
├── app.py                      # Main Streamlit application entry point and navigation
├── application_pages/          # Directory containing individual page modules
│   ├── __init__.py             # Makes application_pages a Python package
│   ├── budget_input.py         # Handles budget category and amount input
│   ├── expense_tracking.py     # Handles logging individual expenses
│   └── summary.py              # Handles data aggregation, calculations, and visualizations
└── requirements.txt            # Lists Python dependencies
```

*Note: The code snippets provided for `app.py` included two different versions. This README is based on the second version of `app.py` and the corresponding page files (`budget_input.py`, `expense_tracking.py`, `summary.py`). The `application_pages/budgeting.py` file is not used in the second `app.py` version.*

## Technology Stack

*   **Python:** The core programming language.
*   **Streamlit:** Framework for building the web application user interface.
*   **Pandas:** Library for data manipulation and analysis (managing budget and expense dataframes).
*   **Plotly:** Library for creating interactive visualizations (bar charts and line charts).

## Contributing

This application is presented as a lab project generated using the QuCreate platform. Contributions in the standard open-source model (e.g., pull requests) are not typically applicable for this specific type of educational material.

If you have questions or feedback related to the lab content, please refer to the guidelines provided by the educational institution or platform (QuantUniversity).

## License

This lab project and its code are provided for educational use and illustration purposes only.

© 2025 QuantUniversity. All Rights Reserved.

Any reproduction or distribution of this demonstration material requires prior written consent from QuantUniversity.

The code was generated using the QuCreate platform, which relies on AI models that may produce inaccuracies or errors.

## Contact

For inquiries related to this lab or the QuCreate platform, please refer to QuantUniversity's official website or contact channels.

*   **QuantUniversity Website:** [https://www.quantuniversity.com/](https://www.quantuniversity.com/)
