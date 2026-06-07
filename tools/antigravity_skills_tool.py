import os
import glob
from tools.registry import registry, tool_error, tool_result

PLUGIN_DIR = os.path.expanduser("~/.gemini/config/plugins")

def antigravity_skills_tool(args, **kwargs):
    action = args.get("action")
    if action == "list":
        return _list_antigravity_skills()
    elif action == "read":
        path = args.get("skill_path")
        if not path:
            return tool_error("skill_path is required for read action")
        return _read_antigravity_skill(path)
    else:
        return tool_error(f"Unknown action: {action}")

def _list_antigravity_skills():
    skills = []
    for skill_path in glob.glob(f"{PLUGIN_DIR}/**/*.md", recursive=True):
        if not skill_path.endswith("SKILL.md"):
            continue
            
        parts = skill_path.split(os.sep)
        try:
            skills_idx = parts.index("skills")
            plugin_name = parts[skills_idx - 1]
            skill_name = parts[skills_idx + 1]
            
            skills.append({
                "plugin": plugin_name,
                "skill": skill_name,
                "path": skill_path
            })
        except ValueError:
            skills.append({
                "plugin": "unknown",
                "skill": parts[-2],
                "path": skill_path
            })
            
    return tool_result(skills=skills)

def _read_antigravity_skill(skill_path: str):
    try:
        with open(skill_path, "r", encoding="utf-8") as f:
            return tool_result(content=f.read())
    except Exception as e:
        return tool_error(f"Error reading skill: {e}")

ANTIGRAVITY_SKILLS_SCHEMA = {
    "name": "antigravity_skills",
    "description": "List and read Antigravity skills from the local plugin directory. Useful for retrieving skill capabilities.",
    "parameters": {
        "type": "object",
        "properties": {
            "action": {
                "type": "string",
                "enum": ["list", "read"],
                "description": "Action to perform: 'list' to see all skills, 'read' to read a specific skill."
            },
            "skill_path": {
                "type": "string",
                "description": "The exact path of the skill to read (required if action is 'read')."
            }
        },
        "required": ["action"]
    }
}

registry.register(
    name="antigravity_skills",
    toolset="antigravity",
    schema=ANTIGRAVITY_SKILLS_SCHEMA,
    handler=antigravity_skills_tool,
    emoji="🚀"
)
