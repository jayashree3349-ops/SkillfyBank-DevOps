import os
from flask import Flask, jsonify, request

app = Flask(__name__)
APP_VERSION = os.getenv("APP_VERSION", "v1")

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "service": "SkillfyBank Notification Service",
        "version": APP_VERSION,
        "status": "running"
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy", "version": APP_VERSION}), 200

@app.route("/notify", methods=["POST"])
def notify():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "Test notification")
    return jsonify({
        "service": "SkillfyBank Notification Service",
        "version": APP_VERSION,
        "message": message,
        "status": "accepted"
    }), 202

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
