from flask import Blueprint,jsonify
from project.app.schemas.customer import AddCustomerSchema, CustomerSchema,GetCustomerSchema
from project.app.bl.CustomerBLC import CustomerBLC
from marshmallow import fields
from webargs.flaskparser import use_args



bp = Blueprint('customer', __name__)


@bp.route('/api/customer', methods=['POST'])
@use_args(AddCustomerSchema(exclude=("id",)),location='json')
def add_customer(args):
    """Adding a Customer to a Database"""
    try:
        result = CustomerBLC.add_customer(args)
        customer_schema = CustomerSchema()
        result = customer_schema.dump(result)
        return result,201
    except Exception as e:
        return jsonify(str(e)),422
    
    
@bp.route('/api/customer', methods=['GET'])
@use_args({'id':fields.Integer()}, location='query')
def get_cutomer(args):
    """Getting Customers"""
    
    try:
        result = CustomerBLC.get_customer(args)
        customer_schema = CustomerSchema(many=True)
        result = customer_schema.dump(result)
        return result
    except Exception as e:
        return jsonify(str(e)),422
    
@bp.route('/api/customer', methods=['PUT'])
@use_args(GetCustomerSchema(),location='json')
def update_customer(args):
    """Update a Customer"""
    
    try:
        result = CustomerBLC.update_customer(args)
        customer_schema = CustomerSchema()
        result = customer_schema.dump(result)
        return jsonify({"message":"Customer Updated succesfully", "result":result})
    except Exception as e:
        return jsonify({"error":str(e)}),422
    
        
    
    