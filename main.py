import asyncio

from dotenv import find_dotenv, load_dotenv
from langchain_core.messages import HumanMessage

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
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            # Initialize session
            await session.initialize()
            print("Session initialized")
            # Get the available tools
            tools = await load_mcp_tools(session)
            print(tools)

            agent = create_agent(model=llm, tools=tools)

            result = await agent.ainvoke({"messages": [HumanMessage(content="What is 54 + 2 * 3?")]})
            print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
