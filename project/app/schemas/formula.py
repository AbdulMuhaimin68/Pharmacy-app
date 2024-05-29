from marshmallow import Schema, fields, validate

class FormulaSchema(Schema):
    id = fields.Integer(dump_only=True)
    formula_name = fields.Str(required=True, validate=validate.Length(max=100))
    disease = fields.Str(required=True, validate=validate.Length(max=100))
    description = fields.Str()
    
class UpdateFomulaSchema(FormulaSchema):
    id = fields.Integer(required=True)
    
# class AddFormulaSchema(FormulaSchema):
#     ...
    