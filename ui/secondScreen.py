from tools.ClearContent import clear_content
from tools.Configure import *
from tkinter import ttk, filedialog
from resources.Variables import *
from constraint import *


class secondScreen:

    def display(self):

        frame = Frame(app)
        configFrame(frame)




        frame.update_idletasks()
        cenX = (x - frame.winfo_reqwidth()) // 2
        cenY = ((y - frame.winfo_reqheight()) // 2)

        frame.place(x=cenX, y=cenY)