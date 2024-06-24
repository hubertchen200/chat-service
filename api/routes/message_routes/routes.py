from flask import request
from api.chat import get_message, send_message, delete_message
from . import message_bp


@message_bp.route('/message', methods = ['GET', 'POST', 'DELETE'])
def my_message():
    if request.method == 'GET':
        id = request.args.get('id', default=1, type=int)
        count = request.args.get('count', default=10, type=int)
        return get_message(id, count)
    if request.method == "POST":
        message = request.get_json()
        return send_message(message['sender'], message['receiver'], message['content'], '', message['is_group'])
    if request.method == "DELETE":
        id = request.args.get("id", default = None, type = int)
        return delete_message(id)