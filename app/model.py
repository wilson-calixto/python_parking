from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def configure_database(app):
    db.init_app(app)
    app.db = db


class Product(db.Model):
    """
    Product Model Class.
    """

    __tablename__ = 'products'

    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.String)
    quantity = db.Column(db.Integer)

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f'<Product {self.name}>'
