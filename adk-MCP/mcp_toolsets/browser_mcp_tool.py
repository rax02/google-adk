from google.adk.tools.mcp_tool.mcp_toolset import StdioServerParameters, StdioConnectionParams # type: ignore
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset



browser_mcp_tool =  MCPToolset(
        connection_params=StdioConnectionParams(
            server_params=StdioServerParameters(
                command='npx',
                args=[
                    "@browsermcp/mcp@latest"
                ]
            ),
            timeout=10,
        )
    )