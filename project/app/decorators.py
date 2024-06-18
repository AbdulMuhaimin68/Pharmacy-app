from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt,current_user
from flask import jsonify

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if current_user.role != 'admin':
            return "Admin privileges required"
        return fn(*args, **kwargs)
    return wrapper
