import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure API
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

def query_api(prompt):
    """Query the Google Gemini API with a prompt"""
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.7,
                max_output_tokens=500
            )
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying API...")
    result = query_api(user_prompt)
    print("Response:\n", result)
