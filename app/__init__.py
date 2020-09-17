from flask import Flask
from flask_migrate import Migrate
from sqlalchemy import event
from .models.model import configure_database
from .models.serializer import configure_marshmallow
from .routes.order import bp_order
from .routes.order_report import bp_order_report

from .models.model import Period


def create_app():
    """
    app factory function.
    """

    app = Flask(__name__)
    app.config.from_object('config')

    configure_database(app)
    configure_marshmallow(app)

    Migrate(app, app.db)




    app.register_blueprint(bp_order)
    app.register_blueprint(bp_order_report)
    
    # TODO adicionar pasta routes
    return app

