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

    def create_session(self, email: str) -> str:
        """Create a user session id and return it"""
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            return None
        else:
            user.session_id = _generate_uuid()
            return user.session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """find user by session ID"""
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        else:
            return user

    def destroy_session(self, user_id: int) -> None:
        """Destroy session"""
        try:
            user = self._db.find_user_by(id=user_id)
        except Exception:
            return None
        else:
            user.session_id = None
            return None

    def get_reset_password_token(self, email: str) -> str:
        """Return: generated reset token"""
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            raise ValueError
        else:
            reset_token = _generate_uuid()
            user.reset_token = reset_token
            return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """Update the user password"""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            user.hashed_password = _hash_password(password)
            user.reset_token = None
        except Exception:
            raise ValueError


def _hash_password(password: str) -> bytes:
    """Hash password using bcrypt
        return: bytes
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Return string representation of uuid"""
    return str(uuid.uuid4())
