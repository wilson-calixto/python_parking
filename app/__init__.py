from flask import Flask
from flask_migrate import Migrate
from .model import configure_database
from .serializer import configure_marshmallow


def create_app():
    """
    app factory function.
    """

    app = Flask(__name__)
    app.config.from_object('config')

    configure_database(app)
    configure_marshmallow(app)

    Migrate(app, app.db)

    from .products import bp_products
    app.register_blueprint(bp_products)

    return app
