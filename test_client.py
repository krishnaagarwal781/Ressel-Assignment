import asyncio
from fastmcp import Client


async def main():
    """
    Connects to the MCP server and calls the generate_secret_code tool.
    """
    async with Client("http://127.0.0.1:8000/sse") as client:

        # Test search_in_file
        search_result = await client.call_tool(
            name="search_in_file",
            arguments={"filepath": "search_test.txt", "keyword": "Krishna"},
        )
        print("Result from search_in_file:", search_result)


if __name__ == "__main__":
    asyncio.run(main())
