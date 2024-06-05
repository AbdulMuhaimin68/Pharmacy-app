from project.app.db import db
from project.app.models.formula import Formula
from sqlalchemy.orm import session as Session
from sqlalchemy.exc import IntegrityError
from project.app.exceptions import DuplicateError,NotFoundException


class FormulaRepository:
    @staticmethod
    def adding_formula(args: dict, session: Session = db.session):
        formula: Formula = Formula(**args)
        session.add(formula)
        try:
            session.flush()
        except IntegrityError as e:
            session.rollback()
            raise DuplicateError("Formula with same name already exists!")
        return formula
    
    @staticmethod
    def get_formula(session, id=None):
        query = session.query(Formula)
        if id:
            query = query.filter(Formula.id == id)
        return query.all()
    
    @staticmethod
    def get_formula_by_id(session, id=None):
        query = session.query(Formula)
        if id:
            query = query.filter(Formula.id == id)
        return query.first()
    
    @staticmethod
    def update_formula(formula, args):
        formula.description = args.get('description', formula.description)
        formula.disease = args.get('disease', formula.disease)
        formula.formula_name = args.get('formula_name', formula.formula_name)
        return formula
    
    @staticmethod
    def delete_formula(args,session):
        
        try:
            result = session.query(Formula).filter(Formula.id == args.get('id')).first()
            session.delete(result)
            session.flush()
            return result
        except Exception as e:
            session.rollback()
            raise e
            
    
        
        
        