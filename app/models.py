"""
SQLModel-based ORM models for users and projects.
"""

from sqlmodel import SQLModel, Field
from typing import Optional
from enum import Enum


class RoleEnum(str, Enum):
    """
    Enum for user roles.
    """
    admin = "admin"
    user = "user"


class User(SQLModel, table=True):
    """
    Database model for application users.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    hashed_password: str
    role: RoleEnum = RoleEnum.user


class Project(SQLModel, table=True):
    """
    Database model for projects.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
