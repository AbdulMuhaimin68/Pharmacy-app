from project.app.models.company import Company
from project.app.db import db
from sqlalchemy.orm import joinedload

class CompanyRepository:
    
    @staticmethod
    def get_session():
        return db.session
    
    @staticmethod
    def add_company(args, session):
        try:
            company:Company = Company(**args)
            session.add(company)
            session.flush()
            return company
        except Exception as e:
            session.rollback()
            raise e
        
    @staticmethod
    def get_company(session,id=None):
        query = session.query(Company)
        # query = query.options(joinedload(Company.distributor))
        
        if id:
            query = query.filter(Company.id == id)
        return query.all()
    
    @staticmethod
    def get_company_by_id(session,id=None):
        query = session.query(Company)
        if id:
            query.filter(Company.id == id)
        return query.first()
    
    @staticmethod
    def update_company(company, args):
        company.name = args.get('name', company.name)
        company.address = args.get('address', company.address)
        company.contact_number = args.get('contact_number',company.contact_number)
        company.email = args.get('email',company.email)
        
        return company
    
    @staticmethod
    def delete_company(company_id, session):
        try:
            company = session.query(Company).filter(Company.id==company_id).first()
            if not company:
                raise ValueError(f"Company with id {company_id} does not exist")
            session.delete(company)
            session.flush()
            return {"id": company_id, "status": "deleted"}
        except Exception as e:
            session.rollback()
            raise e
        