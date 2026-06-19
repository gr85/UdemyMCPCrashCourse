import asyncio

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(".env"))

from langchain.agents import create_agent
from langchain_anthropic import ChatAnthropic
from langchain_mcp_adapters.tools import load_mcp_tools
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


llm = ChatAnthropic(model="claude-haiku-4-5", temperature=0)

stdio_server_params = StdioServerParameters(
    command="python",
    args=["D:/Udemy/LangChain_Agentic_AI/UdemyMCPCrashCourse/servers/math_server.py"]
)


async def main():
    print("Hello from udemymcpcrashcourse!")


if __name__ == "__main__":
    asyncio.run(main())
