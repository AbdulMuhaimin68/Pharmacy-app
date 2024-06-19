from flask import Blueprint, jsonify
from project.app.bl.ProductBLC import ProductBLC
from http import HTTPStatus
from project.app.db import db
from project.app.schemas.ProductSchema import ProductSchema
from webargs.flaskparser import use_args
from marshmallow import fields
from sqlalchemy.exc import IntegrityError

bp = Blueprint("product", __name__)


@bp.route('/api/product', methods=['POST'])
@use_args(ProductSchema(), location="json")
def add_product(args):
    """
    Adding a product
    """
    try:
        result = ProductBLC.add_product(args)
        return jsonify({"message":result}), HTTPStatus.CREATED
    except IntegrityError as ie:
        return {"message": "Foreign key constraint failed", 'error': str(ie)}, 422
    except Exception as e:
        return jsonify(str(e)), 422

