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
    data = request.get_json()

    if not data or "text" not in data or "mode" not in data:
        return jsonify({"error": "Missing 'text' or 'mode'"}), 400

    text = data["text"].strip()
    mode = data["mode"]

    if not text:
        return jsonify({"error": "Text cannot be empty"}), 400

    if mode not in ["grammar", "chat"]:
        return jsonify({"error": "Invalid mode"}), 400

    try:
        reply = process_message(text, mode)
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": "AI service failed"}), 500


if __name__ == "__main__":
    app.run(debug=True)
