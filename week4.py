# Ask the user for the input file name
filename = input("Enter the name of the file to read: ")

try:
    # Try to open and read the file
    with open(filename, 'r') as file:
        content = file.read()

    # Modify the content by capitalizing each word on the file
    modified_content = content.title()

    # Create a new file to write the modified content
    new_filename = "modified_" + filename
    with open(new_filename, 'w') as new_file:
        new_file.write(modified_content)

    print(f"Modified content written to '{new_filename}'.")

except FileNotFoundError:
    print("Error: The file was not found.")
except IOError:
    print("Error: The file could not be read or written.")
