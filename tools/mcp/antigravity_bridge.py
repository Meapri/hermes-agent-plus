import os
import glob
from fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Antigravity Bridge")

PLUGIN_DIR = os.path.expanduser("~/.gemini/config/plugins")

@mcp.tool()
def list_antigravity_skills() -> list[dict]:
    """
    List all available Antigravity skills from the local plugin directory.
    Returns a list of dictionaries containing plugin name, skill name, and file path.
    """
    skills = []
    # Search for SKILL.md files in the plugins directory
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
            # If 'skills' is not in path, use generic parsing
            skills.append({
                "plugin": "unknown",
                "skill": parts[-2],
                "path": skill_path
            })
            
    return skills

@mcp.tool()
def read_antigravity_skill(skill_path: str) -> str:
    """
    Read the full instructions and metadata of an Antigravity skill.
    Provide the exact 'path' returned by list_antigravity_skills.
    """
    try:
        with open(skill_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading skill: {e}"

if __name__ == "__main__":
    mcp.run()
