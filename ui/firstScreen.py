# from resources.Variables import Variables as v
from tools.ClearContent import clear_content
from tools.Configure import *
from tkinter import ttk, filedialog
from resources.Variables import Variables as v


def open_file(textView: Entry):
    file_path = filedialog.askopenfilename(
        title="Open File",
        filetypes=[("Json files", "*.json"), ("All files", "*.*")]
    )
    if file_path:
        textView.delete(0, tk.END)
        textView.insert(0, file_path)
        textView.configure(foreground="black")


def button_click(courseFilePath: str, hallFilePath: str, availableSlotFilePath: str):
    if courseFilePath:
        with open(courseFilePath, "r") as file:
            v.courseListJson = file.read()
    if hallFilePath:
        with open(hallFilePath, 'r') as file:
            v.hallListJson = file.read()
    if availableSlotFilePath:
        with open(availableSlotFilePath, 'r') as file:
            v.availableSlotJson = file.read()

    print(v.courseListJson)
    print(v.hallListJson)
    print(v.availableSlotJson)



# This page display the first interface
class firstScreen:

    def display(self, x, y):
        clear_content()
        frame = Frame(self)
        configFrame(frame)

        # v.holdFrameReference = frame
        # v.app.update_idletasks()

        configLabel(Label(frame, text="Course Data: ", anchor='w')).grid(row=0, column=0, sticky="w")
        configLabel(Label(frame, text="Hall Data: ")).grid(row=2, column=0, sticky="w")
        configLabel(Label(frame, text="Available Slots: ")).grid(row=4, column=0, sticky="w")
        configLabel(Label(frame, text="", anchor='w')).grid(row=0, column=4, sticky="w")

        Label(frame, font=('ariel', '5', 'normal'), bg=color.white).grid(row=1, column=1)
        Label(frame, font=('ariel', '5', 'normal'), bg=color.white).grid(row=3, column=1)
        Label(frame, font=('ariel', '5', 'normal'), bg=color.white).grid(row=5, column=1)

        courseEntry = ttk.Entry(frame, width=35)
        hallEntry = ttk.Entry(frame, width=35)
        availableSlotsEntry = ttk.Entry(frame, width=35)

        btn1 = Button(frame, text="+", padx=10, command=lambda: open_file(courseEntry))
        btn2 = Button(frame, text="+", padx=10, command=lambda: open_file(hallEntry))
        btn3 = Button(frame, text="+", padx=10, command=lambda: open_file(availableSlotsEntry))

        btn4 = Button(frame, text=">> Proceed >>", padx=10, command=lambda:
        button_click(courseEntry.get(), hallEntry.get(), availableSlotsEntry.get()))

        configButton(btn1)
        configButton(btn2)
        configButton(btn3)
        configButton(btn4)

        add_hint(courseEntry, "Paste file address here...")
        add_hint(hallEntry, "Paste file address here...")
        add_hint(availableSlotsEntry, "Paste file address here...")

        courseEntry.grid(row=0, column=1, columnspan=3, ipady=5)
        hallEntry.grid(row=2, column=1, columnspan=3, ipady=5)
        availableSlotsEntry.grid(row=4, column=1, columnspan=3, ipady=5)
        btn1.grid(row=0, column=5, columnspan=1, sticky='nswe')
        btn2.grid(row=2, column=5, columnspan=1, sticky='nswe')
        btn3.grid(row=4, column=5, columnspan=1, sticky='nswe')
        btn4.grid(row=5, column=0, columnspan=6, pady=10, sticky='nswe')

        self.update_idletasks()
        cenX = (x - frame.winfo_reqwidth()) // 2
        cenY = ((y - frame.winfo_reqheight()) // 2)

        frame.place(x=cenX, y=cenY)
