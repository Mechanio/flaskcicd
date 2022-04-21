from flask import Flask
from config import Config


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = Config.SECRET_KEY
    app.static_folder = 'templates/static'
    from .views import main_routes_bp
    app.register_blueprint(main_routes_bp)
    return app
