import os
import glob

# Define the target string you want to search for
target_string = "setup"

# Get the current directory where the script is located
current_directory = os.path.dirname(os.path.realpath(__file__))

# Use the glob module to list all files in the current directory
file_list = glob.glob(os.path.join(current_directory, '*'))

# Iterate through the list of files and search for the target string
matching_files = []

for file_path in file_list:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line_number, line in enumerate(lines, start=1):
            if target_string in line:
                matching_files.append((file_path, line_number, line.strip()))

# Print the names of files and the lines containing the target string
if matching_files:
    print("Occurrences of the target string:")
    for file_path, line_number, line_content in matching_files:
        print(f"File: {file_path}, Line {line_number}: {line_content}")
else:
    print("No occurrences of the target string found in any file.")
