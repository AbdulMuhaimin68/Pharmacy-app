from project.app.models.user import User
from flask_jwt_extended import create_access_token
from project.app.db import db

class LoginRepository:
    
    @staticmethod
    def get_session():
        return db.session
    
    @staticmethod
    def login(args, session):
        username = args.get('username')
        password = args.get('password')

        user = session.query(User).filter(User.username == username).first()
        if not user or not user.check_password(password):
            return {'message': 'Invalid username or password'}

        access_token = create_access_token(identity=username)
        return access_token