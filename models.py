from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import ChoiceType

db = create_engine("sqlite:///bank.db")

Base = declarative_base()

#create a table w/
# User
# Order
# OrderIten

class User(Base):
    __tablename__ = "Users"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    email = Column("email", String, nullable=False)
    password = Column("password", String, nullable=False)
    active = Column("active", Boolean)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, name, email, password, active=True, admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        self.admin = admin

class Order(Base):
    __tablename__ = "Orders"

    #ORDER_STATUS = [
    #    ("PENDING", "Pending"),
    #    ("CANCELED", "Canceled"),
    #    ("FINALIZED", "Finalized")
    #]

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String) # PENDING, CANCELED, FINALIZED
    user = Column("user", ForeignKey("Users.id"))
    price = Column("price", Float)
    # itens = 

    def __init__(self, user, status="PENDING", price=0):
        self.user = user
        self.price = price
        self.status = status
    
    def calculate_price(self):
        self.price = 10
        

class OrderItem(Base):
    __tablename__ = "OrderItens"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantity = Column("quantity", Integer)
    flavor = Column("flavor", String)
    size = Column("size", String)
    unity_price = Column("unity_price", Float)
    order = Column("order", ForeignKey("Orders.id"))

    def __init__(self, quantity, flavor, size, unity_price, order):
        self.quantity = quantity
        self.flavor = flavor
        self.size = size
        self.unity_price = unity_price
        self.order = order