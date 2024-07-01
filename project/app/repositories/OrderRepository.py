from project.app.db import db
from project.app.models import stock_order
from project.app.models.order import Order
from project.app.models.stock import Stock
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound


class OrderRepository:
    @staticmethod
    def add_order(data, session):
        try:
            customer_id = data['customer_id']
            stock_items = data['products']
            
            total_amount = 0
            stock_updates = []
            
            for item in stock_items:
                product_id = item['product_id']
                quantity = item['quantity']
                
                try:
                    stock = session.query(Stock).filter(Stock.product_id == product_id, Stock.quantity >= quantity).one()
                except NoResultFound:
                    raise NoResultFound(f"Not enough stock for product_id: {product_id}")
                except MultipleResultsFound:
                    stock = session.query(Stock).filter(Stock.product_id == product_id, Stock.quantity >= quantity).first()
                    if not stock:
                        raise NoResultFound(f"Not enough stock for product_id: {product_id}")
                
                total_amount += stock.price * quantity
                
                stock.quantity -= quantity
                stock_updates.append((stock, quantity))
            
            new_order = Order(customer_id=customer_id, total_amount=total_amount)
            session.add(new_order)
            session.flush()
            
            for stock, quantity in stock_updates:
                stock_order_entry = stock_order.StockOrder.insert().values(order_id=new_order.order_id, stock_id=stock.id, quantity=quantity)
                session.execute(stock_order_entry)
            
            session.commit()
            
            session.refresh(new_order)
            
            for stock, quantity in stock_updates:
                session.refresh(stock)
            receipt = OrderRepository.prepare_receipt(new_order, stock_updates)
            
            return receipt
        
        except Exception as e:
            session.rollback()
            raise e
        
        finally:
            session.close()

    @staticmethod
    def prepare_receipt(new_order, stock_updates):
        receipt = {
            "customer_id": new_order.customer_id,
            "total_amount": new_order.total_amount,
            "items": []
        }
        
        for stock, quantity in stock_updates:
            product = stock.product
            receipt["items"].append({
                "product_id": product.id,
                "product_name": product.product_name,
                "quantity_ordered": quantity,
                "price_per_pack": stock.price,
                "total_price": stock.price * quantity,
                "stock_details": {
                    "available_quantity": stock.quantity,
                    "expiry_date": stock.expiry_date
                }
            })
        
        return receipt  # Return the full receipt details 
            
    @staticmethod  
    def get_order(session,id=None):
        query = session.query(Order)
        if id:
            query = query.filter(Order.order_id == id)
        return query.all()
    
    @staticmethod
    def get_order_by_id(session, id=None):
        query = session.query(Order)
        if id:
            query = query.filter(Order.order_id == id)
        return query.first()
    
    @staticmethod
    def update_order(order,args):
        order.customer_id = args.get('customer_id',order.customer_id)
        order.discount = args.get('discount',order.discount)
        order.total_amount = args.get('total_amount',order.total_amount)
        
        return order
    
    @staticmethod
    def delete_order(args,session):
        try:
            result = session.query(Order).filter(Order.order_id == args.get('id')).first()
            session.delete(result)
            session.flush()
            return result
        except Exception as e:
            session.rollback()
            raise e