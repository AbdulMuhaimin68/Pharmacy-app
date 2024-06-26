from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from project.app.bl.ProductBLC import ProductBLC
from http import HTTPStatus
from project.app.db import db
from project.app.decorators import admin_required
from project.app.schemas.ProductSchema import ProductSchema,GetProductSchema,ProductSearchSchema
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
    
@bp.route('/api/product', methods=['GET'])
@jwt_required()
@admin_required
@use_args(ProductSearchSchema(), location='json')
def get_products(args):
    """
    Get all products or a single product by ID.
    Args:
        args (dict): A dictionary containing request arguments.
    Returns:
        Response: A JSON response containing the list of products or a single product.
    """
    try:
        result = ProductBLC.get_products(args)
        product_schema = GetProductSchema(many=True)
        result = product_schema.dump(result)
        return result,200
    except ValueError as e:
        return jsonify(error=str(e)), 400
    except KeyError as e:
        return jsonify(error=str(e)), 404
    except Exception as e:
        import traceback
        print(traceback.print_exc())
        return jsonify(error=str(e)), 500
    


