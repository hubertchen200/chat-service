from . import friend_bp
from flask import request
from api.friend import get_request, send_request, accept, decline


@friend_bp.route('/friend/request', methods = ["GET", "POST"])
def my_friend():
    if request.method == "GET":
        id = request.args.get("user_id")
        return get_request(id)
    if request.method == "POST":
        my_request = request.get_json()
        return send_request(my_request["user_id"], my_request["friend_id"])



@friend_bp.route("/friend/accept", methods = ["POST"])
def friend_accept():
    if request.method == "POST":
        return accept(request.args.get("id"))


@friend_bp.route("/friend/decline", methods = ["POST"])
def friend_decline():
    if request.method == "POST":
        return decline(request.args.get("id"))





