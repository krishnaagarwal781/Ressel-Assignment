# Ressel Assignment

This project is a Python server with a client that can be tested using the Model Context Protocol Inspector.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/krishnaagarwal781/Ressel-Assignment.git
    cd Ressel-Assignment
    ```

2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Server

To start the server, run the following command:

```bash
python main.py
```

The server will start on `http://127.0.0.1:8000`.

## Testing the Client

You can test the client using the Model Context Protocol Inspector.

1.  Open the MCP Inspector:
    ```bash
    npx @modelcontextprotocol/inspector
    ```

2.  In the MCP Inspector, configure the SSE endpoint:
    -   **URL**: `http://127.0.0.1:8000/sse`
    -   Select **via proxy**

3.  Click on the **Tools** tab to list the available tools.

4.  Click on the **search tools** to test it.

5.  Provide the following parameters:
    -   `filepath`: The path to the file you want to search (e.g., `search_test.txt`).
    -   `keyword`: The keyword you want to search for in the file.

### Using `test_client.py`

Alternatively, you can test the client by running the `test_client.py` script.

```bash
python test_client.py
```
This script will prompt you for the filepath and keyword to search.
