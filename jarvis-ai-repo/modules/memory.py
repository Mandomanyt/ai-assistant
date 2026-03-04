import json, os

FILE = "data/memory.json"

def load():
    if not os.path.exists(FILE):
        return {}
    with open(FILE) as f:
        return json.load(f)

def save(key, value):
    data = load()
    data[key] = value
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)