from flask import Blueprint,jsonify
from webargs.flaskparser import use_args
from project.app.schemas.UserSchema import UserSchema, LoginSchema
from project.app.bl.LoginBLC import LoginBLC
from project.app.bl.UserBLC import UserBLC
from flask_jwt_extended import get_jwt, jwt_required, get_jwt_identity, current_user
from sqlalchemy.exc import IntegrityError

bp = Blueprint('user',__name__)

@bp.route('/api/register', methods=['POST'])
@use_args(UserSchema(), location='json')
@jwt_required()
def add_user(args):
    """Adding a user to a Database"""
    
    if current_user.role != 'admin':
        return "Admin privileges required"
    
    try:
        result = UserBLC.add_user(args)
        
        return jsonify({"message":"User added succefully","result":result}),201
    except IntegrityError as e:
        return jsonify({"Error":e.orig.args[1]}), 422
    except Exception as e:
        return jsonify(str(e)),422
    
@bp.route('/api/login', methods=['POST'])
@use_args(LoginSchema(), location='json')
def login(args):
    """Login User"""
    
    try:
        result = LoginBLC.login(args)
        
        return jsonify({"result":result})
    except IntegrityError as e:
        return jsonify({"Error":e.orig.args[1]}), 422
    except Exception as e:
        return jsonify(str(e)),422