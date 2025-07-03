
import streamlit as st
import pandas as pd

def run_budget_input():
    st.header("Input Budget Categories and Amounts")
    if 'budget_df' not in st.session_state:
        # Initialize DataFrame
        st.session_state['budget_df'] = pd.DataFrame(columns=["Category", "Budgeted"])

    df = st.session_state['budget_df']

    with st.form("add_category_form", clear_on_submit=True):
        category = st.text_input("Category Name")
        amount = st.number_input("Budgeted Amount", min_value=0.0, format="%.2f")
        submitted = st.form_submit_button("Add/Update Category")
        if submitted and category:
            if category in df['Category'].values:
                df.loc[df['Category'] == category, 'Budgeted'] = amount
            else:
                df = pd.concat([df, pd.DataFrame([[category, amount]], columns=["Category", "Budgeted"])], ignore_index=True)
            st.session_state['budget_df'] = df

    if not df.empty:
        st.subheader("Current Budget Plan")
        st.dataframe(df.set_index('Category'))

