#!/usr/bin/env python3
"""Authentication module"""

from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes a password and returns bytes"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers new user with given email and password"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"user {email} already exists")
        except NoResultFound:
            pass
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user
