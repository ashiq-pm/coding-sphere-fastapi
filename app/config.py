"""
Loads environment variables for application configuration.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Application secret key for JWT
SECRET_KEY = os.getenv("SECRET_KEY", "fallbacksecret")

# JWT encryption algorithm
ALGORITHM = os.getenv("ALGORITHM", "HS256")

# Token expiry time in minutes
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
