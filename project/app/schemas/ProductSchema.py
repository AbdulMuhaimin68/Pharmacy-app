from marshmallow import Schema, fields, validate
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from project.app.models.product import Product
from project.app.schemas.CompanySchema import CompanySchema, GetCompanySchema
from project.app.schemas.DistributerSchema import DistributerSchema
from project.app.schemas.FormulaSchema import FormulaSchema
from project.app.schemas.StockSchema import StockSchema
from marshmallow import post_dump, pre_dump

class ProductSchema(Schema):
    product_name = fields.Str(required=True, validate=validate.Length(max=100, error="Give Shorter Name"))
    formula_id = fields.Int(required=True)
    per_pack = fields.Int(required=True)
    company_id = fields.Int(required=True)
    distribution_id = fields.Int(required=True)
    description = fields.Str()
    
    
    
class GetProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        include_fk = False
        
    formula = fields.Nested(FormulaSchema)
    company = fields.Nested(GetCompanySchema)
    distributor = fields.Nested(DistributerSchema)
    stocks = fields.Nested(StockSchema(many=True))

    @post_dump
    def total_qty(self, data, **args):
        total_qty = sum(dct["quantity"] for dct in data.get("stocks")) if data.get("stocks") else 0
        data["total_qty"] = total_qty
        return data
    
class ProductSearchSchema(Schema):
    search = fields.String(required=False)
    company_id = fields.Integer(required=False)
    formula_id = fields.Integer(required=False)
    distributer_id = fields.Integer(required=False)
    short_stock = fields.Boolean(required=False)
    short_expiry = fields.Boolean(required=False)
    expired = fields.Boolean(required=False)
    sort = fields.String(required=False, validate=lambda x: x in ['price_asc', 'price_desc'])
