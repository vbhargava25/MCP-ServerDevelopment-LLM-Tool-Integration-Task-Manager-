MCP Task Manager (Python)
📌 Overview

This project is a Model Context Protocol (MCP) Server built in Python that exposes a simple Task Management system to any MCP-compatible AI client.

The goal of this project is to demonstrate how to:

Expose local functionality to LLMs in a structured way
Enable AI systems to interact with real data and actions
Build modular AI infrastructure using MCP
🚀 Why This Project?

Large Language Models (LLMs) are powerful but cannot directly access local systems, databases, or APIs.

To solve this:

MCP acts as a standard interface layer
Instead of writing custom integrations for each AI tool, we build one MCP server
Any MCP-compatible client (like Claude Desktop, Cursor, or custom agents) can use it

👉 This project simulates a real-world AI assistant that can:

Add tasks
Track pending work
Help organize workflows
🏗️ Architecture
🔹 Components
MCP Host
The application the user interacts with (e.g., Claude Desktop)
MCP Client
Lives inside the host
Converts LLM requests into structured tool calls
MCP Server (This Project)
Exposes tools and data
Handles execution of logic
🔄 Flow
User gives instruction → “Add a task”
LLM interprets intent
MCP Client converts it → tool call
MCP Server executes function
Response is returned → shown to user
🧩 Features Implemented
✅ Tools (Core of MCP)
1. add_task
Adds a new task to the system
Inputs:
title (required)
description (optional)
Output:
Confirmation message
2. get_pending_tasks
Retrieves all tasks with status = pending
Output:
Formatted list of tasks
⚙️ Tech Stack
Component	Tool	Why Used
MCP Framework	FastMCP	Simplifies JSON-RPC + tool exposure
Language	Python	Rapid development + strong ecosystem
Transport	STDIO	Avoids network overhead, ideal for local agents
Storage	In-memory list	Simplicity for prototype
🧠 Why These Design Choices?
1. FastMCP
Handles:
Tool registration
Schema generation
Communication layer
Avoids writing low-level protocol code

👉 Without this, you'd manually handle:

JSON-RPC parsing
Tool metadata
Request routing
2. In-Memory Storage
Chosen for simplicity and demonstration
No external dependencies

👉 Trade-off:

Data is lost when server stops

👉 Real-world alternative:

SQLite / PostgreSQL
3. Docstrings for Tools
LLM reads docstrings to understand:
What the function does
When to use it

👉 Poor docstrings = wrong tool usage

4. STDIO Transport
Communication via input/output streams
No HTTP server required

👉 Benefits:

No port conflicts
No firewall issues
Works seamlessly with local AI tools
