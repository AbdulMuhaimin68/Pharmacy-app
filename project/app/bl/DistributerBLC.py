from sqlalchemy.orm import session as Session
from project.app.repositories.DistributerRepository import DistributerRepository
from project.app.exceptions import NotFoundException
from project.app.db import db


class DistributerBLC:
    @staticmethod
    def get_session():
        return db.session
    
    @staticmethod
    def add_distributer(args:dict):
        session: Session = DistributerBLC.get_session()
        result = DistributerRepository.add_distributer(args,session)
        session.commit()
        return result
    
    @staticmethod
    def get_distributers(args:dict):
        session = DistributerBLC.get_session()
        try:
            res = DistributerRepository.get_distributers(session,**args)
            return res
        except Exception as e:
            raise e
    
    @staticmethod
    def update_distributer(args:dict):
        session:Session = DistributerBLC.get_session()
        try:
            distributer = DistributerRepository.get_distributer_by_id(session, args.get('id'))
            if not distributer:
                raise NotFoundException('Distributer not Found!')
            distributer = DistributerRepository.update_distributer(distributer,args)
            session.commit()
            return distributer       
        except Exception as e:
            session.rollback()
            raise e
        
    @staticmethod
    def delete_distributer_by_id(args):
        session: Session = DistributerBLC.get_session()
        try:
            result = DistributerRepository.delete_distributer(args,session)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e
        
        
        
        
         
        
        