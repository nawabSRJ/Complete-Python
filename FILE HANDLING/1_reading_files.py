# Reading Files in Python
# =======================
# This file demonstrates different methods to read file content.
# Each method has its own use case and performance characteristics.

# Setup: create a sample file for reading
# (In practice, the file already exists. We create it here for demonstration.)
with open('sample_text.txt', 'w') as f:
    f.write("Line 1: Introduction to Python\n")
    f.write("Line 2: Python is versatile\n")
    f.write("Line 3: File handling is important\n")
    f.write("Line 4: Reading files is fundamental\n")

# 1. read() method
# ================
# Reads the entire file content as a single string.
# Use when: you want all content at once and the file is not too large.

print("1. Using read() - entire file as one string:")
with open('sample_text.txt', 'r') as file:
    content = file.read()
    print(repr(content))  # repr shows escape characters like \n

# 2. readline() method
# ====================
# Reads one line at a time.
# Use when: you want to process lines one by one.

print("\n2. Using readline() - one line at a time:")
with open('sample_text.txt', 'r') as file:
    line1 = file.readline()
    line2 = file.readline()
    print("First line:", repr(line1))
    print("Second line:", repr(line2))

# 3. readlines() method
# =====================
# Reads all lines and returns a list where each element is a line.
# Use when: you want all lines as a list for easy iteration.

print("\n3. Using readlines() - list of all lines:")
with open('sample_text.txt', 'r') as file:
    lines = file.readlines()
    print("Lines list:", lines)
    print("Number of lines:", len(lines))

# 4. Iterating over a file object directly
# ==========================================
# When you iterate over an open file, it automatically reads lines one by one.
# Use when: you want to process large files without loading everything into memory.
# This is memory-efficient and the most Pythonic approach.

print("\n4. Using for loop - memory efficient line iteration:")
with open('sample_text.txt', 'r') as file:
    for index, line in enumerate(file, start=1):
        print(f"Line {index}: {repr(line)}")
# ? 'start=1' just tells the enumerate function to put index 0 as 1 so when the lines print out we see 1 and not 0. We can put any numeric value at start. Also, that won't change the starting point of file content, that will remain same. We can also give negative values to start.



# 5. Stripping newline characters
# ================================
# By default, readline() and iteration include the '\n' character.
# To remove it, use strip() or rstrip().

print("\n5. Removing newline characters:")
with open('sample_text.txt', 'r') as file:
    for line in file:
        cleaned_line = line.strip()  # removes \n and whitespace
        print(f"Cleaned: '{cleaned_line}'")

# 6. Reading specific number of characters
# ==========================================
# read(n) reads exactly n characters, or fewer if EOF is reached.

print("\n6. Reading specific characters:")
with open('sample_text.txt', 'r') as file:
    first_10_chars = file.read(10)
    print("First 10 characters:", repr(first_10_chars))
    next_5_chars = file.read(5)
    print("Next 5 characters:", repr(next_5_chars))

# 7. Key differences summary
# ==========================
# read()       - entire file as string | use for small files
# readline()   - one line as string | use for step-by-step processing
# readlines()  - list of all lines | use when you need a list structure
# for loop     - iterate lines | use for large files, most memory efficient
#
# Note: all methods include '\n' at line ends. Use strip() to remove them.
