"""
Analytics page - Financial analytics and insights.
"""

import streamlit as st
import pandas as pd
from utils.styles import inject_custom_css, render_hero
from utils.helpers import render_sidebar, initialize_session_state, format_currency

inject_custom_css()
initialize_session_state()

if not st.session_state.get("logged_in"):
    st.error("Please log in first!")
    st.stop()

render_sidebar()
render_hero("📈 Analytics", "Detailed financial analytics")

st.markdown("### Spending by Category")

# Demo spending data
spending_data = {
    "Category": ["Food & Groceries", "Transportation", "Utilities", "Entertainment", "Healthcare", "Other"],
    "Amount": [5000, 3000, 2000, 2500, 1500, 1000],
}
df = pd.DataFrame(spending_data)

col1, col2 = st.columns(2)
with col1:
    st.bar_chart(df.set_index("Category"))
with col2:
    st.pie_chart(df.set_index("Category")["Amount"])

st.divider()
st.markdown("### Income vs Expenses (Last 6 Months)")

# Demo monthly data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
income = [25000, 25000, 26000, 25000, 27000, 25000]
expenses = [18000, 16000, 17500, 15000, 14500, 15000]

monthly_data = pd.DataFrame({
    "Month": months,
    "Income": income,
    "Expenses": expenses,
})

st.line_chart(monthly_data.set_index("Month"))

st.divider()
st.markdown("### Financial Summary")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Income (6M)", format_currency(153000))
with col2:
    st.metric("Total Expenses (6M)", format_currency(96000))
with col3:
    st.metric("Net Savings (6M)", format_currency(57000))
with col4:
    st.metric("Savings Rate", "37.3%")

st.divider()
st.markdown("### Net Worth Breakdown")

assets = {
    "Cash": 50000,
    "Savings Goals": 500000,
    "Investments": 250000,
}

liabilities = {
    "Loans": 100000,
}

net_worth = sum(assets.values()) - sum(liabilities.values())

st.metric("Total Net Worth", format_currency(net_worth))

col1, col2 = st.columns(2)
with col1:
    st.markdown("**Assets**")
    for asset, value in assets.items():
        st.caption(f"{asset}: {format_currency(value)}")
with col2:
    st.markdown("**Liabilities**")
    for liability, value in liabilities.items():
        st.caption(f"{liability}: {format_currency(value)}")
