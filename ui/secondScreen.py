from tools.ClearContent import clear_content
from tools.Configure import *
from tkinter import ttk, filedialog
from resources.Variables import *


class secondScreen:

    def display(self):

        frame = Frame(app)
        configFrame(frame)



        def on_check():
            # This function will be called whenever a checkbox is clicked
            checked_items = [item.get() for item in checkbox_vars if item.get()]
            print(f"Checked items: {checked_items}")
        # Sample list of items
        items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

        # Create the main window
        # root = tk.Tk()
        # root.title("Item List with Checkboxes")

        # Create a frame to hold the list of items and checkboxes
        # frame = ttk.Frame(root, padding="10")
        # frame.pack(fill=tk.BOTH, expand=True)

        # Create a list to hold the variables associated with each checkbox
        checkbox_vars = []

        # Loop through the list of items and create a label and a checkbox for each
        for item in items:
        # Create a label for the item
            label = ttk.Label(frame, text=item)
            label.pack(side=tk.TOP, anchor='w', pady=2)

        # Create a variable to track the checkbox state (checked/unchecked)
        var = tk.StringVar(value="")

        # Create the checkbox and associate it with the variable
        checkbox = ttk.Checkbutton(frame, variable=var, text="")
        checkbox.pack(side=tk.TOP, anchor='e', pady=2)
        checkbox_vars.append(var)

        # Bind the checkbox to call `on_check` when clicked
        checkbox.config(command=on_check)

        frame.update_idletasks()
        cenX = (x - frame.winfo_reqwidth()) // 2
        cenY = ((y - frame.winfo_reqheight()) // 2)

        frame.place(x=cenX, y=cenY)