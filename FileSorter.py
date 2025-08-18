import os
import shutil

# Path to the folder you want to sort
source_folder = '/path/to/folder'  # Example: r'C:\Users\YourName\Downloads'

# Extension-based folder rules
file_types = {
    'Images': ['.png', '.jpg', '.jpeg', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Code': ['.py', '.js', '.html', '.css'],
    'Archives': ['.zip', '.rar', '.7z'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Others': []  # as a fallback if not found
}

def get_folder(extension):
    for folder, extensions in file_types.items():
        if extension.lower() in extensions:
            return folder
    return 'Others'

for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    if os.path.isfile(file_path):
        ext = os.path.splitext(filename)[1]
        target_folder = get_folder(ext)
        target_path = os.path.join(source_folder, target_folder)

        os.makedirs(target_path, exist_ok=True)
        shutil.move(file_path, os.path.join(target_path, filename))
        print(f"Moved: {filename} → {target_folder}")
