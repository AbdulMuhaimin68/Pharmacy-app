from project.app.db import db
from project.app.models.formula import Formula
from sqlalchemy.orm import session as Session
from sqlalchemy.exc import IntegrityError
from project.app.exceptions import DuplicateError,NotFoundException


class FormulaRepository:
    @staticmethod
    def adding_formula(session: Session, args: dict):
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
    def update_formula(formula, args):
        formula.description = args.get('description', formula.description)
        formula.disease = args.get('disease', formula.disease)
        formula.formula_name = args.get('formula_name', formula.formula_name)
        return formula
        
    
        
        
        