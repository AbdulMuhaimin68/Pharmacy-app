from project.app.repositories.productrepository import ProductRepository
from project.app.db import db
from flask import request, jsonify



class ProductBLC:
    @staticmethod
    def get_session():
        return db.session
    
    @staticmethod
    def add_product(args):
        breakpoint()
        session = ProductBLC.get_session()
        
        try:
            result = ProductRepository.adding_product(session, args)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e