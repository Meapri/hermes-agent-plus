import threading
import logging
import uuid
import time
import json
import traceback

logger = logging.getLogger(__name__)

# Global registry of background subagents
# { "job_id": {"status": "running"|"completed"|"error", "summary": "", "thread": Thread, "agent": AIAgent, "workspace_dir": str} }
_BACKGROUND_JOBS = {}
_JOBS_LOCK = threading.Lock()

def register_job(job_id, agent_instance, workspace_dir=None):
    with _JOBS_LOCK:
        _BACKGROUND_JOBS[job_id] = {
            "status": "running",
            "summary": None,
            "agent": agent_instance,
            "workspace_dir": workspace_dir,
            "start_time": time.time(),
        }

def update_job_status(job_id, status, summary):
    with _JOBS_LOCK:
        if job_id in _BACKGROUND_JOBS:
            _BACKGROUND_JOBS[job_id]["status"] = status
            _BACKGROUND_JOBS[job_id]["summary"] = summary

def get_job(job_id):
    with _JOBS_LOCK:
        return _BACKGROUND_JOBS.get(job_id)

def list_jobs():
    with _JOBS_LOCK:
        return {
            jid: {
                "status": data["status"],
                "start_time": data["start_time"],
                "workspace_dir": data["workspace_dir"]
            }
            for jid, data in _BACKGROUND_JOBS.items()
        }

def kill_job(job_id):
    with _JOBS_LOCK:
        if job_id in _BACKGROUND_JOBS:
            agent = _BACKGROUND_JOBS[job_id].get("agent")
            if agent:
                agent._interrupt_requested = True
            _BACKGROUND_JOBS[job_id]["status"] = "killed"
            return True
        return False
