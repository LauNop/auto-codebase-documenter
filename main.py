import os
import fnmatch


def forward_slash_to_backslash(input_string):
    # Replace all forward slashes with backslashes
    result = input_string.replace('/', '\/')
    return result


def get_files(root_dir, ignore_list=[], unwanted_file=[]):
    # Initialize a list to store the file paths
    if unwanted_file is None:
        unwanted_file = []
    file_list = []

    # Create a set to store the patterns from .gitignore
    ignore_patterns = set()

    # Check if a .gitignore file exists and add its patterns to the set
    gitignore_path = os.path.join(root_dir, ".gitignore")
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r") as gitignore_file:
            for line in gitignore_file:
                line = line.strip()
                if line and not line.startswith("#"):  # Ignore comments and empty lines
                    ignore_patterns.add(line)

    # If additional ignore patterns are provided, add them to the set
    if ignore_list:
        ignore_patterns.update(ignore_list)

    print(ignore_patterns)
    # Walk through the root directory and its subdirectories
    count = 0
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for ignore_pattern in ignore_patterns:
            if ignore_pattern in dirnames:
                dirnames.remove(ignore_pattern)
        file_list.extend(
            [
                os.path.join(dirpath, filename)
                for filename in filenames
                if any(filename.endswith(file_type) for file_type in [".py"]) and filename not in unwanted_file
            ]
        )
    return file_list


# Usage example:
if __name__ == "__main__":
    root_directory = "."
    additional_ignore_patterns = ["tests", ".git"]  # Add any additional patterns to ignore
    unwanted_file = ["setup.py", "__init__.py"]
    files = get_files(root_directory, additional_ignore_patterns,unwanted_file)

    # Print the list of files
    for file in files:
        print(file)
    print(len(files))
