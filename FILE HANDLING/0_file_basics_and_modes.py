# File Handling in Python - Introduction & Basic Concepts
# ========================================================
# This file covers the fundamentals of working with files in Python.
#
# What is File Handling?
# File handling is the process of working with files in a program. This involves:
# - Opening files
# - Reading or writing data
# - Closing files
#
# Why is file handling important?
# - Data persistence: save data to disk so it survives after the program ends.
# - Reading external data: load data from files for processing.
# - Logging: record program events to files for debugging and monitoring.
#
# Key concepts:
# - File modes: how you want to interact with the file (read, write, append)
# - File object: Python's representation of an open file
# - Encoding: character encoding format (usually UTF-8)

# 1. Basic file operations: open and close
# =========================================
# To work with a file, you first open it using open(), then close it when done.

# Simple example: open and close a file
file = open('sample.txt', 'r')  # 'r' means read mode
print("File object:", file)
print("File name:", file.name)
print("File mode:", file.mode)
file.close()

# 2. File modes
# =============
# Different file modes allow different operations:
# 'r'  - Read: opens a file for reading (default). Error if file doesn't exist.
# 'w'  - Write: opens a file for writing. Creates file if it doesn't exist.
#                Truncates (erases) the file if it already exists.
# 'a'  - Append: opens a file for appending. Creates file if it doesn't exist.
#                Writes are added to the end without erasing existing content.
# 'x'  - Create: creates a new file. Error if file already exists.
# 'b'  - Binary: modifies other modes to work with binary data (e.g., 'rb', 'wb')
# '+'  - Read and Write: modifies other modes to allow both operations (e.g., 'r+')

# 3. The context manager approach (recommended)
# ==============================================
# Using "with" automatically closes the file, even if an error occurs.
# This is safer and cleaner than manual close().

with open('sample.txt', 'r') as file:
    print("Using context manager - file is automatically closed after this block")

# 4. Why use context managers?
# ============================
# - Automatic file closing: no risk of forgetting close().
# - Exception safe: file is closed even if an error occurs.
# - Cleaner, more readable code.
# - Recommended approach for all file operations.

# 5. Key takeaways
# ================
# - Always close files to free up system resources.
# - Use "with" statements for automatic file closing.
# - Choose the correct file mode for your task.
# - File paths can be absolute or relative.
