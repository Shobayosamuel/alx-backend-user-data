#!/usr/bin/env python3
""" __Regexing__"""


from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Return: log message"""
    for fr in fields:
        message = re.sub(f'{fr}=.*?{separator}',
                         f'{fr}={redaction}{separator}', message)
    return message
