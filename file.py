import os
import shutil

folder_path = r'C:\Your\Folder\Path' 
types = {
    'Images': ['.jpg', '.png'],
    'Docs': ['.pdf', '.txt'],
    'Code': ['.py', '.html'],
    'Others': []
}

for name in types:
    os.makedirs(os.path.join(folder_path, name), exist_ok=True)

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

if os.path.isfile(file_path):
        ext = os.path.splitext(file)[1].lower()
        moved = False

        for folder, extensions in types.items():
            if ext in extensions:
                shutil.move(file_path, os.path.join(folder_path, folder, file))
                moved = True
                break
        if not moved:
            shutil.move(file_path, os.path.join(folder_path, 'Others', file))
            
print("Files organized successfully!")
