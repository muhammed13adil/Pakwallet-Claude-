"""
AI Budget Assistant page - AI-powered spending insights.
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
render_hero("🤖 AI Budget Assistant", "Smart spending insights and recommendations")

st.markdown("### Your Spending Analysis")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Monthly Income", format_currency(25000), "+5%")
with col2:
    st.metric("Monthly Expenses", format_currency(15000), "-10%")
with col3:
    st.metric("Savings Rate", "40%", "+8%")

st.divider()
st.markdown("### AI Insights")

insights = [
    "💡 Your food spending increased 25% this month. Try meal planning!",
    "✨ Great job! You saved 40% more this month compared to last month.",
    "🎯 To reach your Hajj goal in 3 years, save ₨13,889 monthly.",
    "⚠️ Your entertainment spending is 15% above average. Consider reducing.",
    "🌟 You've maintained a consistent savings rate for 6 months. Keep it up!",
]

for insight in insights:
    st.info(insight)

st.divider()
st.markdown("### Ask the AI Assistant")

user_question = st.text_area("Ask for financial advice or insights:")

if st.button("Get Advice", use_container_width=True):
    if user_question:
        st.markdown("### AI Response")
        st.info(
            "🤖 Based on your spending patterns, I recommend:\n\n"
            "1. Create a budget for discretionary spending\n"
            "2. Track your expenses daily\n"
            "3. Set up automatic transfers to savings\n"
            "4. Review your subscriptions monthly"
        )
    else:
        st.warning("Please ask a question first!")
