import requests

def query_api(prompt):
    """Query the local Ollama API with a prompt"""
    try:
        url = "http://localhost:11434/api/generate"
        payload = {
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json().get("response", "")
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying API...")
    result = query_api(user_prompt)
    print("Response:\n", result)
