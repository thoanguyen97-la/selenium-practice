import json
import os

def load_json(filename):
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(base, "resources", filename)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)