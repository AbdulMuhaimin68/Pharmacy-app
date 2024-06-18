from project.app.models.user import User
from project.app.db import db
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

class UserRepository:
    
    @staticmethod
    def get_session():
        return db.session
    
    @staticmethod
    def add_user(session, args):
        
        try:
            user = User(
                username=args['username'],
                role=args['role']
            )
            user.set_password(args['password'])
            session.add(user)
            session.commit()
            return user
        except IntegrityError as e:
            session.rollback()
            raise ValueError("User already exists")
        except Exception as e:
            session.rollback()
            raise e