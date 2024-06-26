from project.app.db import db
from project.app.models.stock import Stock



class StockRepository:
    
    @staticmethod
    def get_session():
        return db.session
    
    @staticmethod
    def add_stock(args,session):
        
        try:
            stock:Stock = Stock(**args)
            session.add(stock)
            session.flush()
            return stock
        except Exception as e:
            session.rollback()
            raise e
        
    @staticmethod
    def get_stock(session, id=None):
        query = session.query(Stock)
        if id:
            query = query.filter(Stock.id == id)
        return query.all()
    
    @staticmethod
    def get_stock_by_id(session, id=None):
        query = session.query(Stock)
        if id:
            query = query.filter(Stock.id == id)
        return query.first()
    
    @staticmethod
    def update_stock(stock,args):
        stock.product_id = args.get('product_id', stock.product_id)
        stock.quantity = args.get('quantity', stock.quantity)
        stock.price = args.get('price', stock.price)
        stock.expiry_date = args.get('expiry_date', stock.expiry_date)
        stock.entry_date = args.get('entry_date', stock.entry_date)
        
        return stock
    
    @staticmethod
    def delete_stock(session, id=None):
        try:
            stock = session.query(Stock).filter(Stock.id==id).first()
            if not stock:
                raise ValueError(f"Stock with id {id} does not exist")
            session.delete(stock)
            session.flush()
            return {"id": id, "status": "deleted"}
        except Exception as e:
            session.rollback()
            raise e
            
    
    
            