import json
import logging
import threading
from tools.registry import register

logger = logging.getLogger(__name__)

# Global in-memory store for the current session
_TEAM_MEMORY = {}
_MEMORY_LOCK = threading.Lock()

STORE_TEAM_MEMORY_SCHEMA = {
    "name": "store_team_memory",
    "description": "Store a piece of information in the shared team memory pool. All subagents can access this data.",
    "parameters": {
        "type": "object",
        "properties": {
            "key": {
                "type": "string",
                "description": "A unique key for the information."
            },
            "value": {
                "type": "string",
                "description": "The information to store (can be stringified JSON)."
            }
        },
        "required": ["key", "value"]
    }
}

RETRIEVE_TEAM_MEMORY_SCHEMA = {
    "name": "retrieve_team_memory",
    "description": "Retrieve information from the shared team memory pool.",
    "parameters": {
        "type": "object",
        "properties": {
            "key": {
                "type": "string",
                "description": "The unique key to look up. If omitted, returns all keys.",
            }
        }
    }
}

def store_team_memory(key: str, value: str, **kwargs) -> str:
    with _MEMORY_LOCK:
        _TEAM_MEMORY[key] = value
    return json.dumps({"status": "success", "message": f"Stored under key: {key}"})

def retrieve_team_memory(key: str = None, **kwargs) -> str:
    with _MEMORY_LOCK:
        if key:
            value = _TEAM_MEMORY.get(key)
            if value is None:
                return json.dumps({"error": f"Key '{key}' not found in team memory."})
            return json.dumps({"key": key, "value": value})
        else:
            return json.dumps({"keys": list(_TEAM_MEMORY.keys())})

register("store_team_memory", "delegation", STORE_TEAM_MEMORY_SCHEMA, store_team_memory)
register("retrieve_team_memory", "delegation", RETRIEVE_TEAM_MEMORY_SCHEMA, retrieve_team_memory)
