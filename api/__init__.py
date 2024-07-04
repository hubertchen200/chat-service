from flask import Flask

print('api init')
from api.routes.message_routes import message_bp

def create_app():
    app = Flask(__name__)
    print('create app')
    app.register_blueprint(message_bp)
    return app
