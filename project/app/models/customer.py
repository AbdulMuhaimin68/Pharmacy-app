from project.app.db import db

class Customer(db.Model):
    __tablename__ = 'customer'
    
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(50), nullable=True)
    address = db.Column(db.String(200), nullable=True)

    orders = db.relationship('Order', back_populates='customer')