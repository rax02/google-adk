import os # Required for path operations
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

playwrite_tool =  MCPToolset(
            connection_params=StdioServerParameters(
                command='npx',
                args=[
                    "@playwright/mcp@latest",
                ]
            )
        )