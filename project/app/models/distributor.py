from project.app.db import db

class Distributor(db.Model):
    __tablename__ = 'distributor'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False,unique=True)
    address = db.Column(db.String(200), nullable=True)
    contact_number = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(100), nullable=True,unique=True)

    products = db.relationship('Product', back_populates='distributor')
    companies = db.relationship('Company', back_populates='distributor')