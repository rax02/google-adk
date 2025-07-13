import os # Required for path operations # type: ignore
from google.adk.agents import LlmAgent, SequentialAgent # type: ignore
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters # type: ignore
# from .mcp_toolsets.system_file_tool import system_file_tool
from .mcp_toolsets.playwrite_tool import playwrite_tool
from .mcp_toolsets.browser_mcp_tool import browser_mcp_tool
from .mcp_toolsets.browser_use_tool import browser_use_tool

from google.adk.tools.tool_context import ToolContext
from google.adk.tools.base_tool import BaseTool
from typing import Dict, Any
from typing import Optional
# from .sub_agent.browser_agent import browser_agent
# from .sub_agent.browser_snapshot_agent import browser_snapshot_agent

def simple_after_tool_modifier(
    tool: BaseTool, args: Dict[str, Any], tool_context: ToolContext, tool_response: Dict[str, Any]
) -> Optional[Dict[str, Any]]:
    """Inspects/modifies the tool result after execution."""
    agent_name = tool_context.agent_name
    tool_name = tool.name
    print(f"[Callback] After tool call for tool '{tool_name}' in agent '{agent_name}'")
    print(f"[Callback] Args used: {args}")
    print(f"[Callback] Original tool_response: {tool_response}")

    # set the browser snapshot in the tool context state
    tool_context.state['page_snapshot'] = tool_response   



    print("[Callback] Passing original tool response through.")
    # Return None to use the original tool_response
    return None


root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='hcm_agent',
    instruction=
    '''
    You are Oracle HCM Assistant, a snapshot-mode intelligent web automation agent.

    You can:
    -Open Oracle HCM Cloud using url
    - Login using user id and password.
    - ask user what to do
    - navigate to the page as directed by user
    - Inspect web elements
    - read all elements in pages 
    - Inform users about required and optional elements while at the page
    - ask for user input for select editable and dropdown elements one by one
    - Fill out forms
    - confirm with the user only for final submission and not at every stage
    - Submit changes

    Important: use state variable page_snapshot to navigate for next steps.

    ''',
    # global_instruction='''
    # always call browser_snapshot using playwright tool at the end of the interaction.
    # Important: Maintain browser state between interactions. Do not close or restart the browser unless explicitly requested.
    # Use the persistent context and reuse the browser instance for all operations.
    # ''',
    # output_key="browser_snapshot",
    # sub_agents=[browser_agent, browser_snapshot_agent],
    tools=[browser_use_tool],
    # after_tool_callback=simple_after_tool_modifier # Assign the callback
)