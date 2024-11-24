import tkinter as tk
from ui.firstScreen import firstScreen
from ui.secondScreen import secondScreen
from ui.thirdScreen import thirdScreen
from ui.forthSCreen import forthScreen

def rootUI():
    # Create the main application window
    root = tk.Tk()
    root.title("Exam Hall Scheduling")
    root.geometry("900x600")

    root.rowconfigure([0, 1], weight=1, uniform="row")
    root.columnconfigure([0, 1], weight=1, uniform="col")

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

    firstScreen(frame_top_left)
    secondScreen(frame_bottom_left)
    thirdScreen(frame_top_right)
    forthScreen(frame_bottom_right)

    root.mainloop()


rootUI()
