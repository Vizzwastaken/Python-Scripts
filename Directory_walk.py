import os
# Prompting user to input folder paths and splitting into a list
folderlist = input("Please enter the folder paths: ").split(" ")
# Iterating over each folder path provided
for folder in folderlist:
    try:
        if os.path.exists(folder):  # Checking if folder exists
            # Walking through directory tree and printing file names
            for dirpath, subdir, files in os.walk(folder):
                print("Directory: " + dirpath)
                for name in files:
                    print(name)
        else:
            print(folder + " doesn't exist")  # If folder doesn't exist
    except PermissionError:
        print("Permission denied to " + folder)  # Handling permission errors
        break  # Exiting loop if permission denied to any folder
