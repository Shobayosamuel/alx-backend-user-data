#!/usr/bin/env python3
"""Function to hash password"""
import bcrypt


def _hash_password(password) -> bytes:
    """Hash password using bcrypt
        return: bytes
    """
    pass_byt = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pass_byt, salt)
    return hashed
