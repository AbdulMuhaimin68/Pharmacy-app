from sqlalchemy.orm import session as Session
from project.app.exceptions import NotFoundException
from project.app.repositories.StockRepository import StockRepository


class StockBLC:
        
    @staticmethod
    def add_stock(args):
        session:Session = StockRepository.get_session()
        try:
            result = StockRepository.add_stock(args,session)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e
        
    @staticmethod
    def get_stock(args):
        session:Session = StockRepository.get_session()
        try:
            result = StockRepository.get_stock(session,**args)
            return result
        except Exception as e:
            raise e
        
    @staticmethod
    def update_stock(args:dict):
        session:Session = StockRepository.get_session()
        
        try:
            stock = StockRepository.get_stock_by_id(session, args.get('id'))
            if not stock:
                raise NotFoundException('Stock not found!')
            
            result = StockRepository.update_stock(stock,args)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e
        
    @staticmethod
    def delete_stock_by_id(stock_id):
        session:Session = StockRepository.get_session()
        try:
            result = StockRepository.delete_stock(session,stock_id)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e
        
    
        