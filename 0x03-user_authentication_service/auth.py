#!/usr/bin/env python3
"""Function to hash password"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Initialize the new auth"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user if the email does not exist"""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

        else:
            raise ValueError('User {} already exists'.format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """Check if password is valid"""
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            return False
        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)


def _hash_password(password: str) -> bytes:
    """Hash password using bcrypt
        return: bytes
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def _generate_uuid(self) -> str:
    """Return string representation of uuid"""
    return str(uuid.uuid4())
