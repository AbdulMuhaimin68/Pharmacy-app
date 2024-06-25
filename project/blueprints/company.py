from flask import Blueprint,jsonify
from webargs.flaskparser import use_args
from project.app.schemas.CompanySchema import CompanySchema,GetCompanySchema
from project.app.exceptions import NotFoundException
from flask_jwt_extended import get_jwt, jwt_required, get_jwt_identity, current_user
from project.app.decorators import admin_required
from http import HTTPStatus
from project.app.bl.CompanyBLC import CompanyBLC
from marshmallow import fields
from sqlalchemy.exc import IntegrityError


bp = Blueprint('company',__name__)



@bp.route('/api/company', methods=['POST'])
@use_args(CompanySchema(), location='json')
def add_company(args):
    """Adding a company to a Database"""
    try:
        result = CompanyBLC.add_company(args)
        company_schema = CompanySchema()
        result = company_schema.dump(result)
        return jsonify({"message":"Company added succefully","result":result}),201
    except IntegrityError as e:
        return jsonify({"Error":e.orig.args[1]}), 422
    except Exception as e:
        return jsonify(str(e)),422


@bp.route('/api/company', methods=['GET'])
@use_args({'id':fields.Integer()},location='query')
@jwt_required()
@admin_required
def get_company(args):
    """Getting a company"""
    try:
        result = CompanyBLC.get_company(args)
        company_schema = GetCompanySchema(many=True)
        result = company_schema.dump(result)
        return result,200
    except Exception as e:
        return jsonify({'error':str(e)}),422
    
@bp.route('/api/company', methods=['PUT'])
@use_args(CompanySchema(), location='json')
def update_company(args):
    """Updating a company"""
    
    try:
        result = CompanyBLC.update_company(args)
        company_schema = CompanySchema()
        result = company_schema.dump(result)
        return jsonify({"message":"Company Updated Successfully", "result":result})
    except Exception as e:
        return jsonify({'error':str(e)}),422
    
@bp.route('/api/company', methods=['DELETE'])
@use_args({'id': fields.Integer(required=True)}, location='query')
def delete_company(args):
    """Delete a Company"""
    try:
        company_id = args.get('id')
        result = CompanyBLC.delete_company_by_id(company_id)
        return jsonify({"message": f"Company id: {company_id} deleted successfully"}), HTTPStatus.OK
    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.UNPROCESSABLE_ENTITY
    