from project.app.models.user import User
from flask_jwt_extended import create_access_token
from project.app.db import db
from datetime import timedelta

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

        access_token = create_access_token(identity=username, expires_delta=timedelta(days=30))
        return access_token