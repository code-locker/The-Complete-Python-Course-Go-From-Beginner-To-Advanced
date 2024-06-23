# File read and write example
# This file should be created manually
file_path = "example.txt"
  
try: 
    with open(file_path, 'w') as file: 
        file.write("Hello, Geeks!") 
    file.close()
except FileExistsError: 
    print(f"The file '{file_path}' already exists.") 

file_path = "example1.txt"
file = open(file_path, 'x')
file.writelines(["Hello, Geeks!\n", "I am back"]) 
file.close()
file = open(file_path, 'r')
print(file.read())
file.close()