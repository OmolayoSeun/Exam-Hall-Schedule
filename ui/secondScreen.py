from tkinter import ttk
from tkinter.ttk import *
from tools.Configure import *
from resources import Variables as v

def secondScreen(frame):
    configLabel(Label(frame, text="Constraints ")).grid(row=0, column=0, sticky="w", padx=5)

    configLabel(Label(frame, text="Maximum Exam Per Day: ", anchor='w')).grid(row=2, column=0, columnspan=2,
                                                                              sticky="w", padx=5)
    configLabel(Label(frame, text="Maximum Exam Per Week: ", anchor='w')).grid(row=4, column=0, columnspan=2,
                                                                               sticky="w", padx=5)
    maxDayEntry = ttk.Entry(frame, width=3)
    maxWeekEntry = ttk.Entry(frame, width=3)

    add_hint(maxDayEntry, "5")
    add_hint(maxWeekEntry, "9")

    v.maxDayEnt = maxDayEntry
    v.maxWeekEnt = maxWeekEntry

    maxDayEntry.grid(row=2, column=2, columnspan=1, ipady=5)
    maxWeekEntry.grid(row=4, column=2, columnspan=1, ipady=5)

    pass
