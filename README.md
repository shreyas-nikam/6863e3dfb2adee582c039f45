# Capital Budgeting & Financial Analysis Lab (QuLab)

![QuLab Logo](https://www.quantuniversity.com/assets/img/logo5.jpg)

This repository hosts a Streamlit application designed as a laboratory project to explore fundamental capital budgeting concepts and financial analysis techniques. Developed for educational purposes, it provides interactive tools for understanding Budget vs. Actual spending, Net Present Value (NPV), and Payback Period calculations, crucial for effective financial decision-making in projects and investments.

## Table of Contents

-   [Project Title and Description](#project-title-and-description)
-   [Features](#features)
-   [Getting Started](#getting-started)
    -   [Prerequisites](#prerequisites)
    -   [Installation](#installation)
-   [Usage](#usage)
-   [Project Structure](#project-structure)
-   [Technology Stack](#technology-stack)
-   [Contributing](#contributing)
-   [License](#license)
-   [Contact](#contact)

## Project Title and Description

**QuLab: Capital Budgeting and Financial Analysis**

This Streamlit application serves as an interactive educational tool for financial concepts. It aims to demystify key capital budgeting methods through a user-friendly interface, allowing users to input data and instantly visualize results for various financial analyses. It covers the post-audit phase (Budget vs. Actual) and project evaluation techniques (NPV, Payback Period).

## Features

The application currently includes the following interactive modules:

*   **Interactive Navigation**: Seamlessly switch between different analysis modules using the sidebar.
*   **Budget vs. Actual Spending Analysis**:
    *   Visually compare planned expenditures against actual spending.
    *   Illustrates the concept of budget variance, vital for financial control and post-audit evaluation in capital budgeting.
    *   (Note: The current implementation uses static data but is designed to be extensible for interactive input.)
*   **Net Present Value (NPV) Calculation**:
    *   Calculate the NPV of a project by providing initial investment, discount rate, and a series of future cash flows.
    *   Helps in determining the profitability of an investment by discounting future cash flows to their present value.
    *   Visualizes cash flows using a bar chart.
*   **Payback Period Calculation**:
    *   Determine the time required for an investment to generate enough cash flow to recover its initial cost.
    *   Provides a quick measure of a project's liquidity and risk.
    *   Visualizes cash flows using a bar chart.
*   **User-Friendly Interface**: Built with Streamlit, offering a clean and intuitive web interface for financial exploration.

## Getting Started

Follow these instructions to set up and run the application on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:

*   **Python**: Version 3.7 or higher. You can download it from [python.org](https://www.python.org/downloads/).
*   **pip**: Python's package installer, usually comes with Python.

### Installation

1.  **Clone the Repository**:
    First, clone this Git repository to your local machine:
    ```bash
    git clone https://github.com/your-username/qucapitalbudgeting-lab.git
    cd qucapitalbudgeting-lab
    ```
    (Replace `your-username/qucapitalbudgeting-lab` with the actual repository URL if different).

2.  **Create a Virtual Environment (Recommended)**:
    It's good practice to create a virtual environment to manage dependencies:
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment**:
    *   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies**:
    Install all required Python packages using `pip`. Create a `requirements.txt` file with the following content:

    ```
    streamlit
    plotly
    numpy
    ```

    Then, install them:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

After completing the installation steps, you can run the Streamlit application:

1.  **Navigate to the project root directory** (where `app.py` is located) in your terminal.
2.  **Run the application** using Streamlit:
    ```bash
    streamlit run app.py
    ```

    This command will open a new tab in your default web browser displaying the Streamlit application. If it doesn't open automatically, you can navigate to `http://localhost:8501` (or the address displayed in your terminal).

3.  **Interact with the Application**:
    *   Use the `Navigation` dropdown in the sidebar to switch between different financial analysis modules.
    *   Input values into the designated fields on each page to see calculations and visualizations update in real-time.

## Project Structure

The project is organized to keep the main application logic separate from the individual page implementations:

```
qucapitalbudgeting-lab/
├── app.py                      # Main Streamlit application file, handles navigation and page routing.
├── application_pages/          # Directory containing individual financial analysis modules.
│   ├── budget_actual.py        # Module for Budget vs. Actual spending analysis.
│   ├── npv_calculation.py      # Module for Net Present Value (NPV) calculations.
│   └── payback_period.py       # Module for Payback Period calculations.
└── requirements.txt            # Lists all Python dependencies required for the project.
```

## Technology Stack

This application is built using the following technologies:

*   **Python**: The core programming language.
*   **Streamlit**: For creating interactive web applications with pure Python.
*   **Plotly**: For generating dynamic and interactive charts and visualizations.
*   **NumPy**: For numerical operations, especially in financial calculations.

## Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please follow these steps:

1.  **Fork** the repository.
2.  **Create** a new branch (`git checkout -b feature/YourFeatureName`).
3.  **Make** your changes.
4.  **Commit** your changes (`git commit -m 'Add new feature'`).
5.  **Push** to the branch (`git push origin feature/YourFeatureName`).
6.  **Open** a Pull Request.

Please ensure your code adheres to good practices and includes relevant documentation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details (you would typically create a `LICENSE` file in your repository with the full MIT license text).

## Contact

For questions or feedback, please reach out:

*   **Project Maintainer**: QuantUniversity Lab Team
*   **Email**: lab@quantuniversity.com
*   **Website**: [www.quantuniversity.com](https://www.quantuniversity.com)
