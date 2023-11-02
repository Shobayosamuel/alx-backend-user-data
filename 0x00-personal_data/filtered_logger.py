#!/usr/bin/env python3
""" __Regexing__"""


from typing import List
import re
import logging


PII_FIELDS = ("name", "email", "phone", "ssn", "password")

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize the class"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Implement formater to filter log records"""
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Return: log message"""
    for fr in fields:
        message = re.sub(f'{fr}=.*?{separator}',
                         f'{fr}={redaction}{separator}', message)
    return message

def get_logger() -> logging.Logger:
    """Return a logging.logger object of the logger"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler(RedactingFormatter(list(PIL_fields)))
    logger.addHandler(stream_handler)
    return logger
