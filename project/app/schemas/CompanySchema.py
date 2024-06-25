from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from project.app.models.company import Company
from marshmallow import fields, validate, post_load
from project.app.schemas.DistributerSchema import DistributerSchema
class CompanySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Company
        include_fk = True
    
    name = fields.String(required=True, validate=validate.Length(min=3, error="Company name must be of atleast 3 characters"))
    email = fields.Email()
    
    @post_load
    def upper_name(self, data, **kwargs):
        data['name'] = data['name'].title()
        return data
    
class GetCompanySchema(CompanySchema):
    class Meta:
        exclude = ["distributor_id"]
        include_fk = False
        
    distributor_name = fields.String(attribute="distributor.name")