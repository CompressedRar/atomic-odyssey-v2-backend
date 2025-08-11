from flask import Blueprint, jsonify

scores_bp = Blueprint("scores", __name__, url_prefix="/api/scores")

@scores_bp.route("/test")
def test_route():
    return jsonify(message = "this score api")