# Writing to Files in Python
# ===========================
# This file demonstrates how to write data to files.
# Writing creates or overwrites files, so be careful with existing data.

# 1. Basic write() method
# =======================
# write() writes a string to the file.
# Use when: you want to write strings directly to a file.
# Important: write() does NOT automatically add newlines.

print("1. Using write() method:")
with open('output1.txt', 'w') as file:
    file.write("Hello, World!")
    file.write(" Welcome to file handling.")
    # file.write("This is on the same line.")

# Read back the file to verify
with open('output1.txt', 'r') as file:
    print("File content:", repr(file.read()))

# 2. Writing multiple lines
# ==========================
# To write multiple lines, explicitly include newline characters \n.
# This gives you full control over formatting.

print("\n2. Writing multiple lines with newlines:")
with open('output2.txt', 'w') as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")

with open('output2.txt', 'r') as file:
    print("File content:")
    print(file.read())

# 3. writelines() method
# ======================
# writelines() takes a list of strings and writes them to the file.
# Important: writelines() does NOT add newlines between items.
# It writes exactly what you provide, so you must include \n if needed.

print("3. Using writelines() method:")
lines = ["First line\n", "Second line\n", "Third line\n"]
with open('output3.txt', 'w') as file:
    file.writelines(lines)

with open('output3.txt', 'r') as file:
    print("File content:")
    print(file.read())

# 4. Overwriting vs creating
# ===========================
# Mode 'w' creates a new file OR overwrites an existing file.
# This means existing content is erased.
# Be careful when using 'w' with important files!

print("\n4. Demonstrating overwrite behavior:")
# First write
with open('overwrite_demo.txt', 'w') as file:
    file.write("Original content")

print("After first write:")
with open('overwrite_demo.txt', 'r') as file:
    print(repr(file.read()))

# Second write with mode 'w' - overwrites
with open('overwrite_demo.txt', 'w') as file:
    file.write("New content - original is gone")

print("After second write with 'w' mode:")
with open('overwrite_demo.txt', 'r') as file:
    print(repr(file.read()))

# 5. Using print() to write to files
# ===================================
# print() can write to a file by using the file parameter.
# This is convenient for formatted output.

print("\n5. Using print() to write to file:")
with open('output4.txt', 'w') as file:
    print("Name: Srajan", file=file)
    print("Age: 21", file=file)
    print("City: New Delhi", file=file)

with open('output4.txt', 'r') as file:
    print("File content:")
    print(file.read())

# 6. Key difference: write() vs writelines()
# ===========================================
# write(string)        - writes one string
# writelines(list)     - writes all strings in list without adding separators
# print(..., file=f)   - formatted output with automatic newlines

# 7. Important notes
# ==================
# - Mode 'w' truncates (erases) existing file content.
# - Remember to include \n for newlines; write() doesn't add them automatically.
# - Use 'a' mode to append instead of overwriting (see next file).
# - Always close files or use context managers to ensure data is written.
