from fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP(name="File Keyword Search Server")


@mcp.tool
def search_in_file(filepath: str, keyword: str) -> str:
    """
    Searches for a specified keyword within a file.
    Returns the line numbers and corresponding lines containing the keyword.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Find all lines that contain the keyword (case-insensitive)
        matches = [
            f"Line {i + 1}: {line.strip()}"
            for i, line in enumerate(lines)
            if keyword.lower() in line.lower()
        ]

        if not matches:
            return f"Keyword '{keyword}' not found in '{filepath}'."

        result = "\n".join(matches)
        return f"✅ Found {len(matches)} occurrence(s) of '{keyword}' in '{filepath}':\n{result}"

    except FileNotFoundError:
        return f"❌ Error: File not found at '{filepath}'."
    except Exception as e:
        return f"⚠️ An error occurred: {str(e)}"


if __name__ == "__main__":
    print("🚀 Starting File Keyword Search Server on http://localhost:8000 ...")
    mcp.run(transport="sse", host="0.0.0.0", port=8000)
