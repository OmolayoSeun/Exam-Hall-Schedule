import tkinter
from tkinter import *
from tkinter import ttk
from ui.firstScreen import firstScreen
from resources.Variables import *
from resources.Variables import SCREEN

x = 1100
y = 700

class RootUI:

    def __init__(self):
        global app
        app = Tk()
        app.title("Exam Hall Scheduling")
        app.geometry("1100x700")
        app.resizable(width=False, height=False)
        app.config(background="white")


    @staticmethod
    def run():
        global app
        firstScreen.display(app)
        app.mainloop()
