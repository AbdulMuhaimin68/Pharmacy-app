from project.app.db import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import func
from sqlalchemy.orm import object_session
from project.app.models.stock import Stock
    
# Define the Product model
class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False,unique=True)
    formula_id = db.Column(db.Integer, db.ForeignKey('formula.id'), nullable=False)
    per_pack = db.Column(db.Integer, nullable=False)
    average_quantity = db.Column(db.Integer, nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    distribution_id = db.Column(db.Integer, db.ForeignKey('distributor.id'), nullable=False)
    description = db.Column(db.Text, nullable=True)

    formula = db.relationship('Formula', back_populates='products')
    stocks = db.relationship('Stock', back_populates='product')
    company = db.relationship('Company', back_populates='products')
    distributor = db.relationship('Distributor', back_populates='products')
    
    @hybrid_property
    def total_qty(self):
        session = object_session(self)
        total = session.query(func.sum(Stock.quantity)).filter(Stock.product_id == self.id).scalar()
        return total if total is not None else 0
    
    @total_qty.expression
    def total_qty(cls):
        return (
            db.session.query(func.coalesce(func.sum(Stock.quantity), 0))
            .filter(Stock.product_id == cls.id)
            .label("total_qty")
        )
        