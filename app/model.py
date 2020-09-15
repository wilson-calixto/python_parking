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


class Car(db.Model):
    """
    Car Model Class.
    """

    __tablename__ = 'car'

    car_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vehicle_license_plate = db.Column(db.String)

    def __init__(self, vehicle_license_plate):
        self.vehicle_license_plate = vehicle_license_plate

    def __repr__(self):
        return f'<Car {self.vehicle_license_plate}>'



class Period(db.Model):
    """
    Period Model Class.
    """

    __tablename__ = 'period'

    period_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    initial_day = db.Column(db.String)
    final_day = db.Column(db.String)
    
    initial_hour = db.Column(db.String)
    final_hour = db.Column(db.String)
    value_per_hour = db.Column(db.String)

    

    def __init__(self, initial_day,final_day,initial_hour,final_hour,value_per_hour):
        self.initial_day = initial_day
        self.final_day = final_day
        self.initial_hour = initial_hour
        self.final_hour = final_hour
        self.value_per_hour = value_per_hour

    def __repr__(self):
        return f'<Period {self.initial_day}>'


