"""
Authentication utility functions for password hashing, verification,
JWT token creation and decoding.
"""

from datetime import datetime, timedelta

from jose import JWTError, jwt
from passlib.context import CryptContext

from app.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from app.models import User

# Password hashing context using bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    """
    Hashes a plain password using bcrypt.

    :param password: Plain text password
    :return: Hashed password
    """
    return pwd_context.hash(password)


def verify_password(plain, hashed):
    """
    Verifies a plain password against its hashed version.

    :param plain: Plain text password
    :param hashed: Hashed password
    :return: True if matched, False otherwise
    """
    return pwd_context.verify(plain, hashed)


def create_access_token(user: User):
    """
    Generates a JWT token for a user.

    :param user: User instance
    :return: JWT token as a string
    """
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.utcnow() + expires_delta
    to_encode = {
        "sub": str(user.id),
        "role": user.role,
        "exp": expire
    }
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str):
    """
    Decodes and verifies a JWT token.

    :param token: JWT token
    :return: Decoded payload if valid, else None
    """
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError as e:
        print(f"JWTError: {e}")
        return None
