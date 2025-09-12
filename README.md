# Python Line Counter

This Python script calculates the total number of lines of code in all `.py` (Python) files within a given project directory (including all subdirectories).

## Usage

1. **Save the script** as `count_python_lines.py`.

2. **Run the script** from your terminal:

   ```bash
   python count_python_lines.py <directory_path>
   ```

   - Replace `<directory_path>` with the path to your project directory.
   - Example:
     ```bash
     python count_python_lines.py .
     ```

## What It Does

- Recursively searches through the specified directory.
- Counts the total number of lines in all files ending with `.py`.
- Handles files with UTF-8 encoding by default. Skips files that can't be read.

## Example Output

```
Total number of lines in Python files: 1234
```

## Notes

- Only counts physical lines (including blank lines and comments).
- Skips files that can't be opened or decoded as UTF-8.
