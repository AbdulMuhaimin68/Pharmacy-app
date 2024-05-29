from project.app.repositories.formularepository import FormulaRepository
from project.app.exceptions import NotFoundException
from project.app.db import db
from flask import request, jsonify
from sqlalchemy.orm import session as Session

class FormulaBLC:
    @staticmethod
    def get_session():
        return db.session
    
    @staticmethod
    def add_formula(args: dict):
        session: Session = FormulaBLC.get_session()
        result = FormulaRepository.adding_formula(session, args)
        session.commit()
        return result
    
    @staticmethod
    def get_formulas(args):
        session = FormulaBLC.get_session()
        try:
            res = FormulaRepository.get_formula(session, **args)
            return res
        except NotFoundException as e:
            raise e
        except Exception as e:
            raise e
        
    @staticmethod
    def update_formula(args):
        session: Session = FormulaBLC.get_session()
        try:
            formula = FormulaRepository.get_formula(session,args.get("id"))
            if not formula:
                raise NotFoundException('Formula not Found')
            
            formula = FormulaRepository.update_formula(formula,args)
            session.commit()
            return formula
        except Exception as e:
            session.rollback()
            raise e
        
        
    