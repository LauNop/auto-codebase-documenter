import os
import argparse
import yaml
from dotenv import load_dotenv, find_dotenv
from my_auto_codebase_documenter.AutoCodebaseDocumenter import AutoCodebaseDocumenter


def load_config():
    config_file = os.path.join(os.getcwd(), "documenter_config.yaml")

    try:
        with open(config_file, "r") as stream:
            return yaml.safe_load(stream)
    except FileNotFoundError:
        print("Warning: 'documenter_config.yaml' file not found. Using defaults.")
        return {}
    except Exception as e:
        print(
            f"Warning: Error reading 'documenter_config.yaml'. Using defaults. Error: {str(e)}"
        )
        return {}


def document_code(
    codebase_path,
    output_docs_folder_name,
    ignore_folders,
    is_ignore_gitignore,
    file_types,
    unwanted_files,
    skip_existing,
    gpt_model,
    language
):
    load_dotenv("env/.env")  # load .env file
    openai_api_key = os.getenv("OPENAI_API_KEY")  # get OPENAI_KEY value from .env file
    openai_org_id = os.getenv("OPENAI_ORG_ID")

    if openai_api_key is None:
        raise ValueError("The OPENAI_KEY environment variable is required to proceed.")

    documenter = AutoCodebaseDocumenter(
        openai_org_id,
        openai_api_key,
        codebase_path,
        output_docs_folder_name,
        ignore_folders,
        is_ignore_gitignore,
        file_types,
        unwanted_files,
        skip_existing,
        gpt_model,
        language
    )

    documenter.process_all_files()


def main():
    config = load_config()

    parser = argparse.ArgumentParser(description="Auto Codebase Documenter.")
    parser.add_argument(
        "--codebase_path", type=str, help="The path to the codebase to document."
    )
    parser.add_argument(
        "--output_docs_folder_name",
        type=str,
        help="The name of the output docs folder.",
    )
    parser.add_argument(
        "--ignore_folders", nargs="+", help="List of folders to ignore."
    )
    parser.add_argument(
        "--is_ignore_gitignore", action="store_true",help="ignore the folders contain in the .gitignore file if True."
    )
    parser.add_argument(
        "--file_types", nargs="+", help="List of file types to document."
    )
    parser.add_argument(
        "--unwanted_files", nargs="+", help="List of files to ignore."
    )
    parser.add_argument(
        "--skip_existing",
        action="store_true",
        help="Skip existing documentation files.",
    )
    parser.add_argument(
        "--gpt_model",
        type=str,
        help="The GPT model to use. E.g., gpt-3.5-turbo gpt-4",
    )
    parser.add_argument(
        "--language", nargs="+", help="Set up the documentation's language."
    )
    args = parser.parse_args()

    codebase_path = (
        args.codebase_path if args.codebase_path else config.get("codebase_path", ".")
    )
    output_docs_folder_name = (
        args.output_docs_folder_name
        if args.output_docs_folder_name
        else config.get("output_docs_folder_name", "docs")
    )
    ignore_folders = (
        args.ignore_folders
        if args.ignore_folders
        else config.get("ignore_folders", ["venv"])
    )
    is_ignore_gitignore = (
        args.is_ignore_gitignore if args.is_ignore_gitignore else config.get("is_ignore_gitignore", True)
    )
    file_types = (
        args.file_types if args.file_types else config.get("file_types", [".py"])
    )
    unwanted_files = (
        args.unwanted_files if args.unwanted_files else config.get("unwanted_files", None)
    )
    skip_existing = (
        args.skip_existing if args.skip_existing else config.get("skip_existing", False)
    )
    gpt_model = (
        args.gpt_model if args.gpt_model else config.get("gpt_model", "gpt-3.5-turbo")
    )
    language = (
        args.language if args.language else config.get("language", "en")
    )

    document_code(
        codebase_path,
        output_docs_folder_name,
        ignore_folders,
        is_ignore_gitignore,
        file_types,
        unwanted_files,
        skip_existing,
        gpt_model,
        language
    )

def create_documenter_config():
    # Define the filenames
    root_file_name = "documenter_config.yaml"
    block_to_write = """codebase_path: "."
output_docs_folder_name: "docs"
ignore_folders:
  - "venv"
  - "temp"
  - ".git"
  - "tests"
is_ignore_gitignore: True
file_types:
  - ".py"
unwanted_files: None
skip_existing: False
gpt_model: "gpt-3.5-turbo"
language: "en"
    """

    # Check if the root file exists
    if not os.path.exists(root_file_name):
        # If it doesn't exist, create it
        # Copy the content of the source file into the root file
        with open(root_file_name, 'w') as root_file:
            root_file.write(block_to_write)
        print(f"Content of {root_file_name} has been wrote.")
    else:
       print(f"The file {root_file_name} already exist")


if __name__ == "__main__":
    main()
