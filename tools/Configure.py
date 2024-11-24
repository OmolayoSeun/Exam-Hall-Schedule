from tkinter import Frame, Button, Entry, Label
from resources.Colors import Color as color
import tkinter as tk
textSize = '10'

def configFrame(frame: Frame):
    frame.config(
        background=color.white
    )
    pass

def configLabel(item: Label):
    item.config(
        background=color.white, foreground=color.grey,
        font=('ariel', textSize, 'normal')
    )
    return item

def configEntry(item: Entry):
    item.config(border=1, background=color.white)

def configButton(item: Button):
    configDefBtn(item)

def configDefBtn(item: Button):
    def on_enter(event):
        item.config(bg=color.skyBlueHighlight, highlightcolor=color.green) 

    def on_leave(event):
        item.config(bg=color.skyBlue, highlightcolor=color.green)

    item.config(
        background=color.skyBlue, foreground=color.white,
        activebackground=color.green, activeforeground=color.white,
        highlightthickness=2, highlightbackground=color.green, highlightcolor=color.green,
        cursor="hand2", border=0, height=1, font=('ariel', textSize, 'bold')
    )
    item.bind('<Enter>', on_enter)
    item.bind('<Leave>', on_leave)
    return item

def configDeleteBtn(item: Button):
    def on_enter(event):
        item.config(bg=color.redHighlight, highlightcolor=color.white)

    def on_leave(event):
        item.config(bg=color.red, highlightcolor=color.white)

    item.config(
        background=color.red, foreground=color.white,
        activebackground=color.green, activeforeground=color.white,
        highlightthickness=2, highlightbackground=color.green, highlightcolor=color.green,
        cursor="hand2", border=0, height=1, font=('ariel', textSize, 'bold')
    )
    item.bind('<Enter>', on_enter)
    item.bind('<Leave>', on_leave)

def add_hint(entry, hint_text):
    def on_entry_click(event):
        if entry.get() == hint_text:
            entry.delete(0, tk.END)
            entry.configure(foreground='black', font=('ariel', textSize, "normal"))

    def on_focusout(event):
        if entry.get() == '':
            entry.insert(0, hint_text)
            entry.configure(foreground='grey', font=('ariel', textSize, "normal"))

    entry.insert(0, hint_text)
    entry.configure(foreground='grey', font=('ariel', textSize, "normal"))
    entry.bind('<FocusIn>', on_entry_click)
    entry.bind('<FocusOut>', on_focusout)
