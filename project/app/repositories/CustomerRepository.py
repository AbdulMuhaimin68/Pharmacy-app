from project.app.models.customer import Customer
from project.app.db import db
from sqlalchemy.orm import session as Session

class CustomerRepository:
    @staticmethod
    def add_customer(args, session:Session=db.Session):
        try:
            customer:Customer = Customer(**args)
            session.add(customer)
            session.flush()
            return customer
        except Exception as e:
            session.rollback()
            raise e
        
    @staticmethod  
    def get_customer(session,id=None):
        query = session.query(Customer)
        if id:
            query = query.filter(Customer.id == id)
        return query.all()
    
    @staticmethod
    def get_customer_by_id(session, id=None):
        query = session.query(Customer)
        if id:
            query = query.filter(Customer.id == id)
        return query.first()
    
    @staticmethod
    def update_customer(customer,args):
        customer.name = args.get('name',customer.name)
        customer.address = args.get('address', customer.address)
        customer.contact = args.get('contact', customer.contact)
        
        return customer
    
    def delete_customer(args,session):
        try:
            result = session.query(Customer).filter(Customer.id == args.get('id')).first()
            session.delete(result)
            session.flush()
            return result
        except Exception as e:
            session.rollback()
            raise e
    
    
        