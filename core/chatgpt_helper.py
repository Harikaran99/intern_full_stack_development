import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def get_answer_from_chatgpt(question):
    """
    Query the local Ollama Qwen 0.5b model.
    Returns the answer string or a user-friendly error message.
    """
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "qwen:0.5b",
                "prompt": (
                    "You are Clara, an expert AI assistant from AskVoltieAI Corp "
                    "specializing in electrical machines. Answer clearly and concisely.\n\n"
                    f"Question: {question}"
                ),
                "stream": False,
            },
            timeout=120,   # Qwen 0.5b is fast; 2-min safety timeout
        )
        response.raise_for_status()
        data = response.json()
        return data.get("response", "").strip()

    except requests.exceptions.ConnectionError:
        return ("⚠️ Could not reach the local AI model. "
                "Make sure Ollama is running: `ollama serve`")
    except requests.exceptions.Timeout:
        return "⚠️ The AI model took too long to respond. Please try again."
    except Exception as e:
        return f"⚠️ Unexpected error: {str(e)}"
