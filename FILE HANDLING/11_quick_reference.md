# File Handling - Quick Reference Guide
# =====================================
# A comprehensive quick reference for all file handling concepts and methods.

\"\"\"
TABLE OF CONTENTS:
1. File Modes
2. Opening and Closing Files
3. Reading Files
4. Writing Files
5. Appending to Files
6. File Operations (copy, move, delete)
7. Working with CSV Files
8. Working with JSON Files
9. File Paths and Directories
10. Error Handling
11. Common Patterns and Best Practices
\"\"\"

# ============================================================
# 1. FILE MODES - How to interact with files
# ============================================================
\"\"\"\nMode   |  Description                    | Creates | Truncates
-------|--------------------------------|---------|----------
'r'    | Read (default)                  | No      | No
'w'    | Write                           | Yes     | Yes (erases content)
'a'    | Append                          | Yes     | No
'x'    | Create (error if exists)        | Yes     | N/A
'b'    | Binary (append to other modes)  | -       | -
'+'    | Read+Write (append to mode)     | -       | -

Examples:
'r'     = Read text
'rb'    = Read binary
'w'     = Write text (overwrites)
'wb'    = Write binary (overwrites)
'a'     = Append text
'ab'    = Append binary
'r+'    = Read and write
'w+'    = Write and read (truncates)
\"\"\"

# ============================================================
# 2. OPENING AND CLOSING FILES
# ============================================================
\"\"\"\n# Manual open/close (NOT recommended)
file = open('file.txt', 'r')
# ... use file ...
file.close()

# Context manager (RECOMMENDED - automatic close)
with open('file.txt', 'r') as file:
    # ... use file ...
    pass
# File automatically closed here
\"\"\"

# ============================================================
# 3. READING FILES
# ============================================================
\"\"\"\nMethod              | Returns           | Use When
--------------------|-------------------|------------------------------------------
read()              | entire string     | file is small, need all content at once
read(n)             | n characters      | need exactly n characters
readline()          | one line (str)    | processing line by line manually
readlines()         | list of lines     | want a list of all lines
for line in file:   | iterate lines     | memory-efficient for large files (preferred)

Examples:
# Read entire file
with open('file.txt', 'r') as f:
    content = f.read()

# Read line by line
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())

# Get all lines as list
with open('file.txt', 'r') as f:
    lines = f.readlines()

# Read specific number of lines
with open('file.txt', 'r') as f:
    first_line = f.readline()
    second_line = f.readline()
\"\"\"

# ============================================================
# 4. WRITING FILES
# ============================================================
\"\"\"\nMethod              | Purpose
--------------------|--------------------------------------
write(string)       | Write a single string
writelines(list)    | Write multiple strings (no separators)
print(..., file=f)  | Write with print() formatting

Important: write() does NOT add newlines automatically!

Examples:
# Write to file
with open('file.txt', 'w') as f:
    f.write('Hello\\n')
    f.write('World\\n')

# Write with writelines
with open('file.txt', 'w') as f:
    f.writelines(['Line 1\\n', 'Line 2\\n'])

# Use print() for formatted output
with open('file.txt', 'w') as f:
    print('Name:', 'Srajan', file=f)
    print('Age:', 21, file=f)

# Multiple writes go to same location
with open('file.txt', 'w') as f:
    for i in range(5):
        f.write(f'Line {i}\\n')
\"\"\"

# ============================================================
# 5. APPENDING TO FILES
# ============================================================
\"\"\"\nMode 'a' appends to the END of file without erasing content.

# Append text
with open('file.txt', 'a') as f:
    f.write('New line at end\\n')

# Append with print()
with open('file.txt', 'a') as f:
    print('New entry', file=f)

# Key difference:
Mode 'w': creates/overwrites - DESTRUCTIVE
Mode 'a': appends - SAFE for existing files
\"\"\"

# ============================================================
# 6. FILE OPERATIONS
# ============================================================
\"\"\"\nimport os
import shutil

# Copy file
shutil.copy('source.txt', 'copy.txt')           # copy content and permissions
shutil.copy2('source.txt', 'copy.txt')          # also preserve metadata

# Copy directory
shutil.copytree('source_dir', 'dest_dir')       # copy entire directory

# Move/Rename
shutil.move('old_name.txt', 'new_name.txt')     # rename on same filesystem
os.rename('old.txt', 'new.txt')                 # alternative method

# Delete file
os.remove('file.txt')                           # permanent deletion

# Delete empty directory
os.rmdir('empty_dir')                           # only if empty

# Delete directory with content
shutil.rmtree('dir_name')                       # recursive deletion - BE CAREFUL!

# Check file properties
os.path.exists('file.txt')                      # True if exists
os.path.isfile('file.txt')                      # True if it's a file
os.path.isdir('dir_name')                       # True if it's a directory
os.path.getsize('file.txt')                     # file size in bytes
os.path.getmtime('file.txt')                    # modification time
os.path.dirname('/path/to/file.txt')            # returns '/path/to'
os.path.basename('/path/to/file.txt')           # returns 'file.txt'

# List directory contents
os.listdir('.')                                 # list files in current directory
os.listdir('/path/to/dir')                      # list files in specific directory

# Working with paths
os.path.join('folder', 'file.txt')              # join paths (OS-independent)
os.getcwd()                                     # get current working directory
os.chdir('/path/to/dir')                        # change working directory

# Create directories
os.mkdir('new_dir')                             # create single directory
os.makedirs('a/b/c', exist_ok=True)             # create nested directories
\"\"\"

# ============================================================
# 7. WORKING WITH CSV FILES
# ============================================================
\"\"\"\nimport csv

# Read CSV with csv.reader() - returns lists
with open('file.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:  # each row is a list
        print(row)

# Read CSV with csv.DictReader() - returns dicts (PREFERRED)
with open('file.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:  # each row is a dict with column names as keys
        print(row['Name'], row['Age'])

# Write CSV with csv.writer()
with open('file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerows([
        ['Alice', 25, 'London'],
        ['Bob', 30, 'Paris']
    ])

# Write CSV with csv.DictWriter()
with open('file.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Name', 'Age', 'City'])
    writer.writeheader()
    writer.writerow({'Name': 'Alice', 'Age': 25, 'City': 'London'})

# Important: Always use newline='' when opening CSV files!
\"\"\"

# ============================================================
# 8. WORKING WITH JSON FILES
# ============================================================
\"\"\"\nimport json

# Read JSON from file
with open('file.json', 'r') as f:
    data = json.load(f)  # returns Python object (dict/list)

# Write JSON to file
with open('file.json', 'w') as f:
    json.dump(data, f, indent=2)  # indent for readability

# Convert Python object to JSON string
json_string = json.dumps(data, indent=2)

# Parse JSON string to Python object
data = json.loads(json_string)

# Important:
json.load()   -> read from file
json.loads()  -> parse from string
json.dump()   -> write to file
json.dumps()  -> convert to string

# Handling non-serializable objects
def default_handler(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    return str(obj)

json.dump(data, f, default=default_handler)
\"\"\"

# ============================================================
# 9. FILE PATHS AND DIRECTORIES
# ============================================================
\"\"\"\nfrom pathlib import Path

# Absolute path: full path from root
# /home/user/documents/file.txt (Unix)
# C:\\Users\\user\\documents\\file.txt (Windows)

# Relative path: relative to current directory
# documents/file.txt
# ./file.txt (current directory)
# ../file.txt (parent directory)

# Working with paths
current_dir = os.getcwd()
file_path = os.path.join(directory, filename)

# Modern approach with pathlib
path = Path('data') / 'records' / 'file.txt'
path.exists()
path.is_file()
path.is_dir()
path.parent
path.name
path.stem
path.suffix
\"\"\"

# ============================================================
# 10. ERROR HANDLING
# ============================================================
\"\"\"\nCommon exceptions:
FileNotFoundError    - file doesn't exist
PermissionError      - no permission to access
IsADirectoryError    - tried to open directory as file
FileExistsError      - file already exists (mode 'x')
UnicodeDecodeError   - encoding error
IOError              - general I/O error

Recommended pattern:
try:
    with open('file.txt', 'r', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print('File not found')
except PermissionError:
    print('No permission')
except UnicodeDecodeError:
    print('Encoding error')
except Exception as e:
    print(f'Unexpected error: {e}')
\"\"\"

# ============================================================
# 11. COMMON PATTERNS AND BEST PRACTICES
# ============================================================
\"\"\"\n# Pattern 1: Safe file reading
def safe_read(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f'File not found: {filename}')
        return None

# Pattern 2: Safe file writing
def safe_write(filename, content):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f'Error writing file: {e}')
        return False

# Pattern 3: Process large files in chunks
def process_large_file(filename, chunk_size=1024):
    with open(filename, 'r') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

# Pattern 4: Configuration management
import json
with open('config.json', 'r') as f:
    config = json.load(f)
# Modify config
with open('config.json', 'w') as f:
    json.dump(config, f, indent=2)

# Best Practices:
# 1. Always use 'with' statement for automatic file closing
# 2. Specify encoding explicitly (usually 'utf-8')
# 3. Use meaningful variable names
# 4. Check if file exists before operations
# 5. Use try-except for error handling
# 6. For CSV files, always use newline=''
# 7. For large files, use generators or chunked reading\n# 8. Use relative paths for portability
\"\"\"

print(\"\"\"\nQUICK REFERENCE GUIDE - FILE HANDLING IN PYTHON\n\" + \"=\"*50)\nRefer to the comments in this file for:\n- File modes\n- Reading/writing methods\n- CSV and JSON handling\n- File operations\n- Error handling\n- Best practices\n\"\"\")\n