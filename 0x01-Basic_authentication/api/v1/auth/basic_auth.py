#!/usr/bin/env python3
"""
Basic Auth module
"""
from api.v1.auth.auth import Auth
import binascii
import base64


class BasicAuth(Auth):
    """Basic Auth class"""
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extracts the Base64 part of the Authorization header"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic"):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decodes Base64 authorization header"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded = base64.b64decode(base64_authorization_header)
            decoded_str = decoded.decode('utf-8')
            return decoded_str
        except Exception as e:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header:
            str) -> (str, str):
        """Handles user email and password"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None

        try:
            email, password = decoded_base64_authorization_header.split(':', 1)
            return email, password
        except Exception as e:
            return None, None
