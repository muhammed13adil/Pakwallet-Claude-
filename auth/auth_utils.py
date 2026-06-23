"""
auth/auth_utils.py
------------------
Authentication utilities for PakWallet.
Handles user login, registration, and credential validation.
"""

import hashlib
import re
from sqlalchemy.orm import Session


def hash_password(password: str) -> str:
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


def authenticate_user(session: Session, identifier: str, password: str):
    """
    Authenticate a user by username or email.
    
    Args:
        session: Database session
        identifier: Username or email
        password: Plain text password
        
    Returns:
        User object if authentication successful, None otherwise
    """
    from database.db import User
    
    user = session.query(User).filter(
        (User.username == identifier) | (User.email == identifier.lower())
    ).first()
    
    if user and user.password_hash == hash_password(password):
        return user
    return None


def register_user(session: Session, full_name: str, username: str, email: str, 
                  phone: str, password: str, pin: str) -> None:
    """
    Register a new user account.
    
    Args:
        session: Database session
        full_name: User's full name
        username: Username (must be unique)
        email: Email address (must be unique)
        phone: Phone number (optional)
        password: Plain text password to be hashed
        pin: 4-digit transaction PIN
    """
    from database.db import User
    
    user = User(
        full_name=full_name,
        username=username.strip(),
        email=email.strip().lower(),
        phone=phone.strip() if phone else None,
        password_hash=hash_password(password),
        pin_hash=hash_password(pin)
    )
    session.add(user)
    session.commit()


def validate_registration_inputs(full_name: str, username: str, email: str, 
                                 password: str, confirm_password: str, 
                                 pin: str, confirm_pin: str) -> tuple[bool, str]:
    """
    Validate registration form inputs.
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not all([full_name, username, email, password, pin]):
        return False, "All fields are required."
    
    if len(full_name.strip()) < 2:
        return False, "Full name must be at least 2 characters."
    
    if len(username.strip()) < 3:
        return False, "Username must be at least 3 characters."
    
    if not re.match(r"^[a-zA-Z0-9_-]+$", username):
        return False, "Username can only contain letters, numbers, underscores, and hyphens."
    
    if not re.match(r"^[^@]+@[^@]+\.[^@]+$", email):
        return False, "Please enter a valid email address."
    
    if len(password) < 6:
        return False, "Password must be at least 6 characters."
    
    if password != confirm_password:
        return False, "Passwords do not match."
    
    if not pin.isdigit() or len(pin) != 4:
        return False, "PIN must be exactly 4 digits."
    
    if pin != confirm_pin:
        return False, "PINs do not match."
    
    if pin == password[:4]:
        return False, "PIN should be different from your password."
    
    return True, ""


def username_or_email_exists(session: Session, username: str, email: str) -> str:
    """
    Check if username or email already exists.
    
    Returns:
        Error message if exists, empty string otherwise
    """
    from database.db import User
    
    existing_user = session.query(User).filter(
        (User.username == username) | (User.email == email)
    ).first()
    
    if existing_user:
        if existing_user.username == username:
            return "Username already taken. Please choose another."
        else:
            return "Email already registered. Please use a different email or login."
    
    return ""
