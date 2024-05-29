from project.app.db import db

# Define the Formula model
class Formula(db.Model):
    __tablename__ = 'formula'
    id = db.Column(db.Integer, primary_key=True)
    formula_name = db.Column(db.String(100), nullable=False,unique=True)
    disease = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    products = db.relationship('Product', back_populates='formula')