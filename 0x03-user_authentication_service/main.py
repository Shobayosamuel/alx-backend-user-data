#!/usr/bin/env python3
"""
Main file
"""
import requests


BASE_URL = "http://localhost:5000"


def register_user(email: str, password: str) -> None:
    """Test the register user endpoint"""
    end_point = '/register'
    data = {"email": email, "password": password}
    response = requests.post(BASE_URL + end_point, json=data)
    assert response.status_code == 201


def log_in_wrong_password(email: str, password: str) -> None:
    """Test the login with the wrong password user endpoint"""
    endpoint = '/login'
    data = {"email": email, "password": password}
    response = requests.post(BASE_URL + end_point, json=data)
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """Test the login user with correct password endpoint"""
    endpoint = '/login'
    data = {"email": email, "password": password}
    response = requests.post(BASE_URL + end_point, json=data)
    assert response.status_code == 201
    return response.json()["session_id"]


def profile_unlogged() -> None:
    """Test the profile of the user endpoint before login"""
    endpoint = '/profile'
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 401


def profile_logged(session_id: str) -> None:
    """Test for the profile after login"""
    endpoint = '/profile'
    headers = {"Authorization": "Bearer {}".format(session_id)}
    response = requests.get(BASE_URL + endpoint, headers=headers)
    assert response.status_code == 200


def log_out(session_id: str) -> None:
    """Test logout a user"""
    endpoint = '/log_out'
    headers = {"Authorization": "Bearer {}".format(session_id)}
    response = requests.get(BASE_URL + endpoint, headers=headers)
    assert response.status_code == 200


def reset_password_token(email: str) -> str:
    """Test reset password token endpoint"""
    endpoint = '/reset_password'
    data = {"email": email}
    response = requests.post(BASE_URL + endpoint, json=data)
    assert response.status_code == 200
    return response.json()["reset_token"]


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Test update password of user"""
    endpoint = '/reset_password'
    data = {"email": email, "reset_token": reset_token,
            "new_password": new_password}
    response = requests.post(BASE_URL + endpoint, json=data)
    assert response.status_code == 200


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
