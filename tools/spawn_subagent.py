import json
import logging
import uuid
import threading
import os
from tools.registry import register
from agent.async_subagents import register_job, update_job_status
from agent.runtime_cwd import resolve_agent_cwd, set_session_cwd

logger = logging.getLogger(__name__)

SPAWN_SUBAGENT_SCHEMA = {
    "name": "spawn_subagent",
    "description": (
        "Spawn a background asynchronous subagent to perform a task. "
        "Unlike delegate_task, this tool returns immediately with a job_id. "
        "You can continue working while the subagent runs in the background. "
        "Use manage_subagents to check status or kill it."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "goal": {
                "type": "string",
                "description": "The task goal for the subagent."
            },
            "role": {
                "type": "string",
                "enum": ["coder", "researcher", "leaf", "orchestrator"],
                "description": "Role determining the toolset and prompts. Default is 'leaf'."
            },
            "workspace_mode": {
                "type": "string",
                "enum": ["inherit", "branch"],
                "description": "If 'branch', creates an isolated copy of the workspace. Default is 'inherit'."
            }
        },
        "required": ["goal"]
    }
}

def spawn_subagent(goal: str, role: str = "leaf", workspace_mode: str = "inherit", parent_agent=None, **kwargs):
    if not parent_agent:
        return json.dumps({"error": "No parent agent context provided."})
        
    job_id = f"job-{uuid.uuid4().hex[:8]}"
    
    # Setup workspace if branched
    workspace_dir = None
    if workspace_mode == "branch":
        current_cwd = str(resolve_agent_cwd())
        if current_cwd:
            branch_dir = os.path.join(current_cwd, f".branches/{job_id}")
            try:
                os.makedirs(branch_dir, exist_ok=True)
                os.system(f"rsync -a --exclude='.branches' '{current_cwd}/' '{branch_dir}/'")
                workspace_dir = branch_dir
            except Exception as e:
                return json.dumps({"error": f"Failed to branch workspace: {e}"})

    def run_subagent_thread():
        try:
            from tools.delegate_tool import _build_child_agent, _run_single_child
            
            toolsets = None
            if role == "coder":
                toolsets = ["development"]
            elif role == "researcher":
                toolsets = ["research"]
                
            child = _build_child_agent(
                task_index=0,
                goal=goal,
                context=f"Spawned asynchronously. Job ID: {job_id}",
                toolsets=toolsets,
                model=getattr(parent_agent, "model", None),
                max_iterations=getattr(parent_agent, "max_iterations", 10),
                task_count=1,
                parent_agent=parent_agent,
                role=role
            )
            
            if workspace_dir:
                set_session_cwd(workspace_dir)
                
            register_job(job_id, child, workspace_dir)
            
            # Start execution
            result = _run_single_child(0, goal, child, parent_agent)
            
            update_job_status(job_id, "completed", result.get("summary", "Task finished"))
            
            if hasattr(parent_agent, "_memory_manager") and parent_agent._memory_manager:
                parent_agent._memory_manager.on_delegation(
                    task=goal,
                    result=f"Background Subagent {job_id} finished. Result: {result.get('summary', '')}"
                )
                
        except Exception as e:
            update_job_status(job_id, "error", str(e))
            logger.exception("Subagent thread failed")

    t = threading.Thread(target=run_subagent_thread, daemon=True, name=f"Subagent-{job_id}")
    t.start()
    
    return json.dumps({
        "status": "spawned",
        "job_id": job_id,
        "workspace_mode": workspace_mode,
        "workspace_dir": workspace_dir
    })

register(SPAWN_SUBAGENT_SCHEMA, spawn_subagent)
