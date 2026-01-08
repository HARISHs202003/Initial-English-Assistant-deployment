from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from bot import process_message   # <-- UPDATED IMPORT

app = Flask(
    __name__,
    static_folder="frontend",
    static_url_path=""
)

CORS(app)

# -------- Swagger Config --------
SWAGGER_URL = "/docs"
API_URL = "/static/swagger.json"

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        "app_name": "English Assistant API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
# --------------------------------


# Serve frontend
@app.route("/", methods=["GET"])
def frontend():
    return send_from_directory("frontend", "index.html")


# Health check
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


# 🔥 MODE-BASED CHAT ENDPOINT
@app.route("/chat", methods=["POST"])
def chat():
    # 🔐 API Key security
    if request.headers.get("X-API-KEY") != os.getenv("APP_API_KEY"):
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()

    # ✅ Validate payload
    if not data or "mode" not in data or "messages" not in data:
        return jsonify({"error": "Invalid request"}), 400

    mode = data["mode"]
    messages = data["messages"]

    if not isinstance(messages, list) or len(messages) == 0:
        return jsonify({"error": "Messages must be a non-empty list"}), 400

    try:
        if mode == "grammar":
            user_text = messages[-1]["content"]
            reply = correct_english(user_text)

        elif mode == "chat":
            reply = process_messages(messages)

        else:
            return jsonify({"error": "Invalid mode"}), 400

        return jsonify({"reply": reply})

    except Exception as e:
        print("CHAT ERROR:", e)
        return jsonify({"error": "AI service failed"}), 500


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

