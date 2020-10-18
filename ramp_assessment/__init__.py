__version__ = '0.1.0'

from flask import Flask

def create_app():
    app = Flask(__name__)

    from .transform import views
    app.register_blueprint(views.transform)
    app.add_url_rule('/', endpoint="index") # Might not need this

    return app