from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

from google.adk.tools.mcp_tool import McpToolset, StreamableHTTPConnectionParams

tools = McpToolset(
    connection_params=StreamableHTTPConnectionParams(
        url="http://127.0.0.1:8001/mcp",
    )
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
