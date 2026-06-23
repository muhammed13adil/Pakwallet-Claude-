"""
config.py
---------
Global configuration for PakWallet application.
"""

# App branding
APP_NAME = "PakWallet"
APP_TAGLINE = "Smart Money Management for Pakistan"
APP_ICON = "💳"

# Feature flags
ENABLE_OTP = False  # OTP feature (ready but disabled for MVP)
ENABLE_REAL_TRANSACTIONS = False  # All transactions are simulated for MVP

# Demo data
DEMO_BALANCE = 50000  # PKR
DEMO_CURRENCY = "PKR"

# Security
PASSWORD_MIN_LENGTH = 6
PIN_LENGTH = 4

# Session timeouts (in minutes)
SESSION_TIMEOUT = 30
