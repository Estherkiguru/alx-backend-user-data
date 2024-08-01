#!/usr/bin/env python3
"""Module for filter PII from logs"""
import re


def filter_datum(fields, redaction, message, separator: str) -> str:
    """Obfuscates specifed fields in a log message"""
    for f in fields:
        message = re.sub(rf"{f}=(.*?)\{separator}",
                         f'{f}={redaction}{separator}', message)
    return message
