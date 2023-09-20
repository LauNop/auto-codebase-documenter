import os

def read_gitignore(file_path):
    try:
        with open(file_path, 'r') as gitignore_file:
            lines = gitignore_file.readlines()
            patterns = [line.strip() for line in lines if line.strip() and not line.startswith("#")]
            return patterns
    except FileNotFoundError:
        print(f"The .gitignore file at {file_path} was not found.")
        return []


if __name__ == "__main__":
    gitignore_file_path = ".gitignore"  # Change this to the path of your .gitignore file
    ignore_patterns = read_gitignore(gitignore_file_path)

    if ignore_patterns:
        print("Ignore patterns in .gitignore:")
        for pattern in ignore_patterns:
            print(pattern)


if __name__ == "__main__":
    read_gitignore('.gitignore')
