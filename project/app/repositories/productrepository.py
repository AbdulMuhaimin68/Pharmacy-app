from project.app.db import db
from project.app.models.product import Product


class ProductRepository:
    
    @staticmethod
    def adding_product(session, args):
        try:
            product:Product = Product(**args)
            session.add(product)
            session.flush()
            return product
        except Exception as e:
            session.rollback()
            raise e





