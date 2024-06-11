from project.app.db import db
from datetime import datetime

class Order(db.Model):
    __tablename__ = 'order'
    order_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    discount = db.Column(db.Float, nullable=True)
    total_amount = db.Column(db.Float, nullable=False)
    
    stocks = db.relationship('Stock', secondary='stock_order', back_populates='orders')
    customer = db.relationship('Customer', back_populates='orders')