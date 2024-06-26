from flask import Blueprint,jsonify
from webargs.flaskparser import use_args
from project.app.schemas.StockSchema import PostStockSchema, StockSchema, UpdateStockSchema
from sqlalchemy.exc import IntegrityError
from project.app.bl.StockBLC import StockBLC
from http import HTTPStatus
from marshmallow import fields


bp = Blueprint('stock', __name__)


@bp.route('/api/stock', methods=['POST'])
@use_args(PostStockSchema(), location='json')
def add_stock(args):
    """
    Add a new stock to the database.

    Args:
        args (dict): Validated data from the request conforming to `PostStockSchema`.

    Returns:
        JSON response indicating the result of the operation. If successful,
        returns the added stock data.

    Raises:
        IntegrityError: For database integrity issues.
        Exception: For any other errors.
    """
    try:
        result = StockBLC.add_stock(args)
        stock_schema = StockSchema()
        result = stock_schema.dump(result)
        return jsonify({"message":"Stock added succefully","result":result}),200
    except IntegrityError as e:
        return jsonify({"Error":e.orig.args[1]}), 422
    except Exception as e:
        return jsonify(str(e)),422
    
    
@bp.route('/api/stock', methods=['GET'])
@use_args({'id':fields.Integer()}, location='query')
def get_stock(args):
    """
    Get all Stocks or a single stock by ID.
    Args:
        args (dict): A dictionary containing request arguments.
    Returns:
        Response: A JSON response containing the list of stocks or a single stock.
    """
    try:
        result = StockBLC.get_stock(args)
        stock_schema = StockSchema(many=True)
        result = stock_schema.dump(result)
        return result, 200
    except Exception as e:
        return jsonify(str(e)),422
    
@bp.route('/api/stock', methods=['PUT'])
@use_args(UpdateStockSchema(), location='json')
def update_stock(args):
    """
    Update a Stock data
    """
    try:
        result = StockBLC.update_stock(args)
        stock_schema = UpdateStockSchema()
        result = stock_schema.dump(result)
        return jsonify({'message':'Stock updated successfully', 'result':result}),200
    except Exception as e:
        return jsonify({'error':str(e)}),422
    
@bp.route('/api/stock', methods=['DELETE'])
@use_args({'id': fields.Integer(required=True)}, location='query')
def delete_stock(args):
    """Delete a Stock"""
    
    try:
        stock_id = args.get('id')
        result = StockBLC.delete_stock_by_id(stock_id)
        return jsonify({"message": f"Stock id: {stock_id} deleted successfully"}), HTTPStatus.OK
    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.UNPROCESSABLE_ENTITY

