from project.app.repositories.productrepository import ProductRepository
from sqlalchemy.orm import session as Session
from project.app.db import db



class ProductBLC:
    @staticmethod
    def get_session():
        return db.session
    
    @staticmethod
    def add_product(args):
        session = ProductBLC.get_session()
        
        try:
            result = ProductRepository.adding_product(session, args)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e
        
    @staticmethod
    def get_products(args:dict):
        session:Session = ProductBLC.get_session()
        
        try:
            result = ProductRepository.get_products(args,session=session)
            return result
        except Exception as e:
            raise e