from project.app.repositories.OrderRepository import OrderRepository
from project.app.exceptions import NotFoundException
from project.app.db import db
from sqlalchemy.orm import session as Session


class OrderBLC:
    @staticmethod
    def get_session():
        return db.session
    
    @staticmethod
    def add_order(args: dict):
        session: Session = OrderBLC.get_session()
        result = OrderRepository.add_order(args,session)
        session.commit()
        return result
    
    @staticmethod
    def get_order(args):
        session:Session = OrderBLC.get_session()
        try:
            result = OrderRepository.get_order(session,**args)
            return result
        except Exception as e:
            raise e
        
    @staticmethod
    def update_order(args):
        session: Session = OrderBLC.get_session()
        try:
            order = OrderRepository.get_order_by_id(session,args.get("order_id"))
            if not order:
                raise NotFoundException('Order not Found')
            
            order = OrderRepository.update_order(order,args)
            session.commit()
            return order
        except Exception as e:
            session.rollback()
            raise e
        
    @staticmethod
    def delete_order(args):
        session: Session = OrderBLC.get_session()
        try:
            result = OrderRepository.delete_order(args,session)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e