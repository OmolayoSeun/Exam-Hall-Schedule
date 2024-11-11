from tools.ClearContent import clear_content
from tools.Configure import *
from tkinter import ttk, filedialog
from resources.Variables import *
from constraint import *


class secondScreen:

    def display(self):

        frame = Frame(app)
        configFrame(frame)
        # ====================

        def update_loading_bar():
            # Define the bar width increment per frame
            increment = 5
            # Increase the width of the loading bar at intervals
            current_width = canvas.coords(loading_bar)[2]  # Current width of the bar
            if current_width < canvas_width:
                canvas.coords(loading_bar, 0, 0, current_width + increment, bar_height)
                # Schedule the next update
                frame.after(50, update_loading_bar)  # Adjust the time interval to control the speed
            else:
                # Reset the bar for continuous loading effect
                canvas.coords(loading_bar, 0, 0, 0, bar_height)
                frame.after(50, update_loading_bar)  # Restart loading


        # Define dimensions
        canvas_width = 300
        bar_height = 30

        # Create a canvas to draw the loading bar
        canvas = tk.Canvas(frame, width=canvas_width, height=bar_height, bg="lightgrey")
        canvas.pack(pady=20)

        # Create a rectangle on the canvas for the loading bar
        loading_bar = canvas.create_rectangle(0, 0, 0, bar_height, fill="blue")

        # Start the loading animation
        update_loading_bar()

        # Run the Tkinter event loop
        frame.mainloop()

        # =====================
        frame.update_idletasks()
        cenX = (x - frame.winfo_reqwidth()) // 2
        cenY = ((y - frame.winfo_reqheight()) // 2)

        frame.place(x=cenX, y=cenY)