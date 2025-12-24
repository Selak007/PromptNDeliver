from ..llm.llm_client import query_llm

class DecisionEngine:
    def decide_agent(self, user_input: str, context: dict = None) -> dict:
        """
        Uses LLM to decide which agent to handle the request.
        """
        system_prompt = """
        You are the Brain of a Customer Service System. Route the user's request to the correct agent.
        
        AGENTS:
        - "order_agent": Use for questions about order status, shipping, tracking, delivery, or "Where is my order?".
        - "product_agent": Use for questions about buying products, price, stock, or features.
        - "feedback_agent": Use for complaints, reviews, or happiness.
        
        EXAMPLES:
        User: "Where is my order?"
        Output: {"intent": "order_tracking", "urgency": "high", "agent": "order_agent"}

        User: "I want to buy a laptop"
        Output: {"intent": "purchase_query", "urgency": "low", "agent": "product_agent"}
        
        OUTPUT JSON ONLY:
        """
        
        response = query_llm(user_input, system_prompt)
        return response
