import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

from file_organizer import organize_folder


class FileOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python File Organizer")
        self.root.geometry("500x300")
        self.root.resizable(False, False)

        self.selected_folder: Path | None = None

        # Title
        title_label = tk.Label(
            root,
            text="Python File Organizer",
            font=("Segoe UI", 16, "bold")
        )
        title_label.pack(pady=10)

        # Folder display
        self.folder_label = tk.Label(
            root,
            text="No folder selected",
            wraplength=450,
            fg="gray"
        )
        self.folder_label.pack(pady=10)

        # Buttons
        select_button = tk.Button(
            root,
            text="Select Folder",
            width=20,
            command=self.choose_folder
        )
        select_button.pack(pady=5)

        organize_button = tk.Button(
            root,
            text="Organize Files",
            width=20,
            command=self.organize_files
        )
        organize_button.pack(pady=15)

        # Status
        self.status_label = tk.Label(root, text="", fg="green")
        self.status_label.pack(pady=5)

    def choose_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.selected_folder = Path(folder)
            self.folder_label.config(
                text=f"Selected folder:\n{folder}",
                fg="black"
            )
            self.status_label.config(text="")

    def organize_files(self):
        if not self.selected_folder:
            messagebox.showwarning(
                "No Folder Selected",
                "Please select a folder first."
            )
            return

        try:
            organize_folder(self.selected_folder)
            self.status_label.config(
                text="Files organized successfully!",
                fg="green"
            )
        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerApp(root)
    root.mainloop()
