#!/usr/bin/env python3

import sys
import subprocess

# Check if the argument (oldFiles.txt) is provided
if len(sys.argv) < 2:
    print("Usage: ./changeJane.py <oldFiles.txt>")
    sys.exit(1)

# Open the file provided as argument (oldFiles.txt)
with open(sys.argv[1], 'r') as f:
    # Read each line in the file
    lines = f.readlines()

# Iterate over each line in the file
for line in lines:
    # Strip the line to remove any extra whitespace or newline characters
    old_file = line.strip()

    # Replace 'jane' with 'jdoe' in the file name
    new_file = old_file.replace('jane', 'jdoe')

    # Use subprocess to run the mv command to rename the file
    try:
        subprocess.run(["mv", old_file, new_file], check=True)
        print(f"Renamed {old_file} to {new_file}")
    except subprocess.CalledProcessError:
        print(f"Error renaming {old_file}")