#!/usr/bin/env python3
"""Auth class"""

from flask import request
from typing import List, TypeVar
from os import getenv
import re


class Auth:
    """Managed the API authentication."""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ returns False - path"""
        if path is None or excluded_paths is None:
            return True

        normalized_path = path.rstrip('/') + '/'

        for exclusion_path in map(lambda x: x.strip(), excluded_paths):
            normalized_exclusion = exclusion_path.rstrip('/') + '/'

            pattern = (f'^ {re.escape(normalized_exclusion[:-2])}.*')
            if exclusion_path.endswith('*'):
                if re.match(pattern, normalized_path):
                    return False
            else:
                if normalized_path == normalized_exclusion:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """Flask object that returns None - request"""
        if request is None:
            return None
        auth_header = request.headers.get("Authorization")
        return auth_header

    def current_user(self, request=None) -> TypeVar('User'):
        """Flask request object that returns None - request"""
        return None

    def session_cookie(self, request=None):
        """Retrieves cookie value from a request"""
        if request is None:
            return None
        return request.cookies.get(getenv('SESSION_NAME'))
