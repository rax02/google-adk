from google.adk.tools.mcp_tool.mcp_toolset import StdioServerParameters, StdioConnectionParams # type: ignore
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset



browser_use_tool =  MCPToolset(
        connection_params=StdioConnectionParams(
            server_params=StdioServerParameters(
                command='uvx',
                args=["browser-use", "--mcp"],
                env={    "GOOGLE_API_KEY": "AIzaSyCMmUFfQ163ezkWJaEjzvaEw2jYfN-VNpY"    }
            ),
            timeout=10,
        )
    )