#!/usr/bin/env python3
"""Class to manage the api authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """manage the api authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if auth is required"""
        return False

    def authorization_header(self, request=None) -> str:
        """Authorization header"""
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """checks the current user"""
        return request
