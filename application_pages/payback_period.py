
import streamlit as st
import plotly.graph_objects as go

def run_payback_period():
    st.title("Payback Period Calculation")
    st.markdown("""
    This page calculates the payback period of a project. The payback period is the time it takes for a project to recoup its initial investment.
    """)
    initial_investment = st.number_input("Initial Investment:", value=100000, step=1000)
    cashflows = st.text_area("Cash Flows (comma-separated):", value="20000, 30000, 40000, 50000")
    try:
        cashflows_list = [float(x) for x in cashflows.split(',')]
        cumulative_cashflow = 0
        payback_period = 0
        for i, cashflow in enumerate(cashflows_list):
            cumulative_cashflow += cashflow
            if cumulative_cashflow >= initial_investment:
                payback_period = i + 1
                break
        if payback_period > 0:
            st.write(f"Payback Period: {payback_period} years")
            fig = go.Figure(data=[go.Bar(x=list(range(len(cashflows_list))), y=cashflows_list)])
            st.plotly_chart(fig)
        else:
            st.write("The project does not pay back the initial investment.")

    except ValueError:
        st.error("Invalid cash flow input. Please use comma-separated numbers.")
