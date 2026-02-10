from pathlib import Path
import shutil

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"]
}

TARGET_FOLDER = Path(r"C:\Personal\Learning\Test")

def organize_folder(target_folder: Path):
    # Check if folder exists
    if not target_folder.exists():
        raise FileNotFoundError("Folder does not exist")

    # List all files (ignore folders)
    files = [f for f in target_folder.iterdir() if f.is_file()]


    # Create category folders if they don't exist
    for folder_name in FILE_TYPES.keys():
        folder_path = target_folder / folder_name
        folder_path.mkdir(exist_ok=True)

    # Folder for uncategorized files
    others_folder = target_folder / "Others"
    others_folder.mkdir(exist_ok=True)

    def get_unique_destination(destination: Path) -> Path:
        if not destination.exists():
            return destination

        counter = 1
        while True:
            new_destination = destination.with_stem(
                f"{destination.stem}_{counter}"
            )
            if not new_destination.exists():
                return new_destination
            counter += 1


    # Move files to respective folders
    for file in files:
        moved = False
        file_extension = file.suffix.lower()

        for folder_name, extensions in FILE_TYPES.items():
            if file_extension in extensions:
                destination = target_folder / folder_name / file.name
                destination = get_unique_destination(destination)
                shutil.move(str(file), str(destination))
                moved = True
                break

        if not moved:
            destination = others_folder / file.name
            destination = get_unique_destination(destination)
            shutil.move(str(file), str(destination))


if __name__ == "__main__":
    organize_folder(TARGET_FOLDER)
