from sqlalchemy.orm import session as Session
from project.app.models.distributor import Distributor
from project.app.exceptions import DuplicateError
from sqlalchemy.exc import IntegrityError
from project.app.db import db

class DistributerRepository:
    @staticmethod
    def add_distributer(args: dict,session:Session = db.session):
        distributer:Distributor = Distributor(**args)
        session.add(distributer)
        try:
            session.flush()
        except IntegrityError as e:
            session.rollback()
            raise DuplicateError('Distributer with same name already exist in database!')
        
        return distributer
    
    @staticmethod
    def get_distributers(session,id=None):
        query = session.query(Distributor)
        if id:
            query = query.filter(Distributor.id == id)
        return query.all()
    
    @staticmethod
    def get_distributer_by_id(session, id=None):
        query = session.query(Distributor)
        if id:
            query = query.filter(Distributor.id == id)
        return query.first()
    
    @staticmethod
    def update_distributer(distributer,args):
        distributer.name = args.get('name',distributer.name)
        distributer.email = args.get('email',distributer.email)
        distributer.contact_number = args.get('contact_number',distributer.contact_number)
        distributer.address = args.get('address',distributer.address)
        return distributer
    
    @staticmethod
    def delete_distributer(args, session):
        try:
            result = session.query(Distributor).filter(Distributor.id == args.get('id')).first()
            session.delete(result)
            session.flush()
            return result
        except Exception as e:
            session.rollback()
            raise e
        
    
        