from flask import Blueprint, request, jsonify
from FirebaseApi.config import db, disables_user, enables_user, get_all_users


user_bp = Blueprint("user", __name__, url_prefix="/api/user")

@user_bp.route("/test")
def test_route():
    return jsonify(message = "this is user api")


@user_bp.route("/disable", methods=["POST"])
def disable_user():
    data = request.get_json()
    print(data)
    uid = data.get("uid")
    disabled = data.get("disabled")

    if not uid:
        return jsonify(success=False, error="Missing UID"), 400

    success = disables_user(uid) if disabled else enables_user(uid)
    if success:
        return jsonify(success=True, message=("User disabled" if disabled else "User re-enabled")), 200
    else:
        return jsonify(success=False, error="Failed to update user"), 500

@user_bp.route("/get-all", methods=["GET"])
def get_users():
    return get_all_users()