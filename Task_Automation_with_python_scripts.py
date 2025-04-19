import os
import shutil

def organize_files(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            ext = file.split('.')[-1]
            target_folder = os.path.join(folder_path, ext.upper())
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, target_folder)
    print("Files organized successfully!")


organize_files("path_to_your_folder")