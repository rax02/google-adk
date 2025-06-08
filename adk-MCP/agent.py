import os # Required for path operations
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from .mcp_toolsets.system_file_tool import system_file_tool
from .mcp_toolsets.playwrite_tool import playwrite_tool

root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='mcp_agent',
    instruction='Help the user manage their files. You can list files, read files, etc. And you can also use Playwright to interact with web pages.',
    tools=[playwrite_tool,system_file_tool],
)