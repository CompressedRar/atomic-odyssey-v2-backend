from flask import Blueprint, jsonify

elements_bp = Blueprint("elements", __name__, url_prefix="/api/elements")

@elements_bp.route("/test")
def test_route():
    return jsonify(message = "this is elements api")