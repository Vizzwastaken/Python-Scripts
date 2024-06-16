def file_edit(file, key, value):
    # Open the file in read mode
    with open(file, 'r') as content:
        # Read all the lines of the file
        lines = content.readlines()
        # Iterate through each line and its index
        for i, line in enumerate(lines):
            # Check if the key is present in the line
            if key in line:
                # Extract the indentation from the line
                indentation = line.split(key)[0]
                # Replace the value associated with the key in the line
                lines[i] = f"{indentation}{key} = \"{value}\" \n"
                # Exit the loop after updating the value
                break

    # Open the file in write mode to update its content
    with open(file, 'w') as content:
        # Write the updated lines back to the file
        content.writelines(lines)


file  = input("Enter the file path: ")
key   = input("Enter the key to change: ")
value = input("Enter the value to update: ")

# Call the file_edit function with the provided inputs
file_edit(file, key, value)
