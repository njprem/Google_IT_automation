#!/bin/bash

# Clear the oldFiles.txt file to start fresh
> oldFiles.txt

# Define the directory to check
directory="/Users/nj.prem/OneDrive - King Mongkut’s University of Technology Thonburi (KMUTT)/google it automation python/python_interact_with_OS/Python_Bash/bash_project"

# Check if the directory exists
if test -d "$directory"; then
    # Loop through all files in the directory
    for file in "$directory"/*; do
        # Check if the file exists and contains 'jane' but not 'janez'
        if test -e "$file" && echo "$file" | grep -q "jane" && ! echo "$file" | grep -q "janez"; then
            # Add the full path to oldFiles.txt
            echo "$file" >> oldFiles.txt
        fi
    done
else
    echo "Directory does not exist: $directory"
fi