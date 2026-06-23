"""
Savings Goals page - Track and manage savings targets.
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
render_hero("🎯 Savings Goals", "Track your financial aspirations")

st.markdown("### Your Savings Goals")

# Demo savings goals
goals = [
    {"name": "Emergency Fund", "target": 200000, "current": 75000, "category": "Emergency"},
    {"name": "Hajj Trip", "target": 500000, "current": 150000, "category": "Travel"},
    {"name": "Home Down Payment", "target": 1000000, "current": 250000, "category": "Home"},
    {"name": "Education Fund", "target": 300000, "current": 100000, "category": "Education"},
]

for goal in goals:
    progress = goal["current"] / goal["target"]
    remaining = goal["target"] - goal["current"]
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"**{goal['name']}** ({goal['category']})")
        st.progress(progress)
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.caption(f"Target: {format_currency(goal['target'])}")
        with col_b:
            st.caption(f"Saved: {format_currency(goal['current'])}")
        with col_c:
            st.caption(f"Remaining: {format_currency(remaining)}")

st.divider()
st.markdown("### Add New Savings Goal")

with st.form("new_goal_form"):
    goal_name = st.text_input("Goal Name", placeholder="e.g., Wedding, House, Education")
    goal_category = st.selectbox("Category", ["Emergency", "Travel", "Home", "Education", "Vehicle", "Other"])
    target_amount = st.number_input("Target Amount (PKR)", min_value=1000, step=10000)
    col1, col2 = st.columns(2)
    with col1:
        monthly_contribution = st.number_input("Monthly Contribution (PKR)", min_value=1000, step=1000)
    with col2:
        if monthly_contribution > 0:
            months = target_amount / monthly_contribution
            st.caption(f"Expected Duration: {months:.0f} months ({months/12:.1f} years)")
    
    if st.form_submit_button("Create Goal", use_container_width=True):
        st.success(f"✅ Savings goal '{goal_name}' created successfully!")
