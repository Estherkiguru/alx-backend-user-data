#!/usr/bin/env python3
"""Auth class"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Managed the API authentication."""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ returns False - path"""
        check = path
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if not path.endswith('/'):
            check += '/'
        if check in excluded_paths or path in excluded_paths:
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
