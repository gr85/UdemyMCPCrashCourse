import asyncio

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(".env"))

from langchain.agents import create_agent
from langchain_anthropic import ChatAnthropic
from langchain_mcp_adapters.client import MultiServerMCPClient

llm = ChatAnthropic(model="claude-haiku-4-5", temperature=0)


async def main():
    print("Hello langchain mcp")

if __name__ == "__main__":
    asyncio.run(main())