from project.app.db import db

class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    address = db.Column(db.String(200), nullable=True)
    contact_number = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(100), nullable=True, unique=True)
    distributor_id = db.Column(db.Integer, db.ForeignKey('distributor.id'))

    products = db.relationship('Product', back_populates='company')
    distributor = db.relationship('Distributor', back_populates='companies')