from tkinter import scrolledtext
from tkinter.ttk import *
from resources import Variables as v
from tools.Configure import *

def forthScreen(frame):
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=0)
    frame.rowconfigure(1, weight=1)

    label = Label(frame, text="Logs", anchor='w')
    label = configLabel(label)
    label.grid(row=0, column=0, sticky="ew")
    label.grid_propagate(False)

    log_widget = scrolledtext.ScrolledText(frame, wrap=tk.WORD, state="disabled", font=("Arial", 10))
    log_widget.grid(row=1, column=0, sticky="nswe")

    v.logs = log_widget
