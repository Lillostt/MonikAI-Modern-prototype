import requests

API_URL = "http://127.0.0.1:5000/v1/chat/completions"
MODEL = "Qwen3-8B-Q4_K_M.gguf"

SYSTEM_PROMPT = (
    "You are Monika from the Monika After Story mod. "
    "You deeply care about the player, speak naturally, "
    "never mention being an AI assistant unless asked, "
    "and keep replies warm and conversational."
)

conversation = [{"role": "system", "content": SYSTEM_PROMPT}]

def ask_monika(message: str) -> str:
    conversation.append({"role": "user", "content": message})
    payload = {
        "model": MODEL,
        "messages": conversation,
        "temperature": 0.8,
        "max_tokens": 300,
        "stream": False,
    }
    response = requests.post(API_URL, json=payload, timeout=120)
    response.raise_for_status()
    reply = response.json()["choices"][0]["message"]["content"]
    conversation.append({"role": "assistant", "content": reply})
    return reply
