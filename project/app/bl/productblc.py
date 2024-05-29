from project.app.repositories.productrepository import ProductRepository
from project.app.db import db
from flask import request, jsonify

class ProductBLC:
    @staticmethod
    def get_session():
        return db.session
    
    @staticmethod
    def add_product(args):
        session = ProductBLC.get_session()
        result = ProductRepository.adding_product(session,args)
        return result