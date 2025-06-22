from google.adk.agents import LlmAgent
from .mcp_toolsets.browser_snapshot_tool import browser_snapshot_tool

browser_snapshot_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='browser_snapshot_agent',
    instruction='''
    You are browser agent. Your primary role is to take snapshot of current page in the browser.
    You can use the browser_snapshot tool to capture the current state of the web page.
    ''',
    tools=[browser_snapshot_tool],
    output_key="browser_snapshot",
    )