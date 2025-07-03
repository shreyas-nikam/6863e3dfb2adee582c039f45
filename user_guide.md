id: 6863e3dfb2adee582c039f45_user_guide
summary: Capital budgeting User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Budget Management Dashboard: A User Guide

## Introduction to Budget Management
Duration: 0:05:00

Welcome to the Capital Budgeting Dashboard user guide! This application is designed to help you take control of your finances by providing a clear overview of your spending compared to your financial plan. Understanding where your money goes is the first step towards achieving your financial goals.

The core idea behind this application is **Budgeting**, which is simply creating a plan for your money. You decide how much you *intend* to spend in different areas (categories) over a specific period. This is your **Budgeted** amount.

As you spend, you track your actual expenses. This is your **Actual** spending.

The application then helps you perform **Variance Analysis**. This involves comparing your **Actual** spending to your **Budgeted** amount to see if you stayed within your plan, spent more, or spent less. The difference is called the **Variance**.

The key formulas used are:

*   **Variance:** The difference between how much you actually spent and how much you planned to spend. A positive variance means you spent more than planned, while a negative variance means you spent less.
    $$ \text{Variance} = \text{Actual} - \text{Budgeted} $$
*   **Percentage Variance:** This tells you the variance relative to your budget, expressed as a percentage.
    $$ \text{Percentage Variance} = \frac{\text{Actual} - \text{Budgeted}}{\text{Budgeted}} \times 100 $$

Understanding these concepts through this dashboard empowers you to make informed decisions about your spending and identify areas where you might need to adjust your habits or your budget.

<aside class="positive">
Using a budget helps you visualize your financial health and work towards your financial goals more effectively.
</aside>

## Defining Your Budget Categories
Duration: 0:03:00

Before you can track your spending, you need to define the areas or categories you want to budget for. This could be anything from 'Groceries' and 'Utilities' to 'Entertainment' and 'Savings'.

Look for the section titled **Define Budget Categories**.

1.  **Enter Category Name:** In the text box labeled "Category Name", type the name of a spending category (e.g., "Rent", "Groceries", "Transportation").
2.  **Enter Budgeted Amount:** In the number input labeled "Budgeted Amount", enter the amount you plan to spend on this category for your budgeting period. This is your target. You can use the up/down arrows or type the number directly.
3.  **Add Category:** Click the "Add Category" button.

The application will add this category to your budget plan. You should see a success message confirming it was added. Repeat this process for all the categories you want to include in your budget.

<aside class="positive">
Start with a few major categories and add more as you get comfortable with the process. You can always add or adjust categories later.
</aside>

## Logging Your Expenses
Duration: 0:05:00

As you spend money, it's crucial to record these expenses so the dashboard can track your actual spending.

Look for the section titled **Log Expenses**. This section uses a form to help you record your spending details accurately.

1.  **Select Expense Category:** Click on the dropdown menu labeled "Expense Category". This list will contain the categories you defined in the previous step. Choose the category that the expense belongs to.
2.  **Select Date of Expense:** Use the date picker labeled "Date of Expense" to select the date you incurred the expense.
3.  **Enter Expense Amount:** In the number input labeled "Expense Amount", enter the exact amount you spent for this expense.
4.  **Submit Expense:** Click the "Add Expense" button within the form.

When you submit the form, the application records this expense and updates the 'Actual' spending amount for the chosen category in your budget data. You'll see a success message. Continue logging expenses as they occur to keep your data up-to-date.

## Viewing Your Budget Summary
Duration: 0:04:00

With categories defined and expenses logged, the application automatically calculates your budget summary and variance analysis.

Scroll down to the section titled **Budget Summary**.

Here, you will see a table (a dataframe) displaying the key information for each of your budget categories:

*   **Category:** The name of the spending area you defined.
*   **Budgeted:** The amount you planned to spend.
*   **Actual:** The total amount you have logged as spent in this category so far.
*   **Variance:** The difference between your Actual spending and your Budgeted amount ($\text{Actual} - \text{Budgeted}$). A positive number here means you've spent over budget, and a negative number means you've spent under budget.
*   **Percentage Variance:** The variance expressed as a percentage of your Budgeted amount. This helps you see how significant the variance is relative to the planned amount.

<aside class="negative">
Keep an eye on categories with large positive variances or high percentage variances. These are areas where you might be overspending significantly compared to your plan.
</aside>

This table provides a quick snapshot of where you stand financially for each category.

## Understanding Visualizations
Duration: 0:03:00

Seeing numbers in a table is useful, but visualizations can make the information much easier to understand and identify patterns.

Scroll down to the section titled **Visualizations**.

*   **Budgeted vs Actual Spending Bar Chart:** This bar chart visually compares your planned (Budgeted) spending against your actual spending for each category. Categories are shown on the horizontal axis (x-axis), and the amounts on the vertical axis (y-axis). You can quickly see which categories are close to budget, significantly over budget, or under budget by comparing the heights of the 'Budgeted' (blue) and 'Actual' (red) bars.
*   **Spending Trends:** Below the main bar chart, you'll find line charts showing the trend of your expenses for each category *over time*. Currently, this basic implementation shows the amount of each expense transaction for a category plotted sequentially. If you've logged multiple expenses for a category, you'll see how the amounts vary with each transaction. This is a basic form of **Trend Analysis**, helping you spot patterns in your spending habits.

<aside class="positive">
Visualizations make it easy to quickly identify your biggest spending areas and where you are exceeding your budget at a glance.
</aside>

## Interpreting Alerts
Duration: 0:02:00

The application includes a simple alert system to draw your attention to critical situations.

Scroll down to the section titled **Alerts**.

This section will display warnings if your actual spending in any category has exceeded the budgeted amount.

*   **Overspending Alert:** If the 'Variance' for a category is a positive number (meaning $\text{Actual} > \text{Budgeted}$), you will see a warning message highlighting which category is over budget and by how much.

<aside class="negative">
Pay close attention to these alerts. They signal areas that require immediate attention to get your spending back on track with your budget.
</aside>

By using the Budget Summary table, the Visualizations, and the Alerts together, you gain a comprehensive understanding of your spending habits and your progress towards your financial goals. Regularly defining categories, logging expenses, and reviewing this dashboard is key to effective budget management.

