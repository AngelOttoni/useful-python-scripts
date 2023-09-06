import os

# Function to rename a file
def rename_file(file):
    # Split the file name and extension
    name, extension = os.path.splitext(file)

    # Handle specific renaming cases
    if ' (' in name:
        # Remove spaces and replace parentheses with underscores
        new_name = name.replace(' (', '_').replace(')', '')
    elif '(' in name:
        # Remove spaces and replace parentheses with underscores
        new_name = name.replace('(', '_').replace(')', '')
    elif '__' in name:
        # Replace double underscores with underscores
        new_name = name.replace('__', '_')
    else:
        # Remove spaces and replace other spaces with underscores
        new_name = name.replace(' ', '_')

    # Add the extension back to the new file name
    new_name += extension

    return new_name

# Function to rename all files in a directory
def rename_files_in_directory(directory):
    for file_name in os.listdir(directory):
        # Check if it's an image file with a recognized extension (case insensitive)
        if file_name.lower().endswith(allowed_extensions):
            # Apply the renaming function
            new_file_name = rename_file(file_name)

            # Full paths to the original and new files
            original_path = os.path.join(directory, file_name)
            new_path = os.path.join(directory, new_file_name)

            try:
                # Rename the file
                os.rename(original_path, new_path)
                print(f"Renamed: {file_name} -> {new_file_name}")
            except Exception as e:
                print(f"Error renaming {file_name}: {str(e)}")

# Directory containing the images
directory = './Ascomycota/'

# List of allowed extensions
allowed_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')

# Rename files in the directory
rename_files_in_directory(directory)

# Print a message to indicate that the files were renamed
print("The files have been successfully renamed!")

