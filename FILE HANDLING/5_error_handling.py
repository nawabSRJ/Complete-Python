# Error Handling in File Operations
# ==================================
# This file demonstrates common errors when working with files and how to handle them.

# 1. Common file-related exceptions
# ==================================
# FileNotFoundError  - file or directory does not exist
# PermissionError    - no permission to read/write
# IsADirectoryError  - tried to open a directory as a file\n# NotADirectoryError - path component is not a directory
# FileExistsError    - file already exists (with mode 'x')
# IOError            - general input/output error
# ValueError         - invalid file mode or encoding

# 2. FileNotFoundError
# ====================
# Occurs when trying to open a non-existent file in read mode.

print("1. Handling FileNotFoundError:")
try:
    with open('nonexistent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found. Creating a new file instead.")
    with open('nonexistent_file.txt', 'w') as file:
        file.write("New file created due to error.\n")

# 2.1 Safe file reading with error handling
# ==========================================
def safe_read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: '{filename}' does not exist.")
        return None
    except PermissionError:
        print(f"Error: No permission to read '{filename}'.")
        return None
    except IOError as e:
        print(f"Error reading file: {e}")
        return None

print("\n2.1 Using safe file reading:")
content = safe_read_file('sample.txt')
if content:
    print(f"Content: {content[:50]}...")  # Print first 50 chars

# 3. PermissionError
# ==================
# Occurs when the program lacks permission to access the file.

print("\n3. Handling PermissionError:")
try:
    # This would fail on a read-only file
    with open('readonly_file.txt', 'w') as file:
        file.write("Attempt to write")
except PermissionError:
    print("Error: No permission to write to this file.")

# 4. FileExistsError
# ===================
# Occurs when using mode 'x' (create) and the file already exists.

print("\n4. Handling FileExistsError:")
try:
    with open('new_file.txt', 'x') as file:
        file.write("Creating a new file")
    print("File created successfully")
except FileExistsError:
    print("Error: File already exists. Use 'w' or 'a' mode instead.")

# 5. Invalid encoding
# ===================
# Occurs when the file encoding doesn't match the specified encoding.

print("\n5. Handling encoding errors:")
try:
    # Specify encoding when opening files
    with open('sample_text.txt', 'r', encoding='utf-8') as file:
        content = file.read()
except UnicodeDecodeError:
    print("Error: File encoding is not UTF-8. Try a different encoding.")
    # Try with a different encoding
    with open('sample_text.txt', 'r', encoding='latin-1') as file:
        content = file.read()

# 6. General try-except for file operations
# ===========================================
print("\n6. General file operation with comprehensive error handling:")
def process_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except PermissionError:
        print(f"Permission denied for '{filename}'.")
    except UnicodeDecodeError:
        print(f"Encoding error in '{filename}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return 0

line_count = process_file('sample_text.txt')
print(f"Lines in file: {line_count}")

# 7. Validating input before file operations
# ============================================
print("\n7. Input validation:")
import os

def safe_append_to_file(filename, content):
    # Validate inputs
    if not filename or not isinstance(filename, str):
        print("Error: Invalid filename")
        return False
    
    if not content:
        print("Error: Content cannot be empty")
        return False
    
    # Check if filename is valid
    if os.path.isdir(filename):
        print(f"Error: '{filename}' is a directory, not a file.")
        return False
    
    try:
        with open(filename, 'a') as file:
            file.write(content + '\n')
        return True
    except Exception as e:
        print(f"Error appending to file: {e}")
        return False

# Test safe append
if safe_append_to_file('append_demo.txt', 'New entry'):
    print("Successfully appended to file")

# 8. Cleaning up after errors
# =============================
# Use finally block to ensure cleanup happens even if error occurs.

print("\n8. Using finally for cleanup:")
file = None
try:
    file = open('important.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    if file:
        file.close()
        print("File closed in finally block")

# 9. Best practices for error handling
# =====================================
# - Always use try-except for file operations.
# - Catch specific exceptions, not just generic Exception.
# - Use context managers (with statement) for automatic cleanup.
# - Provide meaningful error messages to the user.
# - Validate input before attempting file operations.
# - Use finally only when necessary (context manager is preferred).
