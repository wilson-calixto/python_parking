# import sqlalchemy as sa
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref

# engine = sa.create_engine("sqlite:///:memory:")
# session = scoped_session(sessionmaker(bind=engine))
# Base = declarative_base()


# class Author(Base):
#     __tablename__ = "authors"
#     id = sa.Column(sa.Integer, primary_key=True)
#     name = sa.Column(sa.String, nullable=False)

#     def __repr__(self):
#         return "<Author(name={self.name!r})>".format(self=self)


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


class Vehicle(db.Model):
    """
    Vehicle Model Class.
    """

    __tablename__ = 'vehicle'

    vehicle_id = db.Column(db.Integer, primary_key=True)#, autoincrement=True)
    vehicle_license_plate = db.Column(db.String)

    def __init__(self, vehicle_license_plate):
        self.vehicle_license_plate = vehicle_license_plate
        

    def __repr__(self):
        return f'<Vehicle {self.vehicle_license_plate}>'



class Period(db.Model):
    """
    Period Model Class.
    """

    __tablename__ = 'period'

    period_id = db.Column(db.Integer, primary_key=True)
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






class Order(db.Model):
    """
    Order Model Class.
    """

    __tablename__ = 'order'

    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fk_vehicle = db.Column(db.Integer)
    fk_period = db.Column(db.Integer)
    initial_hour = db.Column(db.String)
    final_hour = db.Column(db.String)
    hour_quantity = db.Column(db.String)
    total_value = db.Column(db.String)
    order_date = db.Column(db.String)

    

    def __init__(self, order_id,
        fk_vehicle,
        fk_period,
        initial_hour,
        final_hour,
        hour_quantity,
        total_value,
        order_date):

        self.order_id = order_id,
        self.fk_vehicle = fk_vehicle,
        self.fk_period = fk_period,
        self.initial_hour = initial_hour,
        self.final_hour = final_hour,
        self.hour_quantity = hour_quantity,
        self.total_value = total_value,
        self.order_date = order_date


    def __repr__(self):
        return f'<Order {self.order_id}>'


