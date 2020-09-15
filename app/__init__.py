from flask import Flask
from flask_migrate import Migrate
from .model import configure_database
from .serializer import configure_marshmallow

from .products import bp_products
from .vehicles import bp_vehicles
from .period import bp_period
from .order import bp_order


def create_app():
    """
    app factory function.
    """

    app = Flask(__name__)
    app.config.from_object('config')

    configure_database(app)
    configure_marshmallow(app)

    Migrate(app, app.db)


    app.register_blueprint(bp_products)


    app.register_blueprint(bp_vehicles)
    app.register_blueprint(bp_period)
    app.register_blueprint(bp_order)
    
    
    return app
