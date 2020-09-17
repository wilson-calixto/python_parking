from flask import Flask
from flask_migrate import Migrate, upgrade
from sqlalchemy import event
from .models.model import configure_database
from .models.serializer import configure_marshmallow
from .routes.order import bp_order
from .routes.order_report import bp_order_report

from .models.model import Period


def create_app(custom_config=None):
    """
    app factory function.
    """

    app = Flask(__name__)
    if(custom_config is None):
        app.config.from_object('config')
    else:
        app.config.from_object(custom_config)

    configure_database(app)
    configure_marshmallow(app)

    Migrate(app, app.db)
    # upgrade(app.app_context(), app.db)



    app.register_blueprint(bp_order)
    app.register_blueprint(bp_order_report)
    
    return app

