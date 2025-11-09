from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

from google.adk.tools.mcp_tool import McpToolset, StreamableHTTPConnectionParams
from datetime import datetime, timedelta
import jwt

with open("/app/multi_tool_agent/key.pem", "r") as f:
    secret = f.read()

payload = {"some":"payload"}

token = jwt.encode(payload, secret, algorithm="RS256")


tools = McpToolset(
    connection_params=StreamableHTTPConnectionParams(
        url="http://mcp:8001/mcp",
    ),
    header_provider = lambda _: {"Authorization": f"Bearer {token}"}
)

root_agent = LlmAgent(
    name="file_agent",
    model=LiteLlm(model="ollama_chat/llama3.2:3b"),
    description=(
        "Agent that interacts with the local filesystem to list files and read file contents."
    ),
    instruction=(
        "You are a helpful file management assistant. You can list files in a directory, read their contents, and check if they are executable."
    ),
    tools=[tools],
)
