import os # Required for path operations
from google.adk.tools.mcp_tool.mcp_toolset import StdioServerParameters,StdioConnectionParams # type: ignore
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
# After (with custom timeout patch)  
# from .utils.custom_adk_patches import CustomMCPToolset as MCPToolset

# Create a unique context directory
context_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "playwright-isolated-context.json")
# context_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "")

playwrite_tool =   MCPToolset(
        connection_params=StdioConnectionParams(
            server_params=StdioServerParameters(
                command='npx',
                args=[
                    "-y",
                    "@playwright/mcp@latest",
                    # "--isolated",
                    # f"--storage-state={context_dir}",
                    # "--save-trace",

                    # f"--output-dir={context_dir}"
                    # "--browser-agent=localhost:9001"
                    # "--cdp-endpoint=http://localhost:9222",
                ]
            ),
            timeout=10,
        )
    )