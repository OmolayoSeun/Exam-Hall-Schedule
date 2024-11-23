from tkinter import ttk
from tkinter.ttk import *
from tools.Configure import *


def button_click(courseFilePath: str, hallFilePath: str, availableSlotFilePath: str, frame):
    # First check if all entries are proper
    # TODO Open later
    #
    # if courseFilePath:
    #     with open(courseFilePath, "r") as file:
    #         v.courseListJson = json.load(file)
    # if hallFilePath:
    #     with open(hallFilePath, 'r') as file:
    #         v.hallListJson = json.load(file)
    # if availableSlotFilePath:
    #     with open(availableSlotFilePath, 'r') as file:
    #         v.availableSlotJson = json.load(file)
    #
    # print(v.courseListJson)
    # print(v.hallListJson)
    # print(v.availableSlotJson)

    # Display second page
    pass


def secondScreen(frame):
    configLabel(Label(frame, text="Constraints ")).grid(row=0, column=0, sticky="w")

    configLabel(Label(frame, text="Maximum Exam Per Day: ", anchor='w')).grid(row=2, column=0, columnspan=2,
                                                                              sticky="w")
    configLabel(Label(frame, text="Maximum Exam Per Week: ", anchor='w')).grid(row=4, column=0, columnspan=2,
                                                                               sticky="w")
    maxDayEntry = ttk.Entry(frame, width=3)
    maxWeekEntry = ttk.Entry(frame, width=3)


    add_hint(maxDayEntry, "5")
    add_hint(maxWeekEntry, "9")

    maxDayEntry.grid(row=2, column=2, columnspan=1, ipady=5)
    maxWeekEntry.grid(row=4, column=2, columnspan=1, ipady=5)

    pass
