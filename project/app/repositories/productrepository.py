from project.app.db import db
from project.app.models.product import Product


class ProductRepository:
    
    @staticmethod
    def adding_product(session, args):
        brand = Product(**args)
        session.add(brand)
        session.commit()
        
        return "Product added Successfully"




