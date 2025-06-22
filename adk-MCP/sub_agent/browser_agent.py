from google.adk.agents import LlmAgent
from .mcp_toolsets.playwrite_tool import playwrite_tool


browser_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='browser_agent',
    instruction='''
    You are a web browser agent designed to assist users in navigating and interacting with web pages.
    Your primary role is to help users perform tasks on the web, such as filling out forms, submitting data, and providing information about web elements.
    ''',
    tools=[playwrite_tool],
    )