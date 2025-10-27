from crewai.tools import tool
import os

@tool("write_file")
def write_file(filename: str, content: str) -> str:
    """
    Create a file with the given name and content.

    Args:
        filename (str): Path of the file to create.
        content (str): Content to write into the file.
    Returns:
        str: A success message including the file path.
    """
    try:
        os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        return f"✅ File '{filename}' created successfully."
    except Exception as e:
        return f"❌ Failed to create file '{filename}': {str(e)}"
