
import streamlit as st
import plotly.graph_objects as go
import numpy as np

def run_npv_calculation():
    st.title("Net Present Value (NPV) Calculation")
    st.markdown("""
    This page demonstrates how to calculate the Net Present Value (NPV) of a project. NPV is a crucial metric in capital budgeting, helping determine the profitability of an investment.
    """)
    initial_investment = st.number_input("Initial Investment:", value=100000, step=1000)
    discount_rate = st.number_input("Discount Rate (%):", value=10, step=1) / 100
    cashflows = st.text_area("Cash Flows (comma-separated):", value="20000, 30000, 40000, 50000")
    try:
        cashflows_list = [float(x) for x in cashflows.split(',')]
        npv = -initial_investment + np.sum([cf / (1 + discount_rate)**i for i, cf in enumerate(cashflows_list)])
        st.write(f"Net Present Value (NPV): {npv:.2f}")

        fig = go.Figure(data=[go.Bar(x=list(range(len(cashflows_list))), y=cashflows_list)])
        st.plotly_chart(fig)

    except ValueError:
        st.error("Invalid cash flow input. Please use comma-separated numbers.")

