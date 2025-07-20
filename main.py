import os

from google.adk.runners import Runner
import asyncio
from dotenv import load_dotenv
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.adk.agents.run_config import RunConfig
from google.genai import types # For creating message Content/Parts

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "auto-updater")
AGENT = root_agent
QUERY = "Update the file update.py with todays date as comment at the end of the file. Then add, commit and push the changes to GitHub"

async def run_agent(session_id: str):
    """This function simulates a non-streaming audio call with the agent."""    
    session_service = InMemorySessionService()
    session = session_service.create_session(
        app_name=APP_NAME,
        user_id=session_id,
        session_id=session_id,
    )

    runner = Runner(
        app_name=APP_NAME,
        agent=AGENT,
        session_service=session_service,
    )

  content = types.Content(role='user', parts=[types.Part(text=QUERY)])
  
  async for event in runner.run_async(user_id=session_id, session_id=session_id, new_message=user_content, run_config=run_config):
        if event.is_final_response():
            if event.content and event.content.parts:
                final_response_text = event.content.parts[0].text
            elif event.actions and event.actions.escalate: 
                final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
            break 
    print(f"<<< Agent Response: {final_response_text}")

if __name__ == "__main__":
    print("Hello from auto-updater!")
    asyncio.run(run_agent("basic_session"))
