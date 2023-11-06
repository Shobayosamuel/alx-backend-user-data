#!/usr/bin/env python3
"""Class to manage the api authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """manage the api authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if auth is required"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path in excluded_paths or (path + '/') in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Authorization header"""
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """checks the current user"""
        return request
