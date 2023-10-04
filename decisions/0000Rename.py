import os

# Get the current directory where the script is located
current_directory = os.path.dirname(os.path.realpath(__file__))

# Iterate through the files in the current directory
for filename in os.listdir(current_directory):
    if filename.startswith("ToL"):
        new_filename = filename.replace("o", "O")
        # Make sure the new filename is different from the old one
        if new_filename != filename:
            old_filepath = os.path.join(current_directory, filename)
            new_filepath = os.path.join(current_directory, new_filename)
            os.rename(old_filepath, new_filepath)
            print(f"Renamed: {filename} -> {new_filename}")

print("File renaming complete.")
