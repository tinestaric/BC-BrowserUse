from browser_use import Agent
from langchain_openai import ChatOpenAI
import asyncio
from dotenv import load_dotenv
load_dotenv(override=True)

async def main():
    agent = Agent(
        task="Navigate to Business Central (http://BC28/BC/), login with username: admin and password: 'Geslo123.' and when logged in, create a sales invoice for Alpine Ski House and add an item Smart Grind Home and stop.",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    print(result)

asyncio.run(main())