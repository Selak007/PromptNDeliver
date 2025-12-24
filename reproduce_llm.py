from backend.llm.llm_client import query_llm
import json

def test_decision():
    user_input = "Where is my order?"
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
    
    print("Sending prompt to LLM...")
    try:
        response = query_llm(user_input, system_prompt)
        print("\n--- PARSED RESPONSE ---")
        print(json.dumps(response, indent=2))
    except Exception as e:
        print(f"\n--- ERROR ---")
        print(e)

if __name__ == "__main__":
    test_decision()
