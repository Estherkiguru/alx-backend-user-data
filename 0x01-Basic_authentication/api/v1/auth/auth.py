#!/usr/bin/env python3
"""Auth class"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Managed the API authentication."""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ returns False - path"""
        return False

    def authorization_header(self, request=None) -> str:
        """Flask object that returns None - request"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Flask request object that returns None - request"""
        return None
