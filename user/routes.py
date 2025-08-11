from flask import Blueprint, jsonify

user_bp = Blueprint("user", __name__, url_prefix="/api/user")

@user_bp.route("/test")
def test_route():
    return jsonify(message = "this is user api")


