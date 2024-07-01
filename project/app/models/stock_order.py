from project.app.db import db


StockOrder = db.Table('stock_order',
    db.Column('stock_id', db.Integer, db.ForeignKey('stock.id'), primary_key=True),
    db.Column('order_id', db.Integer, db.ForeignKey('order.order_id'), primary_key=True),
    db.Column('quantity', db.Integer, nullable=False)
)