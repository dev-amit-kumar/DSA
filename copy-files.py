#!/usr/bin/env python3
import os
import shutil
import re
import filecmp

not_include_dir = [".git", "leetcode", ".vscode", "info", "logs", "refs", "heads", "remotes", "origin", "hooks", "refs", "heads", "tags", "remotes", "origin", "pack", "my_env"]

def copy_files_with_regex(src_folder, dest_folder, regex_pattern):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    skip_count = 0
    copy_count = 0
    override_count = 0
    # Traverse the source folder and its subdirectories
    for root, dirs, files in os.walk(src_folder):
        folder_name = os.path.basename(root)
        if folder_name in not_include_dir:
            continue
        for file in files:
            if re.search(regex_pattern, file) :
                # Get the full path of the source file
                src_path = os.path.join(root, file)
                # Get the filename and extension
                file_name, file_ext = os.path.splitext(file)
                # Construct the new filename
                new_file_name = f"{file_name}({folder_name}){file_ext}"
                dest_path_with_new_name = os.path.join(dest_folder, os.path.relpath(file, src_folder).replace(file, new_file_name))
                if os.path.exists(dest_path_with_new_name):
                    # Compare file data
                    if filecmp.cmp(src_path, dest_path_with_new_name):
                        skip_count += 1
                        continue
                    else:
                        # Delete the existing file
                        os.remove(dest_path_with_new_name)
                        override_count += 1
                # Copy the file to the destination folder
                shutil.copy2(src_path, dest_path_with_new_name)
                copy_count += 1
                print(f"Copied {new_file_name}")
    print(f"Skip count: {skip_count}")
    print(f"Copy count: {copy_count - override_count}")
    print(f"Over ride count: {override_count}")

def rename_files_and_folders_in_directory(src_folder):
    """
    Traverse the source folder and rename files and folders to lowercase, 
    replacing spaces with hyphens.
    """
    rename_count = 0
    skip_count = 0

    # Rename all files first
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            old_file_path = os.path.join(root, file)
            new_file_name = file.lower().replace(' ', '-')
            new_file_path = os.path.join(root, new_file_name)

            if old_file_path != new_file_path:
                if os.path.exists(new_file_path):
                    print(f"Skipping file: {new_file_name} (already exists)")
                    skip_count += 1
                else:
                    os.rename(old_file_path, new_file_path)
                    print(f"Renamed file: {file} -> {new_file_name}")
                    rename_count += 1

    # Rename directories, starting from the deepest level
    for root, dirs, files in os.walk(src_folder, topdown=False):
        for dir_name in dirs:
            old_dir_path = os.path.join(root, dir_name)
            new_dir_name = dir_name.lower().replace(' ', '-')
            new_dir_path = os.path.join(root, new_dir_name)

            if old_dir_path != new_dir_path:
                if os.path.exists(new_dir_path):
                    print(f"Skipping folder: {new_dir_name} (already exists)")
                    skip_count += 1
                else:
                    os.rename(old_dir_path, new_dir_path)
                    print(f"Renamed folder: {dir_name} -> {new_dir_name}")
                    rename_count += 1

    print(f"\nTotal files and folders renamed: {rename_count}")
    print(f"Total files and folders skipped: {skip_count}")

source_folder = os.getcwd()
target_folder = f"{source_folder}/leetcode/"
regex_pattern = r"^\d+-[a-zA-Z-]+\.(cpp|py)+"  # Replace with your desired regex pattern
# Call the rename function
rename_files_and_folders_in_directory(source_folder)
copy_files_with_regex(source_folder, target_folder, regex_pattern)