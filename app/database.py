"""
Database configuration and session management for the application.
"""

import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine, Session

# Load environment variables from .env file
load_dotenv()

# Get the database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    """
    Initialize the database by creating all tables defined in SQLModel metadata.
    """
    SQLModel.metadata.create_all(engine)


def get_session():
    """
    Provide a session for interacting with the database.
    Yields a SQLModel Session object.
    """
    with Session(engine) as session:
        yield session
