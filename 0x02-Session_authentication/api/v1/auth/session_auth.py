#!/usr/bin/env python3
"""Session authentication module for an API"""

from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """session Authentication"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates Session ID for user_id"""
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Retrieves user ID based on session ID"""
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Retrieves User instance based on cookie value"""
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)

        return User.get(user_id)

    def destroy_session(self, request=None):
        """Deletes user session/logout"""
        if request is None:
            return False
        cookie = self.session_cookie(request)
        if cookie is None or self.user_id_for_session_id(cookie) is None:
            return False
        del self.user_id_by_session_id[cookie]
        return True
