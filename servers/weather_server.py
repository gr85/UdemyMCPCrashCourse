from mcp.server.fastmcp import FastMCP
from typing import List

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather for location."""
    return "It's always hot as hell"

if __name__ == "__main__":
    mcp.run(transport="sse")