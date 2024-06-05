from marshmallow import Schema,fields,validate

class DistributerSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True,validate=validate.Length(max=100))
    address = fields.String(validate=validate.Length(max=200))
    contact_number = fields.String(validate=validate.Length(max=50))
    email = fields.Email()
    
class UpdateDistributerSchema(DistributerSchema):
    id = fields.Integer(required=True)
    