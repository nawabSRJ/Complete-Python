# File Paths and Directory Operations
# ====================================
# This file demonstrates how to work with file paths and directories.

# 1. Absolute vs relative paths
# ==============================
# Absolute path: full path from the root of the file system.
#   Example: C:\\Users\\Srajan\\Documents\\file.txt  (Windows)
#   Example: /home/user/documents/file.txt           (Unix/Linux)
# Relative path: path relative to the current working directory.
#   Example: documents\\file.txt  (from current directory)
#   Example: .\\file.txt          (current directory)
#   Example: ..\\file.txt         (parent directory)

import os

# Get current working directory
print("1. Current working directory:")
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# 2. Working with the os module
# ==============================
# The os module provides functions to interact with the operating system.

print("\n2. Basic os module operations:")
# List files in current directory
print("Files in current directory:", os.listdir('.'))

# Check if a path exists
print(f"Does 'sample.txt' exist? {os.path.exists('sample.txt')}")

# Check if something is a file vs directory
if os.path.exists('sample.txt'):
    print(f"'sample.txt' is a file: {os.path.isfile('sample.txt')}")

# 3. Path joining and manipulation
# ==================================
# Use os.path.join() to build paths correctly for the current OS.
# This handles forward/backward slashes automatically.

print("\n3. Path joining:")
directory = "data"
filename = "records.txt"
full_path = os.path.join(directory, filename)
print(f"Joined path: {full_path}")

# 4. Creating directories
# =========================
# mkdir() creates a single directory.
# makedirs() creates a directory and all parent directories as needed.

print("\n4. Creating directories:")
# Create a single directory (parent must exist)
try:
    os.mkdir('my_folder')
    print("Created 'my_folder'")
except FileExistsError:
    print("'my_folder' already exists")

# Create nested directories (creates parents if needed)
try:
    os.makedirs('data/records/2026', exist_ok=True)
    print("Created nested directories: data/records/2026")
except FileExistsError:
    print("Nested directories already exist")

# 5. Checking file and directory properties
# ===========================================
print("\n5. File properties:")
if os.path.exists('sample.txt'):
    # Get file size
    size = os.path.getsize('sample.txt')
    print(f"File size: {size} bytes")
    
    # Get modification time
    mod_time = os.path.getmtime('sample.txt')
    print(f"Last modified: {mod_time}")

# 6. Listing directory contents
# ==============================
print("\n6. Listing directory contents:")
if os.path.isdir('data'):
    contents = os.listdir('data')
    print(f"Contents of 'data': {contents}")

# 7. Using pathlib (modern alternative)
# =======================================
# pathlib provides an object-oriented approach to paths.
from pathlib import Path

print("\n7. Using pathlib (modern approach):")
current_path = Path('.')
print(f"Current directory: {current_path.absolute()}")

# Create a path object
file_path = Path('data') / 'records' / 'file.txt'
print(f"Path object: {file_path}")

# Check if it exists
print(f"Exists: {file_path.exists()}")

# 8. Common file operations with os
# ===================================
print("\n8. File operations:")
# Rename a file
try:
    os.rename('old_name.txt', 'new_name.txt')
    print("File renamed")
except FileNotFoundError:
    print("File not found for renaming")

# Delete a file
try:
    if os.path.exists('file_to_delete.txt'):
        os.remove('file_to_delete.txt')
        print("File deleted")
except FileNotFoundError:
    print("File not found for deletion")

# Remove an empty directory
try:
    if os.path.exists('empty_folder'):
        os.rmdir('empty_folder')
        print("Empty directory removed")
except FileNotFoundError:
    print("Directory not found")
except OSError:
    print("Directory not empty or other error")

# 9. Key takeaways
# ================
# - Use os.path.join() to build paths (handles OS differences).
# - Use os.path.exists() to check if file/directory exists.
# - Use os.mkdir() for single directory, os.makedirs() for nested.
# - Use os.listdir() to see directory contents.
# - Use pathlib.Path for modern object-oriented path handling.
# - Always handle FileNotFoundError and FileExistsError gracefully.
