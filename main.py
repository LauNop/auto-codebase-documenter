import os
import fnmatch

def forward_slash_to_backslash(input_string):
    # Replace all forward slashes with backslashes
    result = input_string.replace('/', '\/')
    return result

def get_files(root_dir, ignore_patterns=None):
    # Initialize a list to store the file paths
    file_list = []

    # Create a set to store the patterns from .gitignore
    gitignore_patterns = set()

    # Check if a .gitignore file exists and add its patterns to the set
    gitignore_path = os.path.join(root_dir, ".gitignore")
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r") as gitignore_file:
            for line in gitignore_file:
                line = line.strip()
                if line and not line.startswith("#"):  # Ignore comments and empty lines
                    line = forward_slash_to_backslash(line)
                    gitignore_patterns.add(line)

    # If additional ignore patterns are provided, add them to the set
    if ignore_patterns:
        gitignore_patterns.update(ignore_patterns)

    print(gitignore_patterns)
    # Walk through the root directory and its subdirectories
    count = 0
    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            file_path = os.path.join(root, filename)
            relative_path = os.path.relpath(file_path, root_dir)
            print("File path:",file_path)
            print("Relative path:",relative_path)


            # Check if the file matches any of the ignore patterns
            if any(fnmatch.fnmatchcase(relative_path, pattern) for pattern in gitignore_patterns):
                continue  # Skip files that match the ignore patterns
            print(count)
            count += 1
            file_list.append(file_path)

    return file_list


# Usage example:
if __name__ == "__main__":

    root_directory = "."
    additional_ignore_patterns = ["*.txt", "*.md","setup.py"]  # Add any additional patterns to ignore
    files = get_files(root_directory, additional_ignore_patterns)

    # Print the list of files
    # for file in files:
    #     print(file)
    print(len(files))