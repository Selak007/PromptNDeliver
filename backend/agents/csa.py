from sqlalchemy.orm import Session
from ..decision.decision_engine import DecisionEngine
from ..memory.memory_manager import MemoryManager
from .order_agent import OrderAgent
# Import other agents as needed

class CSA:
    def __init__(self, db: Session):
        self.db = db
        self.decision_engine = DecisionEngine()
        self.memory_manager = MemoryManager(db)
        self.order_agent = OrderAgent(db)

    def process_request(self, user_input: str, customer_id: int = None):
        # 1. Observe & Log Input (Optional, maybe just log action later)
        
        # 2. Reason & Decide
        decision = self.decision_engine.decide_agent(user_input)
        agent_name = decision.get("agent", "unknown")
        intent = decision.get("intent", "unknown")
        urgency = decision.get("urgency", "low")

        # 3. Execute Action
        result = {}
        if agent_name == "order_agent":
            result = self.order_agent.handle_request(user_input, customer_id)
        elif agent_name == "product_agent":
            # result = self.product_agent.handle_request(user_input)
            result = {"response": "Product agent not yet implemented."}
        elif agent_name == "feedback_agent":
            # result = self.feedback_agent.handle_request(user_input)
            result = {"response": "Feedback agent not yet implemented."}
        else:
            result = {"response": "I'm not sure how to help with that."}

        # 4. Update Memory & Logs
        self.memory_manager.log_action(
            agent_name=agent_name,
            action=f"Handled intent: {intent}",
            result=str(result)
        )
        self.memory_manager.update_memory(issue_type=intent, trend=urgency)

        # 5. Return Response
        return {
            "decision": decision,
            "result": result
        }
