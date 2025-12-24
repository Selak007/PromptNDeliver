from sqlalchemy.orm import Session
from database.db import SessionLocal, engine
from database.models import Base, Customer, Order, Product
import datetime

# Create tables
Base.metadata.create_all(bind=engine)

def seed_data():
    db = SessionLocal()
    
    # Check if data exists
    if db.query(Customer).first():
        print("Data already seeded.")
        return

    # Create Customers
    customer1 = Customer(name="Alice Smith", email="alice@example.com")
    customer2 = Customer(name="Bob Jones", email="bob@example.com")
    db.add(customer1)
    db.add(customer2)
    db.commit()
    db.refresh(customer1)
    db.refresh(customer2)

    # Create Products
    prod1 = Product(name="Laptop Pro", category="Electronics", price=1200.00)
    prod2 = Product(name="Wireless Headphones", category="Audio", price=150.00)
    db.add(prod1)
    db.add(prod2)
    db.commit()

    # Create Orders
    order1 = Order(customer_id=customer1.id, status="In Transit", current_location="Distribution Center, NY")
    order2 = Order(customer_id=customer2.id, status="Delivered", current_location="Front Porch")
    db.add(order1)
    db.add(order2)
    db.commit()

    print("Database seeded successfully!")
    db.close()

if __name__ == "__main__":
    seed_data()
