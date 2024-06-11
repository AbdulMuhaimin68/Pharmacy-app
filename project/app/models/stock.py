from datetime import datetime
from project.app.db import db

class Stock(db.Model):
    __tablename__ = 'stock'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    expiry_date = db.Column(db.Date, nullable=True)
    entry_date = db.Column(db.Date, default=datetime.utcnow, nullable=False)

    orders = db.relationship('Order', secondary='stock_order', back_populates='stocks')
    product = db.relationship('Product', back_populates='stocks')
