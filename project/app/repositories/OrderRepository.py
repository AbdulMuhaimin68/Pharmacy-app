from project.app.db import db
from project.app.models.order import Order
from sqlalchemy.orm import session as Session
from sqlalchemy.exc import IntegrityError
from project.app.exceptions import DuplicateError,NotFoundException


class OrderRepository:
    @staticmethod
    def adding_order(args: dict, session: Session = db.session):
        order: Order = Order(**args)
        session.add(order)
        try:
            session.flush()
        except IntegrityError as e:
            session.rollback()
        return order
    
    @staticmethod  
    def get_order(session,id=None):
        query = session.query(Order)
        if id:
            query = query.filter(Order.order_id == id)
        return query.all()
    
    @staticmethod
    def get_order_by_id(session, id=None):
        query = session.query(Order)
        if id:
            query = query.filter(Order.order_id == id)
        return query.first()
    
    @staticmethod
    def update_order(order,args):
        order.customer_id = args.get('customer_id',order.customer_id)
        order.discount = args.get('discount',order.discount)
        order.total_amount = args.get('total_amount',order.total_amount)
        
        return order
    
    @staticmethod
    def delete_order(args,session):
        try:
            result = session.query(Order).filter(Order.order_id == args.get('id')).first()
            session.delete(result)
            session.flush()
            return result
        except Exception as e:
            session.rollback()
            raise e