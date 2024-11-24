import os
from pathlib import Path
from tkinter import messagebox
from tkinter.ttk import *
from resources import Variables as v
from tools.Configure import *

def thirdScreen(frame):
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=0)
    frame.rowconfigure(1, weight=1)

    def on_item_click(event):
        selected_index = listbox.curselection()
        if selected_index:
            selected_text = listbox.get(selected_index)
            os.startfile(selected_text)
            # messagebox.showinfo("Item Clicked", f"You selected: {selected_text}")

    label = Label(frame, text="Outputs", anchor='w')
    label = configLabel(label)
    label.grid(row=0, column=0, sticky="ew")
    label.grid_propagate(False)

    listbox = tk.Listbox(frame, font=("Arial", 12), selectmode="single")
    listbox.grid(row=1, column=0, sticky="nswe", ipadx=5)

    v.outputList = listbox

    fileList = list(Path("").glob("*.docx"))

    count = 0
    for item in fileList:
        v.outputList.insert(count, item)
        count = count + 1

    listbox.bind("<<ListboxSelect>>", on_item_click)






