"""
app.py
-------
PakWallet main entry point.

Unauthenticated visitors see a branded login / registration screen.
Authenticated users see a quick-launch landing pad linking into the
multipage app (Dashboard, Calculators, Bills, Savings, AI Assistant,
Analytics) which lives under /pages.
"""

import streamlit as st

from auth.auth_utils import (
    authenticate_user,
    register_user,
    username_or_email_exists,
    validate_registration_inputs,
)
from config import APP_ICON, APP_NAME, APP_TAGLINE
from database.db import get_session, init_db
from utils.helpers import (
    hide_sidebar_nav_if_logged_out,
    initialize_session_state,
    render_sidebar,
)
from utils.styles import inject_custom_css, render_hero

# --------------------------------------------------------------------------
# Page config & bootstrap
# --------------------------------------------------------------------------
st.set_page_config(
    page_title=f"{APP_NAME} | {APP_TAGLINE}",
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="auto",
)

init_db()
initialize_session_state()
inject_custom_css()
hide_sidebar_nav_if_logged_out()


# --------------------------------------------------------------------------
# Logged-out experience: branded hero + Login / Register tabs
# --------------------------------------------------------------------------
def render_logged_out_view() -> None:
    render_hero(f"{APP_ICON} {APP_NAME}", APP_TAGLINE)

    col_left, col_right = st.columns([1, 1.3], gap="large")

    with col_left:
        st.markdown("#### Why PakWallet?")
        st.markdown(
            """
- 💼 One wallet for everyday spending, bills, and savings goals
- 🧮 Built-in calculators for loans, investments, education & Zakat
- 🤖 Rule-based AI assistant that reads your spending and coaches you
- 📊 Clear analytics on where your money actually goes
- 🔐 Hashed passwords, transaction PIN, and OTP-ready architecture
            """
        )
        st.caption(
            "This is a demo MVP. Wallet balances and bills are simulated — "
            "no real money moves and no real OTP/SMS is sent."
        )

    with col_right:
        tab_login, tab_register = st.tabs(["🔑 Login", "🆕 Create Account"])

        with tab_login:
            render_login_form()

        with tab_register:
            render_registration_form()


def render_login_form() -> None:
    with st.form("login_form", clear_on_submit=False):
        identifier = st.text_input("Username or Email")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login", use_container_width=True)

    if submitted:
        if not identifier or not password:
            st.error("Please enter both your username/email and password.")
            return

        with get_session() as session:
            user = authenticate_user(session, identifier, password)
            if user is None:
                st.error("Invalid credentials. Please try again.")
                return

            st.session_state["logged_in"] = True
            st.session_state["user_id"] = user.id
            st.session_state["username"] = user.username
            st.session_state["full_name"] = user.full_name
            st.session_state["email"] = user.email

        st.success(f"Welcome back, {st.session_state['full_name']}! 🎉")
        st.rerun()


def render_registration_form() -> None:
    with st.form("register_form", clear_on_submit=False):
        full_name = st.text_input("Full Name")
        c1, c2 = st.columns(2)
        with c1:
            username = st.text_input("Username")
        with c2:
            phone = st.text_input("Phone (optional)", placeholder="03xx-xxxxxxx")
        email = st.text_input("Email")

        c3, c4 = st.columns(2)
        with c3:
            password = st.text_input("Password", type="password")
        with c4:
            confirm_password = st.text_input("Confirm Password", type="password")

        c5, c6 = st.columns(2)
        with c5:
            pin = st.text_input("4-digit Transaction PIN", type="password", max_chars=4)
        with c6:
            confirm_pin = st.text_input("Confirm PIN", type="password", max_chars=4)

        st.caption(
            "Your Transaction PIN confirms bill payments and savings transfers — "
            "keep it separate from your login password."
        )
        submitted = st.form_submit_button("Create my PakWallet account", use_container_width=True)

    if submitted:
        is_valid, error_message = validate_registration_inputs(
            full_name, username, email, password, confirm_password, pin, confirm_pin
        )
        if not is_valid:
            st.error(error_message)
            return

        with get_session() as session:
            conflict = username_or_email_exists(session, username.strip(), email.strip().lower())
            if conflict:
                st.error(conflict)
                return

            register_user(session, full_name, username, email, phone, password, pin)

        st.success("Account created! Switch to the Login tab to sign in. 🎉")
        st.balloons()


# --------------------------------------------------------------------------
# Logged-in experience: quick-launch landing pad
# --------------------------------------------------------------------------
def render_logged_in_view() -> None:
    render_sidebar()
    render_hero(
        f"{APP_ICON} Welcome, {st.session_state.get('full_name', 'there')}!",
        APP_TAGLINE,
    )

    st.markdown("#### Jump to a section")
    nav_cols = st.columns(3)
    destinations = [
        ("📊 Dashboard", "pages/1_📊_Dashboard.py", "Balances, KPIs, and recent activity"),
        ("🧮 Calculators", "pages/2_💰_Mutual_Fund_Calculator.py", "SIP, EMI, Zakat, tax & more"),
        ("🎯 Savings Goals", "pages/8_🎯_Savings_Goals.py", "Emergency fund, Hajj, education"),
        ("🧾 Bill Payments", "pages/9_🧾_Bill_Payments.py", "Electricity, gas, internet, fees"),
        ("🤖 AI Budget Assistant", "pages/10_🤖_AI_Budget_Assistant.py", "Spending insights & tips"),
        ("📈 Analytics", "pages/11_📈_Analytics.py", "Trends, breakdowns, net worth"),
    ]
    for index, (label, target, description) in enumerate(destinations):
        with nav_cols[index % 3]:
            st.markdown(f'<div class="pw-card">', unsafe_allow_html=True)
            st.markdown(f"**{label}**")
            st.caption(description)
            st.page_link(target, label="Open", icon="➡️")
            st.markdown("</div>", unsafe_allow_html=True)

    st.divider()
    st.caption(
        "Use the sidebar to navigate any time. All figures in this MVP are "
        "demo data generated for your account — feel free to explore freely."
    )


# --------------------------------------------------------------------------
# Router
# --------------------------------------------------------------------------
if st.session_state.get("logged_in"):
    render_logged_in_view()
else:
    render_logged_out_view()
