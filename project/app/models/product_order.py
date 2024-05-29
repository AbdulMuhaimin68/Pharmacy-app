from project.app.db import db


ProductOrder = db.Table('product_order',
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True),
    db.Column('order_id', db.Integer, db.ForeignKey('order.order_id'), primary_key=True)
)