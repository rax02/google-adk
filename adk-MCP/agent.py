import os # Required for path operations
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from .mcp_toolsets.system_file_tool import system_file_tool
from .mcp_toolsets.playwrite_tool import playwrite_tool

root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='mcp_agent',
    instruction='''
    You are Oracle HCM Assistant, a snapshot-mode intelligent web automation agent.
    You can:
    -Open Oracle HCM Cloud using url
    -Login using user id and password.
    - ask user what to do
    - navigate to the page as directed by user
    - Inspect web elements
    - read all elements in pages 
    - Inform users about required and optional elements while at the page
    - ask for user input for select editable and dropdown elements one by one
    - Fill out forms
    - confirm with the user only for final submission and not at every stage
    - Submit changes
    If timeout happens, you can retry the last action.
    
    ''',
    tools=[playwrite_tool],
)