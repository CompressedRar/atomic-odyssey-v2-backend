from flask import Blueprint, jsonify, request
from auth.Authentication import Auth
auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route("/test")
def test_route():
    count = Auth.getUserCount()
    return jsonify(message = count)

@auth_bp.route("/upload/profile", methods = ["POST"])
def upload_profile_pic():
    profile_pic = request.files["file"]
    res = Auth.upload_profile_pic(profile_pic)

    return jsonify({
        "link": res
    })



@auth_bp.route("/test-user-create", methods = ["POST"])
def test_user_creation():
    username = request.form.get("username")
    uuid = request.form.get("uuid")
    profile_pic = request.files["file"]
    
    print(profile_pic)
    res = Auth.create_account(uuid, username, profile_pic)
    
    return res
