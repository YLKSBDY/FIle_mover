import os
import shutil
import tkinter as tk
from tkinter import filedialog

# Function to move files
def move_files():
    source_dir = source_entry.get()
    dest_dir = dest_entry.get()

    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Iterate through all files in all subdirectories
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Construct the full path of the source file
            source_file = os.path.join(root, file)
            
            # Construct the full path of the destination file
            dest_file = os.path.join(dest_dir, file)
            
            # Move the file to the destination directory
            try:
                shutil.move(source_file, dest_file)
                print(f"Moved {source_file} to {dest_file}")
            except shutil.Error as e:
                print(f"Error moving {source_file}: {e}")

    status_label.config(text="Files moved successfully!")

# Function to open file dialog for source directory
def choose_source_dir():
    source_dir = filedialog.askdirectory()
    source_entry.delete(0, tk.END)
    source_entry.insert(0, source_dir)

# Function to open file dialog for destination directory
def choose_dest_dir():
    dest_dir = filedialog.askdirectory()
    dest_entry.delete(0, tk.END)
    dest_entry.insert(0, dest_dir)

# Create the main window
root = tk.Tk()
root.title("File Mover")

# Create the GUI elements
source_label = tk.Label(root, text="Source Directory:")
source_label.grid(row=0, column=0, padx=10, pady=10)

source_entry = tk.Entry(root)
source_entry.grid(row=0, column=1, padx=10, pady=10)

source_button = tk.Button(root, text="...", command=choose_source_dir)
source_button.grid(row=0, column=2, padx=10, pady=10)

dest_label = tk.Label(root, text="Destination Directory:")
dest_label.grid(row=1, column=0, padx=10, pady=10)

dest_entry = tk.Entry(root)
dest_entry.grid(row=1, column=1, padx=10, pady=10)

dest_button = tk.Button(root, text="...", command=choose_dest_dir)
dest_button.grid(row=1, column=2, padx=10, pady=10)

move_button = tk.Button(root, text="Move Files", command=move_files)
move_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

status_label = tk.Label(root, text="")
status_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Start the main event loop
root.mainloop()