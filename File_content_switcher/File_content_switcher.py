import os
import tkinter as tk
from tkinter import filedialog, messagebox


def replace_content(root_file, new_file):
    with open(root_file, 'r') as root_file_obj:
        root_content = root_file_obj.read()
    with open(new_file, 'r') as new_file_obj:
        new_content = new_file_obj.read()
    with open(root_file, 'w') as root_file_obj:
        root_file_obj.write(new_content)
    with open(new_file, 'w') as new_file_obj:
        new_file_obj.write(root_content)


def check_and_replace_files():
    root_directory = root_dir_entry.get()
    new_directory = new_dir_entry.get()

    root_files = os.listdir(root_directory)
    new_files = os.listdir(new_directory)
    common_files = set(root_files).intersection(new_files)

    for file_name in common_files:
        root_file = os.path.join(root_directory, file_name)
        new_file = os.path.join(new_directory, file_name)
        replace_content(root_file, new_file)
        print(root_file, new_file)

    messagebox.showinfo("Success", "Operation completed successfully!")


def browse_root_directory():
    directory = filedialog.askdirectory()
    root_dir_entry.delete(0, tk.END)
    root_dir_entry.insert(tk.END, directory)


def browse_new_directory():
    directory = filedialog.askdirectory()
    new_dir_entry.delete(0, tk.END)
    new_dir_entry.insert(tk.END, directory)


# Create the main window
window = tk.Tk()
window.title("File Content Switcher by Mehmet Ugurlu")
window.configure(background="#011f4b")  # Set the background color

# Calculate the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the window width and height
window_width = 450
window_height = 130

# Calculate the x and y coordinates for the window to be centered
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the window geometry
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create and position the input fields
root_dir_label = tk.Label(window, text="Root Directory:", bg="#011f4b", fg="white")
root_dir_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

root_dir_entry = tk.Entry(window, width=40)
root_dir_entry.grid(row=0, column=1, padx=10, pady=5)

new_dir_label = tk.Label(window, text="New Directory:", bg="#011f4b", fg="white")
new_dir_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

new_dir_entry = tk.Entry(window, width=40)
new_dir_entry.grid(row=1, column=1, padx=10, pady=5)

# Create and position the browse buttons
root_dir_button = tk.Button(window, text="Browse", command=browse_root_directory)
root_dir_button.grid(row=0, column=2, padx=5, pady=5)

new_dir_button = tk.Button(window, text="Browse", command=browse_new_directory)
new_dir_button.grid(row=1, column=2, padx=5, pady=5)

# Create and position the process button
process_button = tk.Button(window, text="Process", command=check_and_replace_files)
process_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Start the GUI event loop
window.mainloop()


 