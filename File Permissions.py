import os

# The file you want to check permissions for
file_path = "example.txt"

# Check if the file exists
if os.path.exists(file_path):
    # Check the permissions
    print(f"Checking permissions for: {file_path}")
    print(f"Readable: {'Yes' if os.access(file_path, os.R_OK) else 'No'}")
    print(f"Writable: {'Yes' if os.access(file_path, os.W_OK) else 'No'}")
    print(f"Executable: {'Yes' if os.access(file_path, os.X_OK) else 'No'}")

    # Try to open the file (read-only)
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("\nFile content:")
            print(content)
    except PermissionError:
        print("\nPermission Denied: You don't have permission to read this file.")
else:
    print(f"File not found: {file_path}")

# -----------------------------------------------------------------------------------
# echo "Hello, selwan is here." > example.txt
# chmod 644 example.txt     
