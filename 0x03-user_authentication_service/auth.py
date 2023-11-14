#!/usr/bin/env python3
"""Function to hash password"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash password using bcrypt
        return: bytes
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
