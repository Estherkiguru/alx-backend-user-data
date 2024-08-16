#!/usr/bin/env python3
"""Simple Flask app"""

from flask import Flask, request, jsonify, abort, make_response
from auth import Auth

app = Flask(__name__)
#auth = Auth()

@app.route("/"), methods=["GET"]
def home():
    """basic Flask app"""
    return jsonify({"message": "Bienvenue"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")