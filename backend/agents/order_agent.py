from sqlalchemy.orm import Session
from ..database.models import Order, Customer
from ..llm.llm_client import query_llm, query_llm_text

class OrderAgent:
    def __init__(self, db: Session):
        self.db = db

    def handle_request(self, user_input: str, customer_id: int = None) -> dict:
        # 1. Identify intent specifics using LLM
        system_prompt = "Extract the order ID if present, or identify if the user is asking about their latest order."
        extraction = query_llm(user_input, system_prompt)
        
        # 2. Fetch data from DB
        response_data = {}
        if customer_id:
            # Simplified: Get latest order for customer
            order = self.db.query(Order).filter(Order.customer_id == customer_id).order_by(Order.last_updated.desc()).first()
            if order:
                response_data = {
                    "order_id": order.order_id,
                    "status": order.status,
                    "location": order.current_location,
                    "last_updated": str(order.last_updated)
                }
            else:
                return {"response": "I couldn't find any orders for you."}
        else:
            # For demo, just mock or say need login
            return {"response": "Please provide your customer ID to check orders."}

        # 3. Generate response using LLM (Text Mode)
        context = f"Order Data: {response_data}"
        system_prompt = f"You are a helpful assistant. Use the provided Order Data to answer the user's question. Be concise. Context: {context}"
        final_response_text = query_llm_text(user_input, system_prompt)
        
        return {
            "response": final_response_text,
            "data": response_data
        }
