
import streamlit as st
import pandas as pd
import plotly.express as px

def run_summary():
    st.header("Budget vs. Actual Expenses Summary")
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

    # Merge budget and expenses
    merged = pd.merge(budget_df, expense_sum, on='Category', how='left')
    merged['Amount'] = merged['Amount'].fillna(0)
    merged['Variance'] = merged['Budgeted'] - merged['Amount']
    merged['Percent Variance'] = (merged['Variance'] / merged['Budgeted']) * 100

    st.subheader("Budget and Expenses Comparison")
    st.dataframe(merged.set_index('Category'))

    # Visualization: Budget vs. Actual
    fig = px.bar(merged, x='Category', y=['Budgeted', 'Amount'], barmode='group',
                 labels={'value':'Amount', 'variable':'Type'}, title='Budget vs. Actual Spending')
    st.plotly_chart(fig)

    # Highlight overspending
    overspent = merged[merged['Variance'] < 0]
    if not overspent.empty:
        st.warning("Over-spent in the following categories:")
        st.dataframe(overspent.set_index('Category'))

    # Trends over time per category
    expenses_df['Date'] = pd.to_datetime(expenses_df['Date'])
    categories = merged['Category'].tolist()
    for cat in categories:
        cat_data = expenses_df[expenses_df['Category'] == cat].sort_values('Date')
        if not cat_data.empty:
            fig_trend = px.line(cat_data, x='Date', y='Amount', title=f"Spending Trend: {cat}")
            st.plotly_chart(fig_trend)

