from marshmallow import Schema,fields,validate
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from datetime import datetime

class OrderSchema(Schema):
    order_id = fields.Integer(dump_onle=True)
    customer_id = fields.Int(required=True)
    discount = fields.Float()
    total_amount = fields.Float(required=True)