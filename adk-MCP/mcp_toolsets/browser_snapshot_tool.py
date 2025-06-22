import os # Required for path operations
from google.adk.tools.mcp_tool.mcp_toolset import StdioServerParameters
# from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
# After (with custom timeout patch)  
from .utils.custom_adk_patches import CustomMCPToolset as MCPToolset

# Create a unique context directory
context_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "playwright-isolated-context")

browser_snapshot_tool =  MCPToolset(
            connection_params=StdioServerParameters(
                command='npx',
                args=[
                    "-y",
                    "@playwright/mcp@latest",
                    # "--isolated",
                    # f"--storage-state={context_dir}"
                ],
                
            ),
            tool_filter=["browser_snapshot"]
        )