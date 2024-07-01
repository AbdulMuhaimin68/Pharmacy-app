from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from project.app.models.stock import Stock


class StockSchema(SQLAlchemyAutoSchema):
    id = fields.Int(dump_only=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)
    price = fields.Float(required=True)
    expiry_date = fields.Date(allow_none=True)
    entry_date = fields.Date(dump_only=True)
    
class PostStockSchema(StockSchema):
    ...
    
class UpdateStockSchema(StockSchema):
    product_id = fields.Int(required=False)
    quantity = fields.Int(required=False)
    price = fields.Float(required=False)
    expiry_date = fields.Date(allow_none=True, required=False)
    entry_date = fields.Date(required=False)
        