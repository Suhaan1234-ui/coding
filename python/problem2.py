# Python program to print contents of a directory using ai

import os

# Path of the directory
directory = "/maggi"

# List all files and folders in the directory
contents = os.listdir(directory)

print("Contents of the directory are:")
for item in contents:
    print(item)