import os
import shutil

def move_mp3_files(source_directory, target_directory=r"C:\Users\thesa\Documents\songs\song_files"):
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    
    for file in os.listdir(source_directory):
        if file.endswith(".mp3"):
            file_path = os.path.join(source_directory, file)
            shutil.move(file_path, target_directory)
            print(f"Moved: {file}")

move_mp3_files(r"C:\Users\thesa\Documents\songs")
