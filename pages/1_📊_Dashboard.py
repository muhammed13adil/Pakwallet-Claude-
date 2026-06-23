"""
Dashboard page - Main overview for authenticated users.
"""

import streamlit as st
from utils.styles import inject_custom_css, render_hero, render_stat_card
from utils.helpers import render_sidebar, initialize_session_state, format_currency

inject_custom_css()
initialize_session_state()

if not st.session_state.get("logged_in"):
    st.error("Please log in first!")
    st.stop()

render_sidebar()
render_hero("📊 Dashboard", "Your wallet at a glance")

st.markdown("### Account Overview")

col1, col2, col3 = st.columns(3)
with col1:
    render_stat_card("Total Balance", format_currency(50000), "💰")
with col2:
    render_stat_card("Monthly Income", format_currency(25000), "📈")
with col3:
    render_stat_card("Monthly Expenses", format_currency(15000), "📉")

st.divider()
st.markdown("### Recent Transactions")
st.info("Transaction history will appear here.")

st.divider()
st.markdown("### Quick Actions")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Add Income", use_container_width=True):
        st.success("Feature coming soon!")
with col2:
    if st.button("Pay Bill", use_container_width=True):
        st.success("Feature coming soon!")
with col3:
    if st.button("Transfer to Savings", use_container_width=True):
        st.success("Feature coming soon!")
