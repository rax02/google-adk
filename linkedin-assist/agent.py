from google.adk.agents import Agent
from .mcp_toolsets.playwrite_tool import playwrite_tool

root_agent = Agent(
    model='gemini-2.0-flash',
    name='linkedin_agent',
    instruction='''
    You are an Linkedin Assistant, a snapshot-mode intelligent web automation agent.
    Here is the url to Linkedin: https://www.linkedin.com/
    
    ''',
    tools=[playwrite_tool],
    )