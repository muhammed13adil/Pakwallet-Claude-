"""
utils/styles.py
---------------
CSS styling and UI components for PakWallet.
"""

import streamlit as st


def inject_custom_css() -> None:
    """Inject custom CSS for PakWallet branding and styling."""
    custom_css = """
    <style>
    /* PakWallet Color Scheme */
    :root {
        --primary-color: #2E7D32;  /* Green (Pakistani theme) */
        --secondary-color: #1565C0; /* Blue */
        --accent-color: #F57C00;   /* Orange */
        --text-dark: #212121;
        --text-light: #757575;
        --bg-light: #F5F5F5;
        --border-color: #E0E0E0;
    }
    
    /* Hero Section */
    .pw-hero {
        background: linear-gradient(135deg, #2E7D32 0%, #1565C0 100%);
        color: white;
        padding: 40px 20px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .pw-hero h1 {
        font-size: 2.5em;
        margin: 0;
        font-weight: 700;
    }
    
    .pw-hero p {
        font-size: 1.1em;
        margin: 10px 0 0 0;
        opacity: 0.95;
    }
    
    /* Card Styling */
    .pw-card {
        background: white;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        padding: 20px;
        margin: 10px 0;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
    }
    
    .pw-card:hover {
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        border-color: var(--primary-color);
    }
    
    /* Button Styling */
    .pw-button {
        background: var(--primary-color);
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 6px;
        cursor: pointer;
        font-weight: 600;
        transition: background 0.3s ease;
    }
    
    .pw-button:hover {
        background: #245D27;
    }
    
    /* Form Styling */
    .pw-form-section {
        background: var(--bg-light);
        padding: 20px;
        border-radius: 8px;
        margin: 15px 0;
    }
    
    /* Alert Styling */
    .pw-alert-success {
        background: #C8E6C9;
        color: #1B5E20;
        padding: 15px;
        border-radius: 6px;
        border-left: 4px solid #4CAF50;
    }
    
    .pw-alert-error {
        background: #FFCDD2;
        color: #B71C1C;
        padding: 15px;
        border-radius: 6px;
        border-left: 4px solid #F44336;
    }
    
    /* Table Styling */
    .pw-table {
        width: 100%;
        border-collapse: collapse;
        margin: 15px 0;
    }
    
    .pw-table th {
        background: var(--primary-color);
        color: white;
        padding: 12px;
        text-align: left;
        font-weight: 600;
    }
    
    .pw-table td {
        padding: 12px;
        border-bottom: 1px solid var(--border-color);
    }
    
    .pw-table tr:hover {
        background: var(--bg-light);
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .pw-hero h1 {
            font-size: 1.8em;
        }
        
        .pw-hero p {
            font-size: 0.95em;
        }
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)


def render_hero(title: str, subtitle: str = "") -> None:
    """
    Render a branded hero section.
    
    Args:
        title: Hero title/heading
        subtitle: Optional subtitle text
    """
    st.markdown(f'<div class="pw-hero">', unsafe_allow_html=True)
    st.markdown(f"## {title}")
    if subtitle:
        st.markdown(f"*{subtitle}*")
    st.markdown("</div>", unsafe_allow_html=True)


def render_stat_card(label: str, value: str, icon: str = "", color: str = "green") -> None:
    """
    Render a statistic card.
    
    Args:
        label: Stat label
        value: Stat value
        icon: Optional emoji/icon
        color: Card color theme
    """
    st.markdown(f'<div class="pw-card">', unsafe_allow_html=True)
    st.markdown(f"**{icon} {label}**" if icon else f"**{label}**")
    st.markdown(f"## {value}")
    st.markdown("</div>", unsafe_allow_html=True)
