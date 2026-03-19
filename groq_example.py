import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# Configure API
api_key = os.getenv("GROQ_API_KEY")

def query_api(prompt):
    """Query the Groq API with a prompt"""
    try:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying API...")
    result = query_api(user_prompt)
    print("Response:\n", result)
