"""
Pydantic schemas for request/response models.
"""

from pydantic import BaseModel
from typing import Optional
from enum import Enum


class RoleEnum(str, Enum):
    """
    Enum for user roles.
    """
    admin = "admin"
    user = "user"


class UserCreate(BaseModel):
    """
    Schema for user registration.
    """
    username: str
    password: str
    role: RoleEnum


class UserLogin(BaseModel):
    """
    Schema for user login.
    """
    username: str
    password: str


class Token(BaseModel):
    """
    Schema for JWT token response.
    """
    access_token: str
    token_type: str = "bearer"


class ProjectCreate(BaseModel):
    """
    Schema for creating a project.
    """
    name: str
    description: str


class ProjectRead(ProjectCreate):
    """
    Schema for reading project details.
    """
    id: int
