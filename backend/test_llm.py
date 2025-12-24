import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

def test_ollama():
    print(f"Testing connection to {OLLAMA_URL} with model {MODEL}...")
    
    payload = {
        "model": MODEL,
        "prompt": "Why is the sky blue?",
        "stream": False,
        "format": "json"
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("Response:", response.json()['response'])
        else:
            print("Error:", response.text)
    except Exception as e:
        print(f"Connection Failed: {e}")

if __name__ == "__main__":
    test_ollama()
