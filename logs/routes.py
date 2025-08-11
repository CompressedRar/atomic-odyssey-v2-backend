from flask import Blueprint, jsonify

logs_bp = Blueprint("logs", __name__, url_prefix="/api/logs")

@logs_bp.route("/test")
def test_route():
    return jsonify(message = "this is logs")