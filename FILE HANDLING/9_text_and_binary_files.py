# Working with Text and Binary Files
# ====================================
# This file demonstrates the differences between text and binary modes,
# encoding, and how to work with different file types.

# 1. Text vs Binary modes
# =======================
# Text mode ('r', 'w', 'a')  - interprets data as text with encoding
# Binary mode ('rb', 'wb')   - reads/writes raw bytes without encoding
#
# Use text mode for: text files, CSV, JSON
# Use binary mode for: images, videos, executables, compressed files

print("1. Understanding text vs binary mode:")
print("Text mode: interprets bytes as text using encoding (default UTF-8)")
print("Binary mode: works with raw bytes without encoding interpretation")

# 2. Reading text files with different encodings
# ===============================================
print("\n2. Working with text encodings:")

# Create a text file with UTF-8 encoding
with open('utf8_file.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, World! 你好 مرحبا\n')
    print("UTF-8 file created")

# Read with UTF-8 (correct encoding)
with open('utf8_file.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(f"Read with UTF-8: {content}")

# Common encodings:
# 'utf-8'    - Unicode (supports all languages) - default and recommended
# 'ascii'    - American Standard Code (only 0-127)
# 'latin-1'  - Western European
# 'cp1252'   - Windows Western European
# 'utf-16'   - Unicode 16-bit

# 3. Reading binary files
# ========================
print("\n3. Reading binary files:")

# Create a simple binary file
with open('binary_data.bin', 'wb') as f:
    data = bytes([72, 101, 108, 108, 111])  # \"Hello\" in ASCII
    f.write(data)
    print("Binary file created")

# Read as binary
with open('binary_data.bin', 'rb') as f:
    binary_content = f.read()
    print(f"Binary content: {binary_content}")
    print(f"Decoded as ASCII: {binary_content.decode('ascii')}")

# 4. Writing binary data
# =======================
print("\n4. Writing binary data:")

# Create a file with specific byte values
binary_data = bytes([0xFF, 0xD8, 0xFF, 0xE0])  # JPEG file signature
with open('binary_output.bin', 'wb') as f:
    f.write(binary_data)
    print("Binary data written")

# 5. Detecting file encoding
# ===========================
# For files with unknown encoding, try UTF-8 first, then fallback
print("\n5. Handling unknown encoding:")

def read_file_safe(filename):
    \"\"\"Attempt to read file with multiple encodings.\"\"\"
    encodings = ['utf-8', 'latin-1', 'cp1252', 'ascii']
    
    for encoding in encodings:
        try:
            with open(filename, 'r', encoding=encoding) as f:
                return f.read(), encoding
        except (UnicodeDecodeError, FileNotFoundError):
            continue
    
    return None, None

# Test with the UTF-8 file
content, used_encoding = read_file_safe('utf8_file.txt')
if content:
    print(f\"File read successfully with {used_encoding} encoding\")

# 6. Working with binary file formats
# =====================================
print("\n6. Creating and reading simple binary format:")

# Write structured binary data
import struct

with open('data.bin', 'wb') as f:
    # Pack an integer and a string
    data = struct.pack('i', 42)  # integer (4 bytes)
    f.write(data)
    f.write(b'Hello')  # string as bytes
    print("Structured binary data written")

# Read back
with open('data.bin', 'rb') as f:
    int_data = struct.unpack('i', f.read(4))  # read 4 bytes as integer
    str_data = f.read()  # read remaining as bytes
    print(f\"Integer: {int_data[0]}, String: {str_data.decode()}\")

# 7. Handling line endings
# =========================
# Different operating systems use different line endings:
# Windows: \\r\\n (CRLF)
# Unix/Linux/Mac: \\n (LF)
# Old Mac: \\r (CR)

print("\n7. Handling line endings:")
text_with_lines = \"Line 1\\nLine 2\\nLine 3\"

# Write with universal newline mode (automatic conversion)
with open('universal_newlines.txt', 'w', newline='') as f:
    f.write(text_with_lines)
    print("File written with newline=''")

# Read with universal newline support
with open('universal_newlines.txt', 'r', newline='') as f:
    lines = f.readlines()
    for line in lines:
        print(f\"Read line: {repr(line)}\")

# 8. Large file handling
# =======================
print("\n8. Reading large files efficiently:")

# For large files, read in chunks instead of all at once
def read_large_file_in_chunks(filename, chunk_size=1024):
    \"\"\"Read large file in chunks to save memory.\"\"\"
    with open(filename, 'r') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

# Example usage (with a smaller file for demo)
with open('large_file_demo.txt', 'w') as f:
    f.write('Data ' * 1000)

print(\"Reading in chunks:\")
total_chars = 0
for chunk in read_large_file_in_chunks('large_file_demo.txt', chunk_size=100):
    total_chars += len(chunk)

print(f\"Total characters read: {total_chars}\")

# 9. Working with image files (binary)
# =====================================
print(\"\n9. Working with image files:\")

# Read image file as binary
def get_image_info(filename):
    \"\"\"Get basic info about an image file.\"\"\"
    try:
        with open(filename, 'rb') as f:
            header = f.read(10)
            size = os.path.getsize(filename)
            return {
                'size_bytes': size,
                'header_hex': header.hex(),
                'size_kb': size / 1024
            }
    except FileNotFoundError:
        return None

import os
# This would work with actual image files
# info = get_image_info('image.jpg')

# 10. Comparing text vs binary mode output
# =========================================
print(\"\\n10. Text vs Binary comparison:\")
test_content = \"Hello\\nWorld\"

# Write in text mode
with open('text_mode.txt', 'w') as f:
    f.write(test_content)

# Write in binary mode
with open('binary_mode.txt', 'wb') as f:
    f.write(test_content.encode('utf-8'))

# Compare sizes
print(f\"Text mode file size: {os.path.getsize('text_mode.txt')} bytes\")
print(f\"Binary mode file size: {os.path.getsize('binary_mode.txt')} bytes\")

# 11. Best practices
# ==================
# - Always specify encoding explicitly (don't rely on defaults).
# - Use UTF-8 as default for text files.
# - Use binary mode for non-text files.
# - For unknown encoding files, try multiple encodings.
# - Read large files in chunks to save memory.
# - Be aware of line ending differences between OSes.
# - Use newline='' for cross-platform CSV/text files.
