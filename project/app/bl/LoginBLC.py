from sqlalchemy.orm import session as Session
from project.app.repositories.LoginRepository import LoginRepository

class LoginBLC:
    
    @staticmethod
    def login(args):
        session:Session = LoginRepository.get_session()
        
        try:
            result = LoginRepository.login(args,session)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e