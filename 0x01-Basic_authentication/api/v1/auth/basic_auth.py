#!/usr/bin/env python3
"""
Module for authentication using Basic auth
"""


from typing import TypeVar
from api.v1.auth.auth import Auth
import base64

from models.user import User


class BasicAuth(Auth):
    """Basic Authentication"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Return the Base64 part  the authorization header"""
        if authorization_header is None:
            return None
        elif type(authorization_header) != str:
            return None
        elif authorization_header[0:6] != "Basic ":
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Return the decoded value for the header if it  not None"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decode_val = base64_authorization_header.encode('utf-8')
            decoded = base64.b64decode(decode_val)
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Return: user email and password"""
        if decoded_base64_authorization_header is None:
            return (None, None)
        elif type(decoded_base64_authorization_header) != str:
            return (None, None)
        elif ':' not in decoded_base64_authorization_header:
            return (None, None)
        else:
            first, sec = decoded_base64_authorization_header.split(":")
            return (first, sec)
