from project.app.db import db
from project.app.models.product import Product
from project.app.models.stock import Stock
from datetime import datetime, timedelta, date
from sqlalchemy import and_, or_, select, func, asc, desc

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
        
    @staticmethod
    def get_products(args, session):
        query = session.query(Product)
        
        if 'search' in args and args['search']:
            query = query.filter(Product.product_name.ilike(f"%{args['search']}%"))
        
        if 'company_id' in args and args['company_id']:
            query = query.filter(Product.company_id == args['company_id'])
        
        if 'formula_id' in args and args['formula_id']:
            query = query.filter(Product.formula_id == args['formula_id'])
        
        if 'distributer_id' in args and args['distributer_id']:
            query = query.filter(Product.distribution_id == args['distributer_id'])

        if args.get('short_stock'):
            query = query.filter(Product.total_qty < Product.average_quantity)

        current_date = date.today()
        expiration_threshold = current_date + timedelta(days=180)

        if args.get('short_expiry') or args.get('expired'):
            query = query.join(Product.stocks)
            filters = []
            
            if args.get('short_expiry'):
                filters.append(and_(Stock.expiry_date < expiration_threshold, Stock.expiry_date > current_date))
            
            if args.get('expired'):
                filters.append(Stock.expiry_date < current_date)
            query = query.filter(or_(*filters))
            
        if args.get('sort'):
            query = query.join(Product.stocks)
            if args.get('sort') == "price_asc":
                query = query.order_by(asc(Stock.price))
            elif args.get('sort') == "price_desc":
                query = query.order_by(desc(Stock.price))
            
        return query.all()






