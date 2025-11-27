import os
import shutil

def organize_files(folder):
    file_types = {
        "Images": [".jpg", ".jpeg", ".png"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mov"],
        "Music": [".mp3"],
        "Archives": [".zip", ".rar"],
    }

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()

            moved = False
            for folder_name, extensions in file_types.items():
                if ext in extensions:
                    target_folder = os.path.join(folder, folder_name)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, target_folder)
                    moved = True
                    break

            if not moved:
                others = os.path.join(folder, "Others")
                os.makedirs(others, exist_ok=True)
                shutil.move(file_path, others)

if __name__ == "__main__":
    folder_path = input("Enter folder path: ")
    organize_files(folder_path)
    print("Files organized successfully!")
