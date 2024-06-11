from project.app.db import db
    
# Define the Product model
class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False,unique=True)
    formula_id = db.Column(db.Integer, db.ForeignKey('formula.id'), nullable=False)
    per_pack = db.Column(db.Integer, nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    distribution_id = db.Column(db.Integer, db.ForeignKey('distributor.id'), nullable=False)
    description = db.Column(db.Text, nullable=True)

    formula = db.relationship('Formula', back_populates='products')
    stocks = db.relationship('Stock', back_populates='product')
    company = db.relationship('Company', back_populates='products')
    distributor = db.relationship('Distributor', back_populates='products')