import tkinter as tk
from ui.firstScreen import firstScreen
from ui.secondScreen import  secondScreen
from ui.thirdScreen import thirdScreen

x = 1100
y = 700


def rootUI():
    # Create the main application window
    root = tk.Tk()
    root.title("Exam Hall Scheduling")
    root.geometry("900x600")  # Set the window size (width x height)

    root.rowconfigure([0, 1], weight=1, uniform="row")  # Divide into 2 rows
    root.columnconfigure([0, 1], weight=1, uniform="col")  # Divide into 2 columns

    # Create frames for each quadrant
    frame_top_left = tk.Frame(root, bg="white", borderwidth=2, relief="groove")
    frame_top_right = tk.Frame(root, bg="white", borderwidth=2, relief="groove")
    frame_bottom_left = tk.Frame(root, bg="white", borderwidth=2, relief="groove")
    frame_bottom_right = tk.Frame(root, bg="white", borderwidth=2, relief="groove")

    # Place the frames in the grid
    frame_top_left.grid(row=0, column=0, sticky="nsew")
    frame_top_right.grid(row=0, column=1, sticky="nsew")
    frame_bottom_left.grid(row=1, column=0, sticky="nsew")
    frame_bottom_right.grid(row=1, column=1, sticky="nsew")

    # tk.Label(frame_top_left, text="Top Left Frame").grid(row=0, column=0)
    # tk.Button(frame_top_left, text="Button 1").grid(row=1, column=0)
    firstScreen(frame_top_left)

    # tk.Label(frame_top_right, text="Top Right Frame").pack(pady=10)
    # tk.Button(frame_top_right, text="Button 2").pack(pady=5)
    thirdScreen(frame_top_right)

    # tk.Label(frame_bottom_left, text="Bottom Left Frame").pack(pady=10)
    # tk.Button(frame_bottom_left, text="Button 3").pack(pady=5)
    secondScreen(frame_bottom_left)

    tk.Label(frame_bottom_right, text="Bottom Right Frame").pack(pady=10)
    tk.Button(frame_bottom_right, text="Button 4").pack(pady=5)

    # Run the application
    root.mainloop()
rootUI()