import json
from pathlib import Path

_users_cache = None

def load_users():
    global _users_cache
    if _users_cache is not None:
        return _users_cache

    base_dir = Path(__file__).parent.parent
    file_path = base_dir / 'mock-users.json' 

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            _users_cache = json.load(f)
        return _users_cache
    except FileNotFoundError:
        raise RuntimeError("mock-users.json not found. Make sure it's in the project root.")