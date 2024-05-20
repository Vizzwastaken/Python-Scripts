import os
folderlist = input("Please enter the folder paths : ").split(" ") # user enters the list of folder paths
for folder in folderlist:
    try:
        if os.path.exists(folder):
            for dirpath, subdir, files in os.walk(folder): #dirpath=Directory path , subdir=sub dir under the dir, files = files in each dir
                print("Directory :" + dirpath)
                for name in files:
                    print(name)
        else:
            print(folder + " Doesnt exist")
    except PermissionError:
        print("Permission denied to " + folder)
        break