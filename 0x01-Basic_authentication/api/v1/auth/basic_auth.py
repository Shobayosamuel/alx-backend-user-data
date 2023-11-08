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
            header_list = decoded_base64_authorization_header.split(":")
            email = header_list[0]
            pwd = ":".header_list[1:]
            return (email, pwd)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Return: user with the valid password"""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        """users = User.search({"email": user_email})
        if users == [] or users is None:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
            else:
                return None"""
        try:
            users = User.search({"email": user_email})
            if not users or users == []:
                return None
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
            return None
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Return User credentials"""
        header = self.authorization_header(request)
        if header is not None:
            token = self.extract_base64_authorization_header(header)
            if token is not None:
                decode = self.decode_base64_authorization_header(token)
                if decode is not None:
                    email, pwd = self.extract_user_credentials(decode)
                    if email is not None:
                        return self.user_object_from_credentials(
                            email, pwd)
        return
