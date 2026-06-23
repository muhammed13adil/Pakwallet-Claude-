"""
Calculators page - Financial calculation tools.
"""

import streamlit as st
from utils.styles import inject_custom_css, render_hero
from utils.helpers import render_sidebar, initialize_session_state, format_currency

inject_custom_css()
initialize_session_state()

if not st.session_state.get("logged_in"):
    st.error("Please log in first!")
    st.stop()

render_sidebar()
render_hero("🧮 Financial Calculators", "EMI, SIP, Zakat, Tax & More")

calculator_type = st.radio(
    "Select Calculator",
    ["EMI Calculator", "SIP Calculator", "Zakat Calculator", "Savings Calculator"]
)

if calculator_type == "EMI Calculator":
    st.markdown("### EMI (Equated Monthly Installment) Calculator")
    principal = st.number_input("Loan Amount (PKR)", min_value=0, value=500000)
    rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, value=10.0)
    months = st.number_input("Loan Duration (Months)", min_value=1, value=60)
    
    if principal > 0:
        monthly_rate = rate / 100 / 12
        if monthly_rate > 0:
            emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
            total_amount = emi * months
            total_interest = total_amount - principal
            
            st.success(f"Monthly EMI: {format_currency(emi)}")
            st.info(f"Total Amount: {format_currency(total_amount)}")
            st.info(f"Total Interest: {format_currency(total_interest)}")
        else:
            st.warning("Interest rate must be greater than 0")

elif calculator_type == "SIP Calculator":
    st.markdown("### SIP (Systematic Investment Plan) Calculator")
    monthly_investment = st.number_input("Monthly Investment (PKR)", min_value=0, value=5000)
    annual_return = st.number_input("Expected Annual Return (%)", min_value=0.0, value=12.0)
    years = st.number_input("Investment Period (Years)", min_value=1, value=10)
    
    if monthly_investment > 0:
        months = years * 12
        monthly_return = annual_return / 100 / 12
        
        if monthly_return > 0:
            future_value = monthly_investment * (((1 + monthly_return) ** months - 1) / monthly_return)
            total_invested = monthly_investment * months
            gains = future_value - total_invested
            
            st.success(f"Future Value: {format_currency(future_value)}")
            st.info(f"Total Invested: {format_currency(total_invested)}")
            st.info(f"Investment Gains: {format_currency(gains)}")
        else:
            st.warning("Return rate must be greater than 0")

elif calculator_type == "Zakat Calculator":
    st.markdown("### Zakat Calculator")
    total_wealth = st.number_input("Total Wealth/Assets (PKR)", min_value=0, value=100000)
    liabilities = st.number_input("Liabilities (PKR)", min_value=0, value=0)
    
    net_wealth = total_wealth - liabilities
    zakat_threshold = 195000  # Nisab value (approximate)
    
    if net_wealth >= zakat_threshold:
        zakat_amount = net_wealth * 0.025  # 2.5% of net wealth
        st.success(f"Zakat Due: {format_currency(zakat_amount)}")
    else:
        st.info(f"Net Wealth Below Nisab ({format_currency(zakat_threshold)}). Zakat not required.")

else:  # Savings Calculator
    st.markdown("### Savings Goal Calculator")
    target_amount = st.number_input("Target Savings Amount (PKR)", min_value=0, value=500000)
    monthly_saving = st.number_input("Monthly Savings (PKR)", min_value=0, value=10000)
    
    if monthly_saving > 0:
        months_needed = target_amount / monthly_saving
        years = months_needed / 12
        st.success(f"Time to Reach Goal: {months_needed:.0f} months ({years:.1f} years)")
    else:
        st.warning("Monthly savings must be greater than 0")
