#!/usr/bin/env python3
"""Simple Flask app"""

from flask import Flask, request, jsonify, abort, make_response
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def home() -> str:
    """basic Flask app"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def register_user() -> str:
    """Endpoint to register a user"""
    email, password = request.form.get("email"), request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"email": email, "message": "email already registered"})


@app.route("/session", methods=["POST"], strict_slashes=False)
def valid_login () -> str:
    """Endpoint implementation for user validation"""
    email, password = request.form.get("email"), request.form.get("password")

    if not AUTH.valid_login(email, password):
        abort(401)
    sess_id = AUTH.create_session(email)

    response =({"email": email, "message":"Successfully logged in"})
    response.set_cookie("sess_id", sess_id)
    return response
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
