from . import jwt_bp
from flask import request
from api.jwt_token.my_jwt import jwt_encode, jwt_decode
@jwt_bp.route('/jwt/encode', methods = [ 'POST'])
def my_encode():
    payload = request.get_json()
    return jwt_encode(payload["user_id"], payload["username"])
@jwt_bp.route('/jwt/decode/<token>', methods = ['GET'])
def my_decode(token):
    return jwt_decode(token)

