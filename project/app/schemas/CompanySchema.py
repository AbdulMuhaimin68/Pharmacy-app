from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from project.app.models.company import Company

class CompanySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Company
        include_fk = True