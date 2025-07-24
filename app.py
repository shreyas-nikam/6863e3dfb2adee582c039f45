
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
