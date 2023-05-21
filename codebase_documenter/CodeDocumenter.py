import openai
import os
from datetime import datetime
from .default_ai_prompt import default_ai_prompt


class CodebaseDocumenter:
    def __init__(self, openai_api_key, root_path, ignore_folders=["venv"], file_types=[".py"]):
        self.openai_api_key = openai_api_key
        self.root_path = root_path
        self.ignore_folders = ignore_folders
        self.file_types = file_types
        self.base_dir = root_path
        self.docs_dir = os.path.join(self.base_dir, "docs")

        openai.api_key = self.openai_api_key

        # Create the docs folder if it doesn't exist
        if not os.path.exists(self.docs_dir):
            os.makedirs(self.docs_dir)

        # Load the ai_prompt_text from a text file
        try:
            with open(os.path.join(self.base_dir, "ai_prompt_override.py"), "r") as file:
                self.ai_prompt_text = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print("Warning: 'ai_prompt_override.py' file not found. Using default prompt.")
            self.ai_prompt_text = default_ai_prompt
        except Exception as e:
            print(f"Warning: Error reading 'ai_prompt_override.py'. Using default prompt. Error: {str(e)}")
            self.ai_prompt_text = default_ai_prompt

    def _get_completion(self, prompt, model="gpt-3.5-turbo"):
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0,  # this is the degree of randomness of the model's output
        )
        return response.choices[0].message["content"]

    def _get_file_paths(self):
        file_paths = []
        for dirpath, dirnames, filenames in os.walk(self.root_path):
            for ignore_folder in self.ignore_folders:
                if ignore_folder in dirnames:
                    dirnames.remove(ignore_folder)
            file_paths.extend(
                [
                    os.path.join(dirpath, filename)
                    for filename in filenames
                    if any(filename.endswith(file_type) for file_type in self.file_types)
                ]
            )
        return file_paths

    def _process_file(self, file_path):
        with open(file_path, "r") as file:
            prompt = file.read()

            if not prompt.strip():
                return False, "Skipping empty file"

            prompt = f"""{'. '.join(self.ai_prompt_text)}.

            Please assess the following file:

            {prompt}
            """

            # Get the relative path of the file
            relative_path = os.path.relpath(file_path, self.base_dir)

            # Create the directory structure in the docs folder
            output_dir = os.path.dirname(os.path.join(self.docs_dir, relative_path))
            os.makedirs(output_dir, exist_ok=True)

            # Define the output file path
            file_name = os.path.basename(file_path)
            output_file = os.path.join(output_dir, f"{file_name}.md")

            # Check if the file already exists
            if os.path.exists(output_file):
                print(f"WARNING: Documentation file {output_file} already exists and will be overwritten.")

            with open(output_file, "w") as output:
                # Add timestamp at the top of the file
                print("# Auto generated documentation file\n", file=output)
                timestamp = datetime.now().strftime("%d %B %Y at %H:%M:%S")
                print(f"This documentation file was created on {timestamp}\n", file=output)

                print("## File path\n", file=output)
                print(file_path, file=output)
                response = self._get_completion(prompt)
                print(response, file=output)

                print(f"Wrote documentation file {output_file}")

            return True, "Processed file successfully"

    def process_all_files(self):
        file_paths = self._get_file_paths()
        total_files = len(file_paths)
        for i, file_path in enumerate(file_paths):
            print(f"Processing file {i+1}/{total_files}: {file_path}")
            success, message = self._process_file(file_path)
            if not success:
                print(f"{message} {i+1}/{total_files}: {file_path}")

    def process_single_file(self, file_path):
        success, message = self._process_file(file_path)
        if not success:
            print(f"{message}: {file_path}")
