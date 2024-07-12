from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

class ProductDetailSchema(SQLAlchemyAutoSchema):
    sku = fields.String()