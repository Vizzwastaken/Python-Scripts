import os

# Get the current working directory
current_directory = os.getcwd()
print(current_directory)
# Store the current directory in a variable for clarity
folder = current_directory

# Traverse through all directories and files starting from 'folder'
for dirpath, subdir, files in os.walk(folder):
    print(dirpath)
    # Print the current directory path
    if dirpath != current_directory:
        print(dirpath)
        
        # Change the current working directory to 'dirpath'
        os.chdir(dirpath)
        
        # Iterate over each file in the current directory
        for name in files:
            # Set the command to change file permissions to executable (+x)
            command1 = f"chmod +x {name}"
            
            # Execute the command to change file permissions
            os.system(command1)
            
            # Set the command to execute the Python script
            exec_command = f"python {name}"
            
            # Execute the Python script
            os.system(exec_command)
        
        # After processing files, list files in long format (sorted by time) in the current directory
        command2 = "ls -lrt"
        os.system(command2)

