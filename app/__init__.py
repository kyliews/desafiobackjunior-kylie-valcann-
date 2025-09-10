from flask import Flask
from app.controllers import users_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(users_blueprint)
    return app