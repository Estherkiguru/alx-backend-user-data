#!/usr/bin/env python3
""" Encrypting pswds with bcrypt """
import bcrypt


def hash_password(password: str) -> bytes:
    """ Hashes a password using bcrypt"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Checks if hashed and unhashed pswds are same
    Returns bool
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
