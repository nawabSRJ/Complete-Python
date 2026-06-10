# Practical File Handling Examples
# ==================================
# This file contains real-world scenarios and practical examples.

import os
import json
import csv
from datetime import datetime

# 1. Reading and processing a log file
# =====================================
print("1. Processing log files:")

# Create a sample log file
log_content = \"\"\"2026-06-10 10:05:12 - INFO - Application started
2026-06-10 10:05:15 - ERROR - Database connection failed
2026-06-10 10:05:20 - WARNING - Retrying connection
2026-06-10 10:05:22 - INFO - Database connected successfully
2026-06-10 10:05:30 - INFO - Loading configuration
2026-06-10 10:06:00 - ERROR - Invalid configuration format\"\"\"

with open('app.log', 'w') as f:
    f.write(log_content)

# Parse and filter errors
print("Errors in log file:")
with open('app.log', 'r') as f:
    for line in f:
        if 'ERROR' in line:
            print(f\"  {line.strip()}\")

# 2. Converting CSV to JSON
# ==========================
print(\"\\n2. Converting CSV to JSON:\")

# Create a CSV file
csv_data = [
    ['Name', 'Email', 'Department'],
    ['Srajan', 'srajan@company.com', 'Engineering'],
    ['Aditi', 'aditi@company.com', 'Marketing'],
    ['Ravi', 'ravi@company.com', 'Sales'],
]

with open('employees_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(csv_data)

# Convert CSV to JSON
employees = []
with open('employees_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    employees = list(reader)

with open('employees_data.json', 'w') as f:
    json.dump(employees, f, indent=2)

print(f\"Converted {len(employees)} employees to JSON\")

# 3. Backup important files
# ==========================
print(\"\\n3. Creating file backups:\")

import shutil
from pathlib import Path

def backup_file(filename):
    \"\"\"Create a timestamped backup of a file.\"\"\"
    if not os.path.exists(filename):
        print(f\"File '{filename}' not found\")
        return False
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_name = f\"{filename}.backup_{timestamp}\"
    
    try:
        shutil.copy2(filename, backup_name)
        print(f\"Backup created: {backup_name}\")
        return True
    except Exception as e:
        print(f\"Error creating backup: {e}\")
        return False

# Create a file to backup
with open('important_data.txt', 'w') as f:
    f.write('Important data that needs backing up')

backup_file('important_data.txt')

# 4. Merging multiple files
# ==========================
print(\"\\n4. Merging multiple files:\")

# Create multiple files
for i in range(1, 4):
    with open(f'part_{i}.txt', 'w') as f:
        f.write(f\"Content of part {i}\\n\")

# Merge them
merged_content = \"\"
for i in range(1, 4):
    with open(f'part_{i}.txt', 'r') as f:
        merged_content += f.read()

with open('merged_file.txt', 'w') as f:
    f.write(merged_content)

print(f\"Merged 3 files into 'merged_file.txt'\")

# 5. Finding and listing files
# ==============================
print(\"\\n5. Finding files by pattern:\")

def find_files(directory, extension):
    \"\"\"Find all files with a specific extension in a directory.\"\"\"
    files = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files.append(filename)
    return files

# Find all .txt files in current directory
txt_files = find_files('.', '.txt')
print(f\"Found {len(txt_files)} .txt files: {txt_files[:3]}...\")

# 6. Configuration file management
# ==================================
print(\"\\n6. Managing configuration files:\")

# Create a configuration file
config = {
    'database': {
        'host': 'localhost',
        'port': 5432,
        'username': 'admin'
    },
    'api': {
        'timeout': 30,
        'retries': 3
    },
    'debug': True
}

with open('config.json', 'w') as f:
    json.dump(config, f, indent=2)

# Read and modify configuration
with open('config.json', 'r') as f:
    config = json.load(f)

# Update a setting
config['api']['timeout'] = 60

# Save back
with open('config.json', 'w') as f:
    json.dump(config, f, indent=2)

print(\"Configuration file updated\")

# 7. Reading specific lines from a large file
# ============================================
print(\"\\n7. Reading specific line numbers:\")

def get_line(filename, line_number):
    \"\"\"Get a specific line from a file (1-indexed).\"\"\"
    try:
        with open(filename, 'r') as f:
            for i, line in enumerate(f, 1):
                if i == line_number:
                    return line.strip()
    except Exception as e:
        print(f\"Error: {e}\")
    return None

# Create a test file
with open('lines.txt', 'w') as f:
    for i in range(1, 11):
        f.write(f\"Line {i}\\n\")

# Get 5th line
fifth_line = get_line('lines.txt', 5)
print(f\"5th line: {fifth_line}\")

# 8. Counting lines and words
# ============================
print(\"\\n8. Analyzing file content:\")

def analyze_file(filename):
    \"\"\"Count lines, words, and characters in a file.\"\"\"
    try:
        with open(filename, 'r') as f:
            content = f.read()
            lines = content.count('\\n') + 1
            words = len(content.split())
            characters = len(content)
            return {
                'lines': lines,
                'words': words,
                'characters': characters
            }
    except Exception as e:
        print(f\"Error: {e}\")
    return None

stats = analyze_file('merged_file.txt')
if stats:
    print(f\"File stats: {stats['lines']} lines, {stats['words']} words, {stats['characters']} chars\")

# 9. Organizing files into directories
# =====================================
print(\"\\n9. Organizing files by extension:\")

def organize_files(source_dir='.'):
    \"\"\"Create subdirectories for different file types.\"\"\"
    extensions = {}
    
    for filename in os.listdir(source_dir):
        if os.path.isfile(filename):
            _, ext = os.path.splitext(filename)
            if ext:
                ext = ext[1:]  # Remove the dot
                if ext not in extensions:
                    extensions[ext] = []
                extensions[ext].append(filename)
    
    print(f\"File types found: {list(extensions.keys())}\")
    return extensions

file_groups = organize_files()

# 10. Safe file operations with context manager
# ==============================================
print(\"\\n10. Safe file operations:\")

class FileManager:
    \"\"\"Context manager for safe file operations.\"\"\"
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False

# Usage
with FileManager('example.txt', 'w') as f:
    f.write('Managed file operation')

print(\"File operation completed safely\")

# 11. Quick reference - Common patterns
# ======================================
print(\"\\n11. Common file handling patterns:\")
print(\"\"\"\n
# Read entire file
with open('file.txt', 'r') as f:
    content = f.read()

# Read line by line
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())

# Write to file
with open('file.txt', 'w') as f:
    f.write('content')

# Append to file
with open('file.txt', 'a') as f:
    f.write('more content')

# Read JSON
with open('file.json', 'r') as f:
    data = json.load(f)

# Write JSON
with open('file.json', 'w') as f:
    json.dump(data, f, indent=2)

# Read CSV
with open('file.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

# Write CSV
with open('file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
\"\"\")\n