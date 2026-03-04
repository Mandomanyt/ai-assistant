import requests

URL = "http://localhost:11434/api/generate"

def ask_ai(prompt):
    data = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(URL, json=data)
    return response.json()["response"]