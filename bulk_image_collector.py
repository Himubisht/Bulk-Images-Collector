import os
import shutil

# Path where all folders exist
source_main_folder = r"Main Folder"

# Path to new folder where all images will be collected
destination_folder = r"Data"

# Create destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Loop through each folder inside main folder
for folder_name in os.listdir(source_main_folder):
    folder_path = os.path.join(source_main_folder, folder_name)

    # Check if it is a folder
    if os.path.isdir(folder_path):
        # Loop through files inside folder
        for file_name in os.listdir(folder_path):
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                source_file = os.path.join(folder_path, file_name)
                destination_file = os.path.join(destination_folder, file_name)

                shutil.copy(source_file, destination_file)

print("All images copied successfully!")
