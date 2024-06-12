from sqlalchemy.orm import session as Session
from project.app.repositories.CompanyRepository import CompanyRepository
from project.app.exceptions import NotFoundException
from project.app.db import db


class CompanyBLC:
    # Better to have this function in CompanyRepository
    def get_session():
        return db.session
    
    @staticmethod
    def add_company(args):
        session:Session = CompanyBLC.get_session()
        
        try:
            result = CompanyRepository.add_company(args,session)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e
        
    @staticmethod
    def get_company(args:dict):
        session:Session = CompanyBLC.get_session()
        try:
            result = CompanyRepository.get_company(session,**args)
            return result
        except Exception as e:
            raise e
        
    @staticmethod
    def update_company(args:dict):
        session:Session = CompanyBLC.get_session()
        
        try:
            company = CompanyRepository.get_company_by_id(session, args.get('id'))
            if not company:
                raise NotFoundException('Company not Found')
            
            result = CompanyRepository.update_company(company,args)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e
        
    @staticmethod 
    def delete_company_by_id(company_id):
        session: Session = CompanyBLC.get_session()
        
        try:
            result = CompanyRepository.delete_company(company_id, session)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
        