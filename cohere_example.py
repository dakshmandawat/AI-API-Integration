import os
import cohere
from dotenv import load_dotenv

load_dotenv()

# Configure API
api_key = os.getenv("COHERE_API_KEY")

def query_api(prompt):
    """Query the Cohere API with a prompt"""
    try:
        co = cohere.ClientV2(api_key=api_key)
        response = co.chat(
            model="command-r-plus",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500
        )
        return response.message.content[0].text
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying API...")
    result = query_api(user_prompt)
    print("Response:\n", result)
