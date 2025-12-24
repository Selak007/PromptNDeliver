import requests
import json

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "tinyllama" # Switched to tinyllama for speed

def query_llm(prompt: str, system_prompt: str = None) -> dict:
    """
    Sends a prompt to the Ollama LLM and returns the JSON response.
    """
    print(f"DEBUG: Querying LLM with prompt: {prompt[:50]}...") # Debug log
    full_prompt = prompt
    if system_prompt:
        full_prompt = f"System: {system_prompt}\nUser: {prompt}"

    payload = {
        "model": MODEL,
        "prompt": full_prompt,
        "stream": False,
        "format": "json" # Force JSON output
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        response.raise_for_status()
        result = response.json()
        raw_response = result['response']

        # JSON Extraction Logic
        try:
            start = raw_response.find('{')
            end = raw_response.rfind('}') + 1
            if start != -1 and end != -1:
                json_str = raw_response[start:end]
                return json.loads(json_str)
            else:
                raise ValueError("No JSON found in response")
        except json.JSONDecodeError:
            print(f"WARNING: Failed to parse JSON. Raw: {raw_response}")
            # Fallback for tinyllama if it fails to produce valid JSON
            if "order_agent" in raw_response:
                return {"intent": "order_tracking", "urgency": "high", "agent": "order_agent"}
            elif "product_agent" in raw_response:
                return {"intent": "product_query", "urgency": "low", "agent": "product_agent"}
            return {"error": "Invalid JSON", "raw": raw_response}

    except requests.exceptions.Timeout:
        print("ERROR: Ollama request timed out!")
        return {"error": "LLM timed out"}
    except requests.exceptions.RequestException as e:
        print(f"Error querying Ollama: {e}")
        return {"error": str(e)}

def query_llm_text(prompt: str, system_prompt: str = None) -> str:
    """
    Sends a prompt to the Ollama LLM and returns the raw text response.
    """
    full_prompt = prompt
    if system_prompt:
        full_prompt = f"System: {system_prompt}\nUser: {prompt}"

    payload = {
        "model": MODEL,
        "prompt": full_prompt,
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        response.raise_for_status()
        result = response.json()
        return result['response']
    except Exception as e:
        print(f"Error querying Ollama (Text): {e}")
        return "I'm having trouble thinking right now."
    except json.JSONDecodeError:
        print(f"Failed to decode LLM response: {result['response']}")
        return {"error": "Invalid JSON response from LLM"}

def check_ollama_status():
    try:
        response = requests.get("http://localhost:11434/")
        return response.status_code == 200
    except:
        return False
