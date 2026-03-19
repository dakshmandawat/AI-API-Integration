import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Configure API
api_key = os.getenv("HUGGINGFACE_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"
headers = {"Authorization": f"Bearer {api_key}"}

def query_api(prompt):
    """Query the Hugging Face API with a prompt"""
    try:
        payload = {
            "inputs": prompt,
            "parameters": {"max_new_tokens": 500, "temperature": 0.7}
        }
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()[0].get("generated_text", "")
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying API...")
    result = query_api(user_prompt)
    print("Response:\n", result)
