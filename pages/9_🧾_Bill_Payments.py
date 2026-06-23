"""
Bill Payments page - Manage recurring bills.
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
render_hero("🧾 Bill Payments", "Manage your recurring bills")

st.markdown("### Upcoming Bills")

# Demo bills
bills = [
    {"name": "Electricity", "amount": 2500, "due_date": 15, "paid": False},
    {"name": "Internet", "amount": 1500, "due_date": 5, "paid": True},
    {"name": "Gas", "amount": 800, "due_date": 20, "paid": False},
    {"name": "Mobile Phone", "amount": 500, "due_date": 10, "paid": False},
]

for i, bill in enumerate(bills):
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
    with col1:
        status = "✅ Paid" if bill["paid"] else "⏳ Pending"
        st.markdown(f"**{bill['name']}** - {status}")
    with col2:
        st.caption(f"Due: {bill['due_date']}th")
    with col3:
        st.caption(format_currency(bill['amount']))
    with col4:
        if not bill["paid"]:
            if st.button("Pay", key=f"pay_{i}", use_container_width=True):
                st.success(f"{bill['name']} payment processed!")

st.divider()
st.markdown("### Add New Bill")

with st.form("new_bill_form"):
    bill_name = st.text_input("Bill Name", placeholder="e.g., Electricity, Internet")
    col1, col2 = st.columns(2)
    with col1:
        bill_amount = st.number_input("Bill Amount (PKR)", min_value=100, step=100)
    with col2:
        bill_due_date = st.number_input("Due Date (Day of Month)", min_value=1, max_value=31, value=15)
    
    if st.form_submit_button("Add Bill", use_container_width=True):
        st.success(f"✅ Bill '{bill_name}' added successfully!")

st.divider()
st.markdown("### Bill Payment History")
st.info("Recent bill payments will appear here.")
