import os

current_directory = os.getcwd()
folder = current_directory
for dirpath, subdir, files in os.walk(folder):
    if dirpath != '.':
        print(dirpath)
        os.chdir(dirpath)
        for name in files:
            command1 = f"chmod +x {name}"
            os.system(command1)
            exec = f"python {name}"
            os.system(exec)
        command2 = "ls -lrt"
        os.system(command2)
