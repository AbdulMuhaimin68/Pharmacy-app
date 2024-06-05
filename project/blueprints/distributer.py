from flask import Blueprint,jsonify
from webargs.flaskparser import use_args
from project.app.schemas.DistributerSchema import DistributerSchema,UpdateDistributerSchema
from project.app.bl.DistributerBLC import DistributerBLC
from project.app.exceptions import DuplicateError
from marshmallow import fields
from http import HTTPStatus


bp = Blueprint('distributer', __name__)



@bp.route('/api/distributer', methods=['POST'])
@use_args(DistributerSchema(), location='json')
def add_distributer(args:dict):
    """
    Add a new distributer to the database
    """
    try:
        result = DistributerBLC.add_distributer(args)
        distributer_schema = DistributerSchema()
        result = distributer_schema.dump(result)
        return jsonify(result),HTTPStatus.CREATED
    except Exception as e:
        return jsonify(str(e)),422
    
@bp.route('/api/distributer', methods=['GET'])
@use_args({'id':fields.Integer()}, location='query')
def get_distributer(args:dict):
    """
    Getting Distributers
    """
    try:
        result = DistributerBLC.get_distributers(args)
        distributer_schema = DistributerSchema(many=True)
        result = distributer_schema.dump(result)
        return result
    except Exception as e:
        return jsonify({"error": str(e)}), 422
        
@bp.route('/api/distributer', methods=['PUT'])
@use_args(UpdateDistributerSchema(), location='json')
def update_distributer(args):
    """
    Update a distributer
    """
    try:
        result =  DistributerBLC.update_distributer(args)
        distributer_schema = DistributerSchema()
        result = distributer_schema.dump(result)
        return jsonify({'messge':f'Distributer {result["id"]}  Updated successfully!','result':result})
    except Exception as e:
        return jsonify({"error": str(e)}), 422
    
    
@bp.route('/api/distributer', methods=['DELETE'])
@use_args({"id":fields.Integer(required=True)}, location='query')
def delete_distributer(args: dict):
    """Delete a Distributer"""
    try:
        res = DistributerBLC.delete_distributer_by_id(args)
        return (jsonify({"message": f"Distributer {args['id']} is deleted successfully"}),HTTPStatus.OK)
    except Exception as e:
        return jsonify({"message": str(e)}), HTTPStatus.UNPROCESSABLE_ENTITY