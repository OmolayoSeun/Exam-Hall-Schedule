import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(
        title="Open File",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            # Do something with the file content here
            print(content)

root = tk.Tk()

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a file menu
file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add an "Open" menu item
file_menu.add_command(label="Open", command=open_file)

# Start the tkinter event loop
root.mainloop()

{
    "day1": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day2": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day3": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day4": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day5": [
        "8:00 - 10:30",
        "2:30 - 5:00"
    ],
    "day6": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day7": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day8": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day9": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day10": [
        "8:00 - 10:30",
        "2:30 - 5:00"
    ],
    "day11": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day12": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day13": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day14": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day15": [
        "8:00 - 10:30",
        "2:30 - 5:00"
    ],
    "day16": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day17": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day18": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day19": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day20": [
        "8:00 - 10:30",
        "2:30 - 5:00"
    ]
}