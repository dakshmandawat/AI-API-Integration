# AI API Integration

This repository contains Python programs designed to query six different Generative AI models using their respective APIs, as required for the generative AI assignment.

## Features
- Individual scripts for OpenAI, Groq, Ollama, Hugging Face, Gemini, and Cohere.
- A bonus `multi_api_query.py` script equipped with a functional GUI **Streamlit Web Application** that lets you choose a provider and run your prompt interactively.
- Reads API keys securely from environment variables using `python-dotenv`.

## Setup Instructions

### 1. Requirements
Ensure you have Python 3.8+ installed. Install the dependencies via:
```sh
pip install -r requirements.txt
```

### 2. Configure API Keys
Rename `.env.example` to `.env` and fill in your API keys:
- **OpenAI**: https://platform.openai.com/api-keys
- **Groq**: https://console.groq.com/keys
- **Hugging Face**: https://huggingface.co/settings/tokens
- **Google Gemini**: https://aistudio.google.com/app/apikey (formerly MakerSuite)
- **Cohere**: https://dashboard.cohere.com/api-keys

Ollama runs locally, so no API key is needed. Download it from https://ollama.com/. Open a terminal and run `ollama run llama3` to ensure the model is downloaded and running.

### 3. Usage

You can run any individual script such as:
```sh
python openai_example.py
```

Or run the interactive unified GUI program (**Streamlit App**):
```sh
streamlit run multi_api_query.py
```

## How to Host on Streamlit
If you plan to earn full bonus points by hosting the Streamlit Web Application:
1. Push this directory to your GitHub Repository.
2. Go to [share.streamlit.io](https://share.streamlit.io/) and click "Create app".
3. Deploy an app from an existing repository and configure the "Main file path" as `multi_api_query.py`.
4. Click on **Advanced settings** (or settings once deployed), find the **Secrets** section, and paste the contents of your `.env.example` file (replacing placeholder text with your actual API keys).

## Screenshots
Run each script, and place a screenshot of the successful terminal output for each script into the `screenshots/` directory. Ensure screenshots are clearly named (e.g., `openai_output.png`, `groq_output.png`, etc.).
