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
            # Extract customer_id and products from the incoming data
            customer_id = data['customer_id']
            stock_items = data['products']
            
            # Initialize variables to calculate total amount and track stock updates
            total_amount = 0
            stock_updates = []
            
            # Process each item in the order
            for item in stock_items:
                product_id = item['product_id']
                quantity = item['quantity']
                
                # Query the stock for the product with sufficient quantity
                try:
                    stock = session.query(Stock).filter(Stock.product_id == product_id, Stock.quantity >= quantity).one()
                except NoResultFound:
                    raise NoResultFound(f"Not enough stock for product_id: {product_id}")
                except MultipleResultsFound:
                    stock = session.query(Stock).filter(Stock.product_id == product_id, Stock.quantity >= quantity).first()
                    if not stock:
                        raise NoResultFound(f"Not enough stock for product_id: {product_id}")
                
                # Calculate total amount for the order
                total_amount += stock.price * quantity
                
                # Update stock quantity and track changes
                stock.quantity -= quantity
                stock_updates.append((stock, quantity))
            
            # Create a new order object and add it to the session
            new_order = Order(customer_id=customer_id, total_amount=total_amount)
            session.add(new_order)
            session.flush()  # Flush to generate order_id
            
            # Record stock orders for each item in the order
            for stock, quantity in stock_updates:
                stock_order_entry = stock_order.StockOrder.insert().values(order_id=new_order.order_id, stock_id=stock.id, quantity=quantity)
                session.execute(stock_order_entry)
            
            # Commit changes to the database
            session.commit()
            
            # Refresh new_order to get updated database state
            session.refresh(new_order)
            
            # Reload stock objects to reflect changes made by the database triggers or defaults
            for stock, quantity in stock_updates:
                session.refresh(stock)
            
            # Prepare the receipt details
            receipt = OrderRepository.prepare_receipt(new_order, stock_updates)
            
            return receipt  # Return the full receipt details
        
        except Exception as e:
            session.rollback()  # Rollback changes in case of any exception
            raise e
        
        finally:
            session.close()  # Close the session to release resources

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