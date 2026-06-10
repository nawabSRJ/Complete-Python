# File Copying, Moving, and Deletion
# ===================================
# This file demonstrates how to perform file operations like copy, move, and delete.

import os
import shutil

# 1. Copying files using shutil.copy()
# =====================================
# shutil.copy(source, destination)
# Copies file content and permissions.
# Use when: you want to duplicate a file to another location.

print("1. Copying files:")
try:
    # First create a file to copy
    with open('original.txt', 'w') as f:
        f.write('This is the original file.\n')
    
    # Copy the file
    shutil.copy('original.txt', 'copy.txt')
    print("File copied: original.txt -> copy.txt")
except Exception as e:
    print(f"Error copying file: {e}")

# 2. Copying file with metadata using shutil.copy2()
# ===================================================
# shutil.copy2() is like copy() but also preserves metadata (timestamps, etc.)

print("\n2. Copying with metadata:")
try:
    shutil.copy2('original.txt', 'copy_with_metadata.txt')
    print("File copied with metadata preservation")
except Exception as e:
    print(f"Error: {e}")

# 3. Copying entire directories
# ==============================
# shutil.copytree(source_dir, dest_dir)
# Recursively copies a directory and all its contents.

print("\n3. Copying directories:")
try:
    # Create a source directory with files
    os.makedirs('source_folder', exist_ok=True)
    with open('source_folder/file1.txt', 'w') as f:
        f.write('File 1')
    with open('source_folder/file2.txt', 'w') as f:
        f.write('File 2')
    
    # Copy the entire directory
    if not os.path.exists('backup_folder'):
        shutil.copytree('source_folder', 'backup_folder')
        print("Directory copied: source_folder -> backup_folder")
except Exception as e:
    print(f"Error copying directory: {e}")

# 4. Moving files using shutil.move()
# ====================================
# shutil.move(source, destination)
# Moves file to a new location. On same filesystem, it's a rename.
# On different filesystems, it copies then deletes the original.

print("\n4. Moving files:")
try:
    # Move a file
    if os.path.exists('copy.txt'):
        shutil.move('copy.txt', 'moved_file.txt')
        print("File moved: copy.txt -> moved_file.txt")
except Exception as e:
    print(f"Error moving file: {e}")

# 5. Renaming files using os.rename()
# ====================================
# os.rename(old_name, new_name)
# Renames a file. Works only on the same filesystem.

print("\n5. Renaming files:")
try:
    with open('to_rename.txt', 'w') as f:
        f.write('This file will be renamed')
    
    os.rename('to_rename.txt', 'renamed_file.txt')
    print("File renamed: to_rename.txt -> renamed_file.txt")
except FileNotFoundError:
    print("File not found for renaming")
except Exception as e:
    print(f"Error: {e}")

# 6. Deleting files using os.remove()
# ====================================
# os.remove(filename)
# Permanently deletes a file. Cannot be undone!
# Be careful when using this.

print("\n6. Deleting files:")
try:
    with open('temp_file.txt', 'w') as f:
        f.write('This file will be deleted')
    
    if os.path.exists('temp_file.txt'):
        os.remove('temp_file.txt')
        print("File deleted: temp_file.txt")
except Exception as e:
    print(f"Error deleting file: {e}")

# 7. Deleting directories using os.rmdir()
# =========================================
# os.rmdir(dirname)
# Removes an EMPTY directory only.
# Use shutil.rmtree() for non-empty directories.

print("\n7. Deleting empty directories:")
try:
    os.makedirs('empty_dir', exist_ok=True)
    os.rmdir('empty_dir')
    print("Empty directory deleted: empty_dir")
except OSError as e:
    print(f"Error: {e}")

# 8. Deleting non-empty directories using shutil.rmtree()
# ========================================================
# shutil.rmtree(dirname)
# Recursively deletes a directory and all its contents.
# Warning: This is permanent and cannot be undone!

print("\n8. Deleting non-empty directories:")
try:
    # Create a directory with files
    os.makedirs('temp_folder', exist_ok=True)
    with open('temp_folder/file.txt', 'w') as f:
        f.write('temp')
    
    # Delete the entire directory tree
    if os.path.exists('backup_folder'):
        shutil.rmtree('backup_folder')
        print("Non-empty directory deleted recursively")
except Exception as e:
    print(f"Error: {e}")

# 9. Safe file operations pattern
# ================================
def safe_copy(source, destination):
    \"\"\"Safely copy a file with error handling.\"\"\"
    try:
        if not os.path.exists(source):
            print(f\"Error: Source file '{source}' does not exist.\")
            return False
        
        if os.path.exists(destination):
            print(f\"Warning: Destination '{destination}' already exists. Overwriting.\")
        
        shutil.copy2(source, destination)
        print(f\"Successfully copied: {source} -> {destination}\")
        return True
    except Exception as e:
        print(f\"Error copying file: {e}\")
        return False

print("\n9. Safe file copy function:")
with open('test_source.txt', 'w') as f:
    f.write('Test content')
safe_copy('test_source.txt', 'test_destination.txt')

# 10. Comparing files
# ====================
# filecmp.cmp(file1, file2)
# Returns True if files are identical, False otherwise.

import filecmp

print("\n10. Comparing files:")
try:
    with open('file_a.txt', 'w') as f:
        f.write('Same content')
    with open('file_b.txt', 'w') as f:
        f.write('Same content')
    
    if filecmp.cmp('file_a.txt', 'file_b.txt'):
        print("Files are identical")
    else:
        print("Files are different")
except Exception as e:
    print(f"Error: {e}")

# 11. Key takeaways
# =================
# - shutil.copy() copies file contents and permissions.
# - shutil.copy2() also preserves metadata.
# - shutil.copytree() copies entire directories recursively.
# - shutil.move() moves files (rename on same filesystem).
# - os.rename() renames a file.
# - os.remove() permanently deletes a file.
# - os.rmdir() deletes empty directories only.
# - shutil.rmtree() deletes non-empty directories (use with caution!).
# - Always check if files exist before operations.
# - Use try-except for robust error handling.
