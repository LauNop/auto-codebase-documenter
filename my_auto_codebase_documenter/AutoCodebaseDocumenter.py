from datetime import datetime
import os
import openai
from my_auto_codebase_documenter.default_ai_prompt import default_ai_prompt


class AutoCodebaseDocumenter:
    def __init__(
        self,
        openai_org_id,
        openai_api_key,
        root_path=".",
        output_docs_folder_name="docs",
        ignore_folders=["venv",".git","tests"],
        is_ignore_gitignore=True,
        file_types=[".py"],
        unwanted_files=None,
        skip_existing=False,
        gpt_model="gpt-3.5-turbo",
        language='en',
    ):
        self.root_path = root_path
        self.output_docs_folder_name = output_docs_folder_name
        self.ignore_folders = ignore_folders
        self.is_ignore_gitignore = is_ignore_gitignore
        self.file_types = file_types
        self.unwanted_files = unwanted_files
        self.skip_existing = skip_existing
        self.gpt_model = gpt_model

        self.docs_dir = os.path.join(self.root_path, self.output_docs_folder_name)
        if language == 'fr':
            default_ai_prompt.insert(0, 'Write in french')

        self.system_message = '. '.join(default_ai_prompt)

        openai.api_key = openai_api_key
        openai.organization = openai_org_id

        # Create the docs folder if it doesn't exist
        if not os.path.exists(self.docs_dir):
            os.makedirs(self.docs_dir)


    def _get_completion(self, prompt):
        messages = [
            {"role": "system", "content": self.system_message},
            {"role": "user", "content": prompt}
        ]
        response = openai.ChatCompletion.create(
            model=self.gpt_model,
            messages=messages,
            temperature=0,  # this is the degree of randomness of the model's output
        )
        return response.choices[0].message["content"]

    def _get_file_paths(self):
        # Initialize a list to store the file paths
        if self.unwanted_files is None:
            unwanted_file = []
        file_list = []

        # Create a set to store the patterns from .gitignore
        ignore_patterns = set()

        # Check if a .gitignore file exists and add its patterns to the set
        gitignore_path = os.path.join(self.root_path, ".gitignore")
        if os.path.exists(gitignore_path):
            with open(gitignore_path, "r") as gitignore_file:
                for line in gitignore_file:
                    line = line.strip()
                    if line and not line.startswith("#"):  # Ignore comments and empty lines
                        ignore_patterns.add(os.path.basename(line))

        # If additional ignore patterns are provided, add them to the set
        if self.ignore_folders:
            ignore_patterns.update(self.ignore_folders)

        print("Ignore folder:", ignore_patterns)
        # Walk through the root directory and its subdirectories
        count = 0
        for dirpath, dirnames, filenames in os.walk(self.root_path):
            for ignore_pattern in ignore_patterns:
                if ignore_pattern in dirnames:
                    dirnames.remove(ignore_pattern)
            file_list.extend(
                [
                    os.path.join(dirpath, filename)
                    for filename in filenames
                    if any(filename.endswith(file_type) for file_type in [".py"])
                       and filename not in self.unwanted_files
                ]
            )
        return file_list

    def _process_file(self, file_path):
        with open(file_path, "r") as file:
            prompt = file.read()

            if not prompt.strip():
                return False, "Skipping empty file"

            prompt = f"""
            Please assess the following file:

            {prompt}
            """

            # Get the relative path of the file
            relative_path = os.path.relpath(file_path, self.root_path)

            # Create the directory structure in the docs folder
            output_dir = os.path.dirname(os.path.join(self.docs_dir, relative_path))
            os.makedirs(output_dir, exist_ok=True)

            # Define the output file path
            file_name, _ = os.path.splitext(os.path.basename(file_path))
            output_file = os.path.join(output_dir, f"{file_name}.md")

            # Check if the file already exists
            if os.path.exists(output_file):
                if self.skip_existing:
                    print(f"Skipping existing file: {output_file}")
                    return True, "File already exists, skipping as per configuration"
                else:
                    print(
                        f"WARNING: Documentation file {output_file} already exists and will be overwritten."
                    )

            with open(output_file, "w") as output:
                # Add timestamp at the top of the file
                print(
                    os.path.basename(file_path),
                    file=output,
                )
                timestamp = datetime.now().strftime("%d %B %Y at %H:%M:%S")
                print(
                    f"This documentation file was created on {timestamp}\n", file=output
                )

                print("## File path\n", file=output)
                print(f"{file_path}\n", file=output)

                try:
                    response = self._get_completion(prompt)
                    print(response, file=output)
                except openai.error.APIConnectionError:
                    print(
                        f"Error communicating with OpenAI for file {file_path}. Skipping this file."
                    )
                    return False, f"Error processing file {file_path}"

                print(f"Wrote documentation file {output_file}")

            return True, "Processed file successfully"

    def process_all_files(self):
        file_paths = self._get_file_paths()
        total_files = len(file_paths)
        print("Files:",total_files,"\n",file_paths)
        for i, file_path in enumerate(file_paths):
            print(f"Processing file {i+1}/{total_files}: {file_path}")
            success, message = self._process_file(file_path)
            if not success:
                print(f"{message} {i+1}/{total_files}: {file_path}")

    def process_single_file(self, file_path):
        print("TODO: Function not implemented yet")
        exit(1)
        # success, message = self._process_file(file_path)
        # if not success:
        #     print(f"{message}: {file_path}")
