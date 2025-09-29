import os
from groq import Groq
from ollama import Client

def invoke_llm(prompt: str, provider: str = "groq", model: str = "llama3-70b-8192"):
    """
    A unified function to invoke an LLM, abstracting the client details.
    :param provider: "groq" or "ollama"
    """
    if provider == "groq":
        try:
            client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model=model,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            print(f"Error calling Groq: {e}")
            return "Error: Could not get response from Groq."

    elif provider == "ollama":
        try:
            client = Client(host=os.environ.get("OLLAMA_HOST"))
            response = client.chat(
                model=model,
                messages=[{"role": "user", "content": prompt}]
            )
            return response['message']['content']
        except Exception as e:
            print(f"Error calling Ollama: {e}")
            return "Error: Could not get response from Ollama."

    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")