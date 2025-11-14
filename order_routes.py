from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_session, verify_token
from schemas import OrderSchema, OrderItemSchema
from models import Order, User

order_router = APIRouter(prefix="/orders", tags=["orders"], dependencies=[Depends(verify_token)])

@order_router.get("/")
async def order():
    return {"message": "You acces the order route"}

@order_router.post("/order")
async def create_order(order_schema: OrderSchema, session: Session = Depends(get_session)):
    new_order = Order(user=order_schema.user_id)
    session.add(new_order)
    session.commit()
    return {"message": f"Order created successfully. id={new_order.id}"}

@order_router.post("/order/cancel/{order_id}")
async def cancel_order(order_id: int, session: Session = Depends(get_session), user: User = Depends(verify_token)):
    order = session.query(Order).filter(Order.id==order_id).first()
    if not order:
        raise HTTPException(status_code=400, detail="order not found")
    if not user.admin or user.id != order.user:
        raise HTTPException(status_code=401, detail="Access denied")
    order.status = "CANCELED"
    session.commit()
    return {
        "message": f"Order n: [{order.id}] successfully canceled",
        "order": order
        }

@order_router.get("/list")
async def list_orders(session: Session = Depends(get_session), user: User = Depends(verify_token)):
    if not user.admin:
        raise HTTPException(status_code=401, detail="Access denied")
    else:
        orders = session.query(Order).all
        return {
            "orders": orders
        }

@order_router.post("/order/add-item/{order_id}")
async def add_order_item(order_id: int,
                        order_item_schema: OrderItemSchema,
                        session: Session = Depends(get_session),
                        user: User = Depends(verify_token)):
    order = session.query(Order).filter(Order.id==order_id).first()
    if not order:
        raise HTTPException(status_code=400, detail="Order not exist")
    if not user.admin or user.id != order.user:
        raise HTTPException(status_code=401, detail="Access denied")
    order_item = OrderItemSchema(order_item_schema.quantity,
                                order_item_schema.flavor,
                                order_item_schema.size,
                                order_item_schema.unity_price, 
                                order_id)
    session.add(order_item)
    order.calculate_price()
    session.commit()
    return {
        "message": "Item sucessfuly created",
        "item_id": order_item.id,
        "order_price": order.price 
    }
