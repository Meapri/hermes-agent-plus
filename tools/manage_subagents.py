import json
import logging
from tools.registry import register
from agent.async_subagents import list_jobs, kill_job

logger = logging.getLogger(__name__)

MANAGE_SUBAGENTS_SCHEMA = {
    "name": "manage_subagents",
    "description": "Manage background asynchronous subagents spawned by spawn_subagent.",
    "parameters": {
        "type": "object",
        "properties": {
            "action": {
                "type": "string",
                "enum": ["list", "kill"],
                "description": "The action to perform."
            },
            "job_id": {
                "type": "string",
                "description": "The job ID to kill. Required if action is 'kill'."
            }
        },
        "required": ["action"]
    }
}

def manage_subagents(action: str, job_id: str = None, **kwargs):
    if action == "list":
        jobs = list_jobs()
        return json.dumps({"jobs": jobs})
    elif action == "kill":
        if not job_id:
            return json.dumps({"error": "job_id is required for kill action."})
        success = kill_job(job_id)
        return json.dumps({"status": "killed" if success else "job_id not found"})
    else:
        return json.dumps({"error": f"Unknown action: {action}"})

register(MANAGE_SUBAGENTS_SCHEMA, manage_subagents)
