"""
Dependency functions for authentication and authorization using FastAPI.
"""

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session, select

from app.auth import decode_token
from app.models import RoleEnum, User
from app.database import get_session

# OAuth2 scheme for getting token from Authorization header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_session)
) -> User:
    """
    Validate the JWT token and return the current authenticated user.
    Raises HTTP 401 if the token is invalid or user does not exist.
    """
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=401, detail="Token missing subject")

    user = session.exec(select(User).where(User.id == int(user_id))).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


def require_admin(user: User = Depends(get_current_user)):
    """
    Ensure the current user has an admin role.
    Raises HTTP 403 if not an admin.
    """
    if user.role != RoleEnum.admin:
        raise HTTPException(status_code=403, detail="Admin access required")
    return user
