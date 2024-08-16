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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
