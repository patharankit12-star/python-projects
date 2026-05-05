# use os modules and first create folder in rendoms file and after change its name squnce wise 1.png,2.png ,3.png

import os

# Create a folder named "my_folder" if it doesn't exist
folder_name = "my_folder"
os.makedirs(folder_name, exist_ok=True)

# Create 15 files inside the folder
for i in range(1, 16):  # from 1 to 15
    file_path = os.path.join(folder_name , f"file_{i}.txt")
    with open(file_path, "w") as f:
        f.write(f"This is file number {i}")
    print(f"Created: {file_path}")
