from marshmallow import Schema, fields, validate

class ProductSchema(Schema):
    product_name = fields.Str(required=True, validate=validate.Length(max=100, error="Give Shorter Name"))
    formula_id = fields.Int(required=True)
    per_pack = fields.Int(required=True)
    company_id = fields.Int(required=True)
    distribution_id = fields.Int(required=True)
    description = fields.Str()
    
class GetProductSchema(ProductSchema):
    class meta:
        fields = ('product_name', 'formula_id', 'per_pack', 'company_id', 'distribution_id')
