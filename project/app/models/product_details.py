from project.app.db import db

class ProductDetails(db.Model):
    __tablename__ = 'product_details'
    id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    sku = db.Column(db.String(50), default=None)
    
    product = db.relationship('Product', back_populates='product_detail')