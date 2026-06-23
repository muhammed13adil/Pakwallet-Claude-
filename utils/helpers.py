"""
utils/helpers.py
----------------
Helper functions for PakWallet UI and session management.
"""

import streamlit as st


def initialize_session_state() -> None:
    """Initialize Streamlit session state variables."""
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    if "user_id" not in st.session_state:
        st.session_state["user_id"] = None
    if "username" not in st.session_state:
        st.session_state["username"] = None
    if "full_name" not in st.session_state:
        st.session_state["full_name"] = None
    if "email" not in st.session_state:
        st.session_state["email"] = None


def hide_sidebar_nav_if_logged_out() -> None:
    """Hide sidebar navigation for logged-out users."""
    if not st.session_state.get("logged_in"):
        st.set_page_config(initial_sidebar_state="collapsed")


def render_sidebar() -> None:
    """Render the sidebar navigation for logged-in users."""
    with st.sidebar:
        st.markdown(f"### Welcome, {st.session_state.get('full_name', 'User')}!")
        st.markdown("---")
        
        pages = {
            "Dashboard": "pages/1_📊_Dashboard.py",
            "Calculators": "pages/2_💰_Mutual_Fund_Calculator.py",
            "Savings Goals": "pages/8_🎯_Savings_Goals.py",
            "Bill Payments": "pages/9_🧾_Bill_Payments.py",
            "AI Assistant": "pages/10_🤖_AI_Budget_Assistant.py",
            "Analytics": "pages/11_📈_Analytics.py",
        }
        
        for label, target in pages.items():
            st.page_link(target, label=label)
        
        st.markdown("---")
        if st.button("Logout", use_container_width=True):
            st.session_state["logged_in"] = False
            st.session_state["user_id"] = None
            st.session_state["username"] = None
            st.session_state["full_name"] = None
            st.session_state["email"] = None
            st.rerun()


def format_currency(amount: float, currency: str = "PKR") -> str:
    """
    Format amount as currency.
    
    Args:
        amount: Numeric amount
        currency: Currency code (default: PKR)
        
    Returns:
        Formatted currency string
    """
    if currency == "PKR":
        return f"₨{amount:,.2f}"
    return f"{currency} {amount:,.2f}"


def calculate_percentage_change(current: float, previous: float) -> float:
    """
    Calculate percentage change between two values.
    
    Args:
        current: Current value
        previous: Previous value
        
    Returns:
        Percentage change
    """
    if previous == 0:
        return 0
    return ((current - previous) / previous) * 100
