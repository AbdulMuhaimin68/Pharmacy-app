from flask import Blueprint, jsonify,request
from project.app.bl.formulablc import FormulaBLC
from http import HTTPStatus
from project.app.schemas.formula import FormulaSchema, UpdateFomulaSchema
from webargs.flaskparser import use_args
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import SQLAlchemyError
from project.app.exceptions import DuplicateError,NotFoundException
from webargs import fields

bp = Blueprint("formula", __name__)


@bp.route('/api/formula', methods=['POST'])
@use_args(FormulaSchema(), location="json")
def add_formula(args: dict):
    """
    Adding a formula
    """
    try:
        result = FormulaBLC.add_formula(args)
        formula_schema = FormulaSchema()
        result = formula_schema.dump(result)
        return jsonify(result), HTTPStatus.CREATED
    except DuplicateError as e:
        return jsonify({"error": str(e)}), 422
    except Exception as e:
        return jsonify({"error": str(e)}), 422
    
@bp.route('/api/formula', methods=['GET'])
@use_args({"id": fields.Integer()}, location="query")
def get_formula(args):
    try:
        
        result = FormulaBLC.get_formulas(args)
        formula_schema = FormulaSchema(many=True)
        result = formula_schema.dump(result)
        return jsonify(result), HTTPStatus.OK
    except Exception as e:
        return jsonify({"error": str(e)}), 422

        
@bp.route('/api/formula', methods=['PUT'])
@use_args(UpdateFomulaSchema(), location='json')
def update_formula(args: dict):
    try:
        result = FormulaBLC.update_formula(args)
        formula_schema = FormulaSchema()
        result = formula_schema.dump(result)
        return jsonify({"message":"Formula updated succefully","result":result}),HTTPStatus.OK
    except NotFoundException as e:
        return jsonify({'error': str(e)}),HTTPStatus.NOT_FOUND
    except SQLAlchemyError as e:
        return jsonify({"error": "An error occurred while updating the formula"}), HTTPStatus.INTERNAL_SERVER_ERROR
    except ValueError:
        return jsonify({"error": "Invalid formula ID"}), HTTPStatus.BAD_REQUEST