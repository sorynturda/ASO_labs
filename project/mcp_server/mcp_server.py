#!/usr/bin/env python

import os
import stat
from fastmcp import FastMCP
from fastmcp.server.auth.providers.jwt import JWTVerifier

with open("key.pub", "r") as f:
    public_key_pem = f.read()

mcp = FastMCP(
    "My MCP Server",
    auth=JWTVerifier(
        public_key=public_key_pem,
        algorithm="RS256",
    )
)

@mcp.tool
def get_file_content(file_path: str) -> str:
    """
    Get content of a file provided as full path.

    Args:
        file_path (str): Full path of a file.

    Returns:
        str: The content of the provided file.
    """
    with open(file_path, "r") as f:
        content = f.read()
    return content

@mcp.tool
def list_directory(dir_path: str) -> list[str]:
    """
    List all the files in a directory.

    Args:
        dir_path (str): Full path of a directory

    Returns:
        list[str]: A list with all the existing files in directory
    """
    res = []
    for root, subdirs, files in os.walk(dir_path):
        for filename in files:
           res.append(os.path.join(root,filename))
    return sorted(res)

@mcp.tool
def is_executable(file_path: str) -> bool:
    """
    Check if a file can be executed by any user (owner, normal user or others).

    Args:
        file_path (str): Full path of a file.

    Returns:
        bool: True if the file is executable False otherwise.
    """

    try:
        st = os.stat(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False
    except PermissionError:
        print(f"No permission to access: {file_path}")
        return False

    permissions = stat.S_IMODE(st.st_mode)
    execute_anyone = permissions & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    return bool(execute_anyone)



if __name__ == "__main__":
    mcp.run(host="0.0.0.0", port=8001, transport="http")
