import os
from dotenv import load_dotenv
from datetime import datetime
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool import (
    MCPToolset,
    StreamableHTTPConnectionParams,
)
load_dotenv()

date = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
PATH_TO_FILE = "path/"

MCP_SERVER_URL = "http://localhost:8080/mcp"

root_agent = LlmAgent(
    model="gemini-2.5-flash-preview-05-20",
    name="updater_agent",
    description="Updater Agent",
    instruction=f"""
    You are an agent that leverages GitHub MCP Server to update readme file with the current date and later adds,
    commits and pushes the changes to the main branch.

    current date = {date}

    file to upload = {PATH_TO_FILE}

    """,
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPConnectionParams(
                url="https://api.githubcopilot.com/mcp/",
                headers={
                    "Authorization": "Bearer " + os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN"),
                },
            ),
        ),
    ],
)
