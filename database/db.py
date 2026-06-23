"""
database/db.py
--------------
Database models and session management for PakWallet.
"""

from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./pakwallet.db")

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class User(Base):
    """User account model."""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, nullable=True)
    password_hash = Column(String)
    pin_hash = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Transaction(Base):
    """Transaction model for wallet operations."""
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    type = Column(String)  # income, expense, transfer, bill_payment
    category = Column(String)
    amount = Column(Float)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


class Bill(Base):
    """Recurring bill model."""
    __tablename__ = "bills"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    name = Column(String)  # Electricity, Gas, Internet, etc.
    amount = Column(Float)
    due_date = Column(Integer)  # Day of month
    is_paid = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class SavingsGoal(Base):
    """Savings goal model."""
    __tablename__ = "savings_goals"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    name = Column(String)
    target_amount = Column(Float)
    current_amount = Column(Float, default=0)
    category = Column(String)  # emergency, hajj, education, home, etc.
    created_at = Column(DateTime, default=datetime.utcnow)


def init_db():
    """Initialize the database and create all tables."""
    Base.metadata.create_all(bind=engine)


def get_session() -> Session:
    """Get a database session."""
    return SessionLocal()
