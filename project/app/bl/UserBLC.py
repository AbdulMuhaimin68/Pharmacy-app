from sqlalchemy.orm import session as Session
from project.app.repositories.UserRepository import UserRepository
from project.app.schemas.UserSchema import UserSchema

class UserBLC:
    @staticmethod
    def add_user(args):
        session = UserRepository.get_session()
        
        with session() as session: 
            user = UserRepository.add_user(session,args)
            
            session.commit()
            user_schema = UserSchema()
            result = user_schema.dump(user)
            return result