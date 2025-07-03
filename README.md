# Capital Budgeting Dashboard - Streamlit Application

An interactive Streamlit application designed to help users visualize and manage their budget by comparing planned (budgeted) spending against actual expenses. This tool aids in understanding spending habits, identifying variances, and making informed financial decisions.

## Description

This application serves as a simple capital budgeting dashboard. It allows users to define budget categories, log expenses against those categories, and view a summary comparison of budgeted versus actual spending. The dashboard calculates variances, visualizes spending patterns, and provides alerts for potential overspending.

It's built using Streamlit for the interactive user interface, Pandas for data handling, and Plotly for dynamic visualizations. The application utilizes Streamlit's session state to maintain data persistence within a single user session.

Key concepts illustrated by this application include:

*   **Budgeting:** Setting financial targets for different spending categories.
*   **Variance Analysis:** Comparing planned vs. actual figures to identify deviations.
*   **Trend Analysis:** Observing spending patterns over time (basic implementation).

The core calculations used are:

*   **Variance:** $$\text{Variance} = \text{Actual} - \text{Budgeted}$$
*   **Percentage Variance:** $$\text{Percentage Variance} = \frac{\text{Actual} - \text{Budgeted}}{\text{Budgeted}} \times 100$$

## Features

*   Define custom budget categories with specified budgeted amounts.
*   Log individual expenses, associating them with defined categories and dates.
*   View a comprehensive summary table showing budgeted amount, actual spending, calculated variance, and percentage variance for each category.
*   Visualize budgeted vs. actual spending per category using interactive bar charts.
*   View basic spending trends over time for each category (line charts).
*   Receive alerts for categories where actual spending exceeds the budgeted amount.
*   Simple and intuitive user interface powered by Streamlit.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python installed on your system. This project is compatible with Python 3.7+.

You will also need `pip`, which usually comes bundled with Python.

### Installation

1.  **Clone the repository (or download the code):**
    ```bash
    git clone <repository_url> # Replace <repository_url> with the actual URL
    cd <project_directory> # Navigate into the project folder
    ```
    If you downloaded the files manually, navigate to the folder containing `app.py`.

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    *   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    *   On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required dependencies:**
    Create a `requirements.txt` file in the project's root directory with the following content:
    ```
    streamlit
    pandas
    plotly
    ```
    Then, install the packages using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the Streamlit application:**
    Make sure your virtual environment is activated (if you created one).
    Open your terminal or command prompt, navigate to the project's root directory (where `app.py` is located), and run:
    ```bash
    streamlit run app.py
    ```

2.  **Access the application:**
    The application will open in your default web browser, typically at `http://localhost:8501`.

3.  **Interact with the Dashboard:**
    *   Use the sidebar to navigate between pages (currently only "Budget Overview").
    *   On the "Budget Overview" page:
        *   Define your budget categories and budgeted amounts in the "Define Budget Categories" section. Click "Add Category".
        *   Log your expenses using the "Log Expenses" form. Select the category, date, and amount. Click "Add Expense".
        *   Observe the "Budget Summary" table and the visualizations ("Budgeted vs Actual Spending", "Spending Trends") update automatically as you add data.
        *   Check the "Alerts" section for any categories exceeding their budget.

*Note: Data entered into the application is stored only for the duration of your current session in the browser. Refreshing the page will clear all entered data.*

## Project Structure

```
.
├── app.py
└── application_pages/
    └── page1.py
└── requirements.txt (optional, but recommended)
```

*   `app.py`: The main entry point of the Streamlit application. Handles basic layout, navigation, and includes introductory text. It imports and runs the appropriate page module based on user selection.
*   `application_pages/`: A directory intended to hold separate Python modules for different pages or sections of the application.
*   `application_pages/page1.py`: Contains the Streamlit code for the "Budget Overview" page, including data input forms, data processing, display, and visualizations.
*   `requirements.txt`: Lists the necessary Python packages for the project.

## Technology Stack

*   **Frontend/Backend Framework:** Streamlit
*   **Data Manipulation:** Pandas
*   **Data Visualization:** Plotly Express
*   **Language:** Python

## Contributing

This project is primarily intended as a lab demonstration and educational resource. Contributions are not actively being sought for this specific lab version.

## License

This application is provided for educational use and illustration purposes only.

© 2025 QuantUniversity. All Rights Reserved.

Any reproduction or distribution of this demonstration or its code requires prior written consent from QuantUniversity.

*Disclaimer: This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors.*

## Contact

For inquiries regarding this project or QuantUniversity, please visit the QuantUniversity website:

[https://www.quantuniversity.com/](https://www.quantuniversity.com/)
