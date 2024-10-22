from tools.ClearContent import clear_content
from tools.Configure import *
from tkinter import ttk, filedialog
from resources.Variables import Variables as v

class secondScreen:

    def display(self,):
        clear_content()
        frame = Frame(self)
        configFrame(frame)

        # v.holdFrameReference = frame
        # v.app.update_idletasks()




        self.update_idletasks()
        cenX = (v.x - frame.winfo_reqwidth()) // 2
        cenY = ((v.y - frame.winfo_reqheight()) // 2)

        frame.place(x=cenX, y=cenY)