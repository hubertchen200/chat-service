from flask import request, jsonify
from api.chat import get_message, send_message, delete_message
from . import message_bp
from hubertchen_package import my_jwt


@message_bp.route('/message', methods = ['GET', 'POST', 'DELETE'])
def my_message():
    data, code = my_jwt.check_token(request.headers)
    sender = data['data']['username']
    if code == 401:
        return jsonify(data), code
    if request.method == 'GET':
        receiver = request.args.get('receiver')
        count = request.args.get('count', 1000)
        return get_message(sender, receiver, count)
    if request.method == "POST":
        message = request.get_json()
        return send_message(sender, message['receiver'], message['content'], '', message['is_group'])
    if request.method == "DELETE":
        id = request.args.get("id", default=None, type=int)
        return delete_message(id)