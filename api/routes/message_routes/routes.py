from flask import request, jsonify
from api.chat import get_message, send_message, delete_message
from . import message_bp
from api.jwt_token.my_jwt import jwt_decode


@message_bp.route('/message', methods = ['GET', 'POST', 'DELETE'])
def my_message():
    token = request.headers.get('Authorization')
    payload = jwt_decode(token)
    if payload == "TOKEN_EXPIRED":
        return jsonify({'error': "TOKEN_EXPIRED"})
    if payload == "INVALID_TOKEN":
        return jsonify({'error': 'INVALID_TOKEN'})
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