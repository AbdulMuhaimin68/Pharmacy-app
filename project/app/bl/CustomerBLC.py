from project.app.db import db
from sqlalchemy.orm import session as Session
from project.app.repositories.CustomerRepository import CustomerRepository
from project.app.exceptions import NotFoundException

class CustomerBLC:
    def get_session():
        return db.session
    
    @staticmethod
    def add_customer(args):
        session:Session = CustomerBLC.get_session()
        try:
            result = CustomerRepository.add_customer(args,session)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e
    
    @staticmethod
    def get_customer(args):
        session:Session = CustomerBLC.get_session()
        try:
            result = CustomerRepository.get_customer(session,**args)
            return result
        except Exception as e:
            raise e
    
    @staticmethod
    def update_customer(args:dict):
        session : Session = CustomerBLC.get_session()
        try:
            customer = CustomerRepository.get_customer_by_id(session,args.get('id'))
            if not customer:
                raise NotFoundException('Customer not found!')
            result = CustomerRepository.update_customer(customer,args)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e
        
        
    @staticmethod
    def delete_customer_by_id(args):
        session: Session = CustomerBLC.get_session()
        try:
            result = CustomerRepository.delete_customer(args,session)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e
        
        
        