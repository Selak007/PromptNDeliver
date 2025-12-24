from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from .db import Base
import datetime

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)

class Order(Base):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    status = Column(String(50), nullable=False)
    current_location = Column(String(255))
    last_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    
    customer = relationship("Customer")

class Product(Base):
    __tablename__ = "products"
    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    category = Column(String(100))
    price = Column(Float, nullable=False)

class Sale(Base):
    __tablename__ = "sales"
    sale_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.product_id"))
    quantity = Column(Integer, nullable=False)
    sale_date = Column(DateTime, default=datetime.datetime.utcnow)
    
    product = relationship("Product")

class CustomerFeedback(Base):
    __tablename__ = "customer_feedback"
    feedback_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    text = Column(Text, nullable=False)
    sentiment = Column(String(50))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    customer = relationship("Customer")

class AgentLog(Base):
    __tablename__ = "agent_logs"
    log_id = Column(Integer, primary_key=True, index=True)
    agent_name = Column(String(100), nullable=False)
    action_taken = Column(Text, nullable=False)
    result = Column(Text)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

class AgentMemory(Base):
    __tablename__ = "agent_memory"
    memory_id = Column(Integer, primary_key=True, index=True)
    issue_type = Column(String(100), nullable=False)
    frequency = Column(Integer, default=1)
    trend = Column(String(100))
    last_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
