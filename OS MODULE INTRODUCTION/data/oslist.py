import os
folders = os.listdir("data")

print(folders)

print(os.getcwd()) # show directsry
 #os.chdir("/Users") #change directary
print(os.getcwd())

'''for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))'''

with open("data/Tutorial85/Tutorial.md", "a") as file:
    file.write("Helloooo!")

with open("data/Tutorial85/Tutorial.md" , "r") as file:
    content=file.read()
    print(content)

    
    import os

# Yahan hum current directory (".") se shuru kar rahe hain
target_directory = "." 

print(f"--- Scanning Directory: {target_directory} ---\n")

for root_folder, sub_folders, files in os.walk(target_directory):
    for file in files:
        # Pura rasta (path) banakar print karna
        file_path = os.path.join(root_folder, file)
        print(f"Found File: {file_path}")
        
        # Advance: Agar aapko specific file dhoondhni ho (jaise passwords.txt)
        if file == "passwords.txt":
            print("🚨 ALERT: Sensitive file found! 🚨")


            import os

print("--- System Network Details ---\n")

# os.popen() command run karke uska output read karne deta hai
command_output = os.popen('ipconfig').read() 

# Output ko screen par print karna
print(command_output)


import os

print("--- Extracting Environment Variables ---\n")

# User profile ka path nikalna
user_profile = os.environ.get('USERPROFILE')
print(f"Target User Profile Path: {user_profile}")

# System ka naam nikalna
computer_name = os.environ.get('COMPUTERNAME')
print(f"Target Computer Name: {computer_name}")

import os

file_name = "main.py" # Apni file ka naam yahan dalein

if os.path.exists(file_name):
    # File ka size bytes mein check karna
    size = os.path.getsize(file_name)
    print(f"'{file_name}' ka size {size} bytes hai.")
else:
    print("File nahi mili!")