from tkinter import ttk, filedialog
from resources import Variables as v
from tools.Configure import *
from ui.controller import startProcess

def open_file(textView: Entry):
    file_path = filedialog.askopenfilename(
        title="Open File",
        filetypes=[("Json files", "*.json"), ("All files", "*.*")]
    )
    if file_path:
        textView.delete(0, tk.END)
        textView.insert(0, file_path)
        textView.configure(foreground="black")

def firstScreen(frame):
    configLabel(Label(frame, text="Inputs", anchor='w')).grid(row=0, column=0, sticky="w", padx=5)
    configLabel(Label(frame, text="Course Data: ", anchor='w')).grid(row=1, column=0, sticky="w", padx=5)
    configLabel(Label(frame, text="Hall Data: ")).grid(row=3, column=0, sticky="w", padx=5)
    configLabel(Label(frame, text="Available Slots: ")).grid(row=5, column=0, sticky="w", padx=5)
    configLabel(Label(frame, text="", anchor='w')).grid(row=1, column=4, sticky="w", padx=5)

    Label(frame, font=('ariel', '5', 'normal'), bg=color.white).grid(row=2, column=1)
    Label(frame, font=('ariel', '5', 'normal'), bg=color.white).grid(row=4, column=1)
    Label(frame, font=('ariel', '5', 'normal'), bg=color.white).grid(row=6, column=1)
    Label(frame, font=('ariel', '5', 'normal'), bg=color.white).grid(row=8, column=1)
    Label(frame, font=('ariel', '5', 'normal'), bg=color.white).grid(row=10, column=1)

    courseEntry = ttk.Entry(frame, width=35)
    hallEntry = ttk.Entry(frame, width=35)
    availableSlotsEntry = ttk.Entry(frame, width=35)

    btn1 = Button(frame, text="+", padx=10, command=lambda: open_file(courseEntry))
    btn2 = Button(frame, text="+", padx=10, command=lambda: open_file(hallEntry))
    btn3 = Button(frame, text="+", padx=10, command=lambda: open_file(availableSlotsEntry))

    configButton(btn1)
    configButton(btn2)
    configButton(btn3)

    add_hint(courseEntry, "Paste file address here...")
    add_hint(hallEntry, "Paste file address here...")
    add_hint(availableSlotsEntry, "Paste file address here...")

    courseEntry.grid(row=1, column=1, columnspan=3, ipady=5)
    hallEntry.grid(row=3, column=1, columnspan=3, ipady=5)
    availableSlotsEntry.grid(row=5, column=1, columnspan=3, ipady=5)

    btn1.grid(row=1, column=5, columnspan=1, sticky='nswe')
    btn2.grid(row=3, column=5, columnspan=1, sticky='nswe')
    btn3.grid(row=5, column=5, columnspan=1, sticky='nswe')

    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.columnconfigure(3, weight=1)
    frame.columnconfigure(4, weight=1)
    frame.columnconfigure(5, weight=1)
    frame.rowconfigure(7, weight=1)

    v.courseEnt = courseEntry
    v.hallEnt = hallEntry
    v.slotEnt = availableSlotsEntry

    bottom_right_button = Button(frame, text="Start", command=lambda: startProcess())
    configButton(bottom_right_button)
    bottom_right_button.grid(row=8, column=6, sticky="se", padx=5, pady=0)
