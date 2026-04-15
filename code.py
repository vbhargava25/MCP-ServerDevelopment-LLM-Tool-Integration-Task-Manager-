# Required import
from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("LocalTaskManager")

# In-memory storage (acts like a simple database)
tasks = []
current_id = 1

# Tool 1: Add a task
@mcp.tool()
def add_task(title: str, description: str = "") -> str:
    """
    Add a new task to the user's task list.
    """
    global current_id

    tasks.append({
        "id": current_id,
        "title": title,
        "description": description,
        "status": "pending"
    })

    current_id += 1
    return f"Success! Task '{title}' was added to the tracker."


# Tool 2: Get pending tasks
@mcp.tool()
def get_pending_tasks() -> str:
    """
    Retrieve all pending tasks so the user knows what to do next.
    """
    pending = [t for t in tasks if t["status"] == "pending"]

    if not pending:
        return "You're all caught up! No pending tasks right now."

    output = "Here are your pending tasks:\n"
    for t in pending:
        output += f"- [ID: {t['id']}] {t['title']} (Details: {t['description']})\n"

    return output


# Run server
if __name__ == "__main__":
    mcp.run(transport="stdio")
