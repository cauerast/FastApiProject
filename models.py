from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

DATABASE_URL = "sqlite:///bank.db"

db = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db)

Base = declarative_base()


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    active = Column(Boolean)
    admin = Column(Boolean, default=False)

    def __init__(self, name, email, password, active=True, admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        self.admin = admin


class Order(Base):
    __tablename__ = "Orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String)
    user = Column(ForeignKey("Users.id"))
    price = Column(Float, default=0)

    items = relationship("OrderItem", cascade="all, delete", backref="order_obj")

    def __init__(self, user, status="PENDING", price=0):
        self.user = user
        self.status = status
        self.price = price

    def calculate_price(self):
        total = 0
        for item in self.items:
            total += item.unity_price * item.quantity
        self.price = total


class OrderItem(Base):
    __tablename__ = "OrderItems"

    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Integer)
    flavor = Column(String)
    size = Column(String)
    unity_price = Column(Float)
    order_id = Column(Integer, ForeignKey("Orders.id"))

    def __init__(self, quantity, flavor, size, unity_price, order_id):
        self.quantity = quantity
        self.flavor = flavor
        self.size = size
        self.unity_price = unity_price
        self.order_id = order_id

