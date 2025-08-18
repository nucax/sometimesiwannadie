import os

prefix = "sometimesiwannadie"
counter = 1

script_folder = os.path.dirname(os.path.abspath(__file__))

with open("folders.txt", "r") as f:
    folders_to_rename = [line.strip() for line in f if line.strip()]

for folder in folders_to_rename:
    if os.path.abspath(folder) == script_folder:
        continue

    if os.path.exists(folder):
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            
            if os.path.isfile(file_path):
                ext = os.path.splitext(filename)[1]
                new_name = f"{prefix}{counter}{ext}"
                new_path = os.path.join(folder, new_name)
                os.rename(file_path, new_path)
                counter += 1
