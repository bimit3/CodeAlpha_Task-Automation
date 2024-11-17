import os
import shutil

directory_to_organize = "C:/Users/Dell/OneDrive/Documents/Contents"

file_categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Documents': ['.pdf', '.docx', '.xlsx', '.pptx', '.txt'],
    'Music': ['.mp3', '.wav', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Others': []
}

def organize_files(directory):
    files_in_directory = os.listdir(directory)

    for file in files_in_directory:
        file_path = os.path.join(directory, file)

        if os.path.isdir(file_path):
            continue

        file_extension = os.path.splitext(file)[1].lower()

        moved = False
        for category, extensions in file_categories.items():
            if file_extension in extensions:
                category_folder = os.path.join(directory, category)
                if not os.path.exists(category_folder):
                    os.mkdir(category_folder)  
                shutil.move(file_path, os.path.join(category_folder, file))  
                print(f"Moved {file} to {category}")
                moved = True
                break

        if not moved:
            others_folder = os.path.join(directory, 'Others')
            if not os.path.exists(others_folder):
                os.mkdir(others_folder)  
            shutil.move(file_path, os.path.join(others_folder, file))
            print(f"Moved {file} to Others")

organize_files(directory_to_organize)
