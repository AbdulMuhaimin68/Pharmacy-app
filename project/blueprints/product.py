from flask import Blueprint, jsonify
from project.app.bl.productblc import ProductBLC
from http import HTTPStatus
from project.app.db import db
from project.app.schemas.product import ProductSchema
from webargs.flaskparser import use_args
from marshmallow import fields

bp = Blueprint("product", __name__)


@bp.route('/api/product', methods=['POST'])
@use_args(ProductSchema(), location="json")
def add_product(args):
    """
    Adding a product
    """
    result = ProductBLC.add_product(args)
    return jsonify({"message":result}), HTTPStatus.CREATED

