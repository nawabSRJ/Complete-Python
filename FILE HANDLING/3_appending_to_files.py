# Appending to Files in Python\n# =============================
# This file demonstrates how to add content to the end of existing files.
# Appending preserves existing content, unlike writing.

# 1. Append mode 'a' overview
# ===========================
# Mode 'a' appends to the end of a file.
# If the file doesn't exist, it is created.
# If the file exists, new content is added without erasing what's there.

print("1. Creating a file and appending to it:")
# Create initial file
with open('append_demo.txt', 'w') as file:
    file.write("Initial content\n")

print("Initial file content:")
with open('append_demo.txt', 'r') as file:
    print(repr(file.read()))

# Append more content
with open('append_demo.txt', 'a') as file:
    file.write("Appended line 1\n")
    file.write("Appended line 2\n")

print("After appending:")
with open('append_demo.txt', 'r') as file:
    print(repr(file.read()))

# 2. Append vs Write comparison
# ==============================
# This demonstrates the critical difference between 'a' and 'w' modes.

print("\n2. Append vs Write comparison:")
# Create a file
with open('comparison.txt', 'w') as file:
    file.write("Original data\n")

# Append - preserves original
with open('comparison.txt', 'a') as file:
    file.write("Appended data\n")

print("After append (original preserved):")
with open('comparison.txt', 'r') as file:
    print(repr(file.read()))

# Write - erases everything
with open('comparison.txt', 'w') as file:
    file.write("New data\n")

print("After write (original erased):")
with open('comparison.txt', 'r') as file:
    print(repr(file.read()))

# 3. Appending in a loop
# ======================
# Common use case: log multiple events to a file over time.

print("\n3. Appending in a loop (simulating log entries):")
log_file = 'application.log'

# Clear the log first
with open(log_file, 'w') as f:
    pass  # creates empty file

# Simulate adding log entries
for i in range(1, 4):
    with open(log_file, 'a') as f:
        f.write(f"2026-06-10 10:0{i}:00 - Event {i} occurred\n")

print("Log file content:")
with open(log_file, 'r') as file:
    print(file.read())

# 4. Appending with print()
# ==========================
# You can also use print() with 'a' mode for convenient appending.

print("\n4. Using print() with append mode:")
with open('append_demo.txt', 'a') as f:
    print("New line added via print()", file=f)
    print(f"Timestamp: 2026-06-10", file=f)

print("After appending with print():")
with open('append_demo.txt', 'r') as file:
    print(file.read())

# 5. Append mode behavior
# =======================
# - File pointer starts at the END of the file.
# - All writes go to the end, regardless of file size.
# - Original content is never modified.
# - If file doesn't exist, it is created.

# 6. When to use append mode
# ===========================
# - Logging events or errors.
# - Building up a file over multiple operations.
# - Recording user input across multiple sessions.
# - Adding data from multiple sources to one file.

# 7. Important notes
# ==================
# - Remember to include \n for newlines in appended content.
# - Append mode is safer than write mode for existing important files.
# - Always close files properly, or use context managers.
