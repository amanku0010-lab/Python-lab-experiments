# Python program to copy the contents of a file to another file.

import shutil

source = "source.txt"
destination = "destination.txt"

shutil.copyfile(source, destination)

print("File copied successfully.")
