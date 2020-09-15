from .model import Product
from .serializer import ProductSchema
from flask import Blueprint, jsonify, request, current_app

# Blueprint init
bp_products = Blueprint('products', __name__)


@bp_products.route('/products', methods=['GET'])
def get_products():
    """
    Get all products in the database.
    """

    product_schema = ProductSchema(many=True)
    product = Product.query.all()
    return product_schema.jsonify(product), 200


@bp_products.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Get a specific product in the database.
    """

    product_schema = ProductSchema()
    products = Product.query.filter(Product.product_id == product_id).first()
    return product_schema.jsonify(products), 200


@bp_products.route('/products', methods=['POST'])
def add_product():
    """
    Add product in database.
    """

    product_schema = ProductSchema()
    product, error = product_schema.load(request.json)

    if not error:
        current_app.db.session.add(product)
        current_app.db.session.commit()
        return product_schema.jsonify(product), 201
    else:
        return jsonify(error), 401


@bp_products.route('/products/<int:product_id>', methods=['PUT'])
def modify_product(product_id):
    """
    Modify data from selected product in the database.
    """

    product_schema = ProductSchema()
    product = Product.query.filter(Product.product_id == product_id)
    product.update(request.json)

    current_app.db.session.commit()
    return product_schema.jsonify(product.first()), 201


@bp_products.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    Delete a selected product in the database.
    """

    product_schema = ProductSchema()
    product = Product.query.filter(Product.product_id == product_id)
    product.delete()
    current_app.db.session.commit()

    return jsonify('Product Deleted'), 200
