from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from project.app.models.order import Order
from project.app.schemas.StockSchema import StockSchema
from project.app.schemas.CustomerSchema import CustomerSchema

class OrderProductSchema(Schema):
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)

class OrderSchema(Schema):
    customer_id = fields.Int(required=True)
    products = fields.List(fields.Nested(OrderProductSchema), required=True)

class ReceiptItemSchema(Schema):
    product_id = fields.Int(required=True)
    product_name = fields.Str(required=True)
    quantity_ordered = fields.Int(required=True)
    price_per_pack = fields.Float(required=True)
    total_price = fields.Float(required=True)
    expiry_date = fields.Date(required=True)

class OrderReceiptSchema(Schema):
    customer_id = fields.Int(required=True)
    total_amount = fields.Float(required=True)
    items = fields.List(fields.Nested(ReceiptItemSchema), required=True)
    
    
class GetOrderSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        include_relationships = True
    stocks = fields.Nested(StockSchema(many=True))
