import os
import streamlit as st
from dotenv import load_dotenv

# Optional imports handled gracefully
try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

try:
    from groq import Groq
except ImportError:
    Groq = None

try:
    import requests
except ImportError:
    requests = None

try:
    import google.generativeai as genai
except ImportError:
    genai = None

try:
    import cohere
except ImportError:
    cohere = None

load_dotenv()

def query_openai(prompt):
    try:
        if not os.getenv("OPENAI_API_KEY"): return "Error: OPENAI_API_KEY is not set."
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def query_groq(prompt):
    try:
        if not os.getenv("GROQ_API_KEY"): return "Error: GROQ_API_KEY is not set."
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def query_ollama(prompt):
    try:
        url = "http://localhost:11434/api/generate"
        response = requests.post(url, json={"model": "llama3", "prompt": prompt, "stream": False})
        response.raise_for_status()
        return response.json().get("response", "")
    except Exception as e:
        return f"Error: {str(e)}\n\n(Make sure Ollama is running locally if you chose this option.)"

def query_huggingface(prompt):
    try:
        api_key = os.getenv("HUGGINGFACE_API_KEY")
        if not api_key: return "Error: HUGGINGFACE_API_KEY is not set."
        headers = {"Authorization": f"Bearer {api_key}"}
        url = "https://api-inference.huggingface.co/models/google/flan-t5-large"
        response = requests.post(url, headers=headers, json={"inputs": prompt})
        response.raise_for_status()
        return response.json()[0].get("generated_text", "")
    except Exception as e:
        return f"Error: {str(e)}"

def query_gemini(prompt):
    try:
        if not os.getenv("GOOGLE_API_KEY"): return "Error: GOOGLE_API_KEY is not set."
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def query_cohere(prompt):
    try:
        if not os.getenv("COHERE_API_KEY"): return "Error: COHERE_API_KEY is not set."
        co = cohere.ClientV2(api_key=os.getenv("COHERE_API_KEY"))
        response = co.chat(
            model="command-r-plus",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.message.content[0].text
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    st.set_page_config(page_title="Multi-API GenAI Query", page_icon="🤖", layout="centered")
    
    st.title("🤖 Multi-API Generative AI App")
    st.markdown("Test multiple Generative AI providers in one unified web interface. Select your provider, enter a prompt, and see the results!")

    providers = {
        "OpenAI": query_openai,
        "Groq": query_groq,
        "Google Gemini": query_gemini,
        "Cohere": query_cohere,
        "Hugging Face": query_huggingface,
        "Ollama (Local)": query_ollama,
    }

    st.sidebar.title("Configuration")
    selected_provider = st.sidebar.selectbox("Select AI Provider", list(providers.keys()))
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    **Streamlit Hosting Notice:**
    When deploying to Streamlit Community Cloud:
    1. Go to App settings > **Secrets**
    2. Add all your API keys exactly like your `.env` file there!
    """)

    prompt = st.text_area("Enter your prompt for the AI:", height=150, placeholder="Explain generative AI to a 5-year-old...")

    if st.button("Generate Response", type="primary"):
        if not prompt.strip():
            st.warning("Please enter a prompt before querying.")
        else:
            with st.spinner(f"Querying {selected_provider}..."):
                provider_func = providers[selected_provider]
                result = provider_func(prompt)
                
            st.success("Query Complete!")
            st.markdown("### Response From " + selected_provider)
            st.info(result)

if __name__ == "__main__":
    main()
