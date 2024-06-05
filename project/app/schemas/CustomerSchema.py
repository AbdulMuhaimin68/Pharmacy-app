from marshmallow import Schema,fields,validate
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from project.app.models.customer import Customer

# class CustomerSchema(Schema):
#     id = fields.Int(dump_only=True)
#     name = fields.Str(required=True, validate=validate.Length(max=100))
#     contact = fields.Str(validate=validate.Length(max=50))
#     address = fields.Str(validate=validate.Length(max=200))

class CustomerSchema(SQLAlchemyAutoSchema):
    class Meta: 
        model = Customer
        
class GetCustomerSchema(CustomerSchema):
    ...
  
class AddCustomerSchema(CustomerSchema):
    name = fields.String(validate=validate.Length(min=3))
    pass

class EditCustomerSchema(AddCustomerSchema):
    ...