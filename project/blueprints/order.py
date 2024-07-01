from flask import Blueprint,jsonify
from webargs.flaskparser import use_args
from http import HTTPStatus
from marshmallow import fields
from project.app.schemas.OrderSchema import OrderReceiptSchema, OrderSchema,GetOrderSchema
from project.app.bl.OrderBLC import OrderBLC

bp = Blueprint('order', __name__)

@bp.route('/api/order', methods=['POST'])
@use_args(OrderSchema(), location='json')
def add_order(args: dict):
    """
    Endpoint to add a new Order to the database.
    """
    try:
        result = OrderBLC.add_order(args)
        order_receipt_schema = OrderReceiptSchema()
        serialized_result = order_receipt_schema.dump(result)
        return jsonify(serialized_result), HTTPStatus.CREATED

    except Exception as e:
        return jsonify(str(e)), 422
    

@bp.route('/api/order', methods=['GET'])
@use_args({'id':fields.Integer()}, location='query')
def get_order(args):
    """Getting Order"""
    
    try:
        result = OrderBLC.get_order(args)
        order_schema = GetOrderSchema(many=True)
        result = order_schema.dump(result)
        return result
    except Exception as e:
        return jsonify(str(e)),422
    
@bp.route('/api/order', methods=['PUT'])
@use_args(OrderSchema(),location='json')
def update_order(args):
    """Update an Order"""
    
    try:
        result = OrderBLC.update_order(args)
        order_schema = OrderSchema()
        result = order_schema.dump(result)
        return jsonify({"message":"Order Updated succesfully", "result":result})
    except Exception as e:
        return jsonify({"error":str(e)}),422
    
@bp.route('/api/order', methods=['DELETE'])
@use_args({"id":fields.Integer(required=True)}, location='query')
def delete_order(args: dict):
    """Delete an Order"""
    try:
        res = OrderBLC.delete_order(args)
        return (jsonify({"message": f"Order {args['id']} is deleted successfully"}),HTTPStatus.OK)
    except Exception as e:
        return jsonify({"message": str(e)}), HTTPStatus.UNPROCESSABLE_ENTITY