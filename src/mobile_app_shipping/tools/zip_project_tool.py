from crewai.tools import tool
import zipfile
import os

@tool("zip_project")
def zip_project(project_dir: str, output_zip: str = "mobile_app_project.zip") -> str:
    """
    Compress a project directory into a zip file and return a message with paths.

    Args:
        project_dir (str): Path to the directory to compress.
        output_zip (str): Name or path of the resulting zip file.
    Returns:
        str: Confirmation message with absolute paths.
    """
    if not os.path.exists(project_dir):
        return f"❌ Directory '{project_dir}' not found."

    try:
        with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(project_dir):
                for file in files:
                    filepath = os.path.join(root, file)
                    arcname = os.path.relpath(filepath, project_dir)
                    zipf.write(filepath, arcname)

        abs_project = os.path.abspath(project_dir)
        abs_zip = os.path.abspath(output_zip)
        return (
            f"✅ Project zipped successfully.\n"
            f"📂 Project folder: {abs_project}\n"
            f"📦 Zip file: {abs_zip}"
        )
    except Exception as e:
        return f"❌ Failed to zip project: {str(e)}"
