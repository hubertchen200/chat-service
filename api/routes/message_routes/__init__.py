from flask import Blueprint

message_bp = Blueprint('message_bp', __name__)

from . import routes