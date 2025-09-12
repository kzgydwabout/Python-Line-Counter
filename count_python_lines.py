import os

def count_python_lines(directory):
    total_lines = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        total_lines += len(lines)
                except (UnicodeDecodeError, FileNotFoundError):
                    print(f"Could not read {file_path}")
    return total_lines

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python count_python_lines.py <directory>")
    else:
        directory = sys.argv[1]
        lines = count_python_lines(directory)
        print(f"Total number of lines in Python files: {lines}")
