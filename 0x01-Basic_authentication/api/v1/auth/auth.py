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
        elif path in excluded_paths or (path + '/') in excluded_paths:
            return False
        for excluded_path in excluded_paths:
            if excluded_path.startswith(path):
                return False
            elif path.startswith(excluded_path):
                return False
            elif excluded_path[-1] == "*":
                if path.startswith(excluded_path[:-1]):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """Authorization header"""
        if request is None:
            return None
        header = request.headers.get('Authorization')
        if header is None:
            return None
        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """checks the current user"""
        return None
