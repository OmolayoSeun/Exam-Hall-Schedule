import json
import tkinter as tk
from resources import Variables as v

courseListJson = None
hallListJson = None
availableSlotJson = None
maxPerDay = 0
maxPerWeek = 0


def append_log(text, colorB):
    v.logs.config(state="normal")
    start_index = v.logs.index(tk.END)
    v.logs.insert(tk.END, text + "\n")
    end_index = v.logs.index(tk.END)

    v.logs.tag_add(colorB, start_index, end_index)
    v.logs.tag_config(colorB, foreground=colorB)

    v.logs.config(state="disabled")
    v.logs.see(tk.END)


def getFiles(courseFilePath: str, hallFilePath: str, availableSlotFilePath: str):
    global courseListJson, hallListJson, availableSlotJson
    try:
        append_log("Reading course file... ", "black")
        with open(courseFilePath, "r") as file:
            courseListJson = json.load(file)
    except FileNotFoundError as e:
        append_log("Error: " + str(e), "red")
        return False
    try:
        append_log("Reading course file... ", "black")
        with open(hallFilePath, 'r') as file:
            hallListJson = json.load(file)
    except FileNotFoundError as e:
        append_log("Error: " + str(e), "red")
        return False
    try:
        append_log("Reading course file... ", "black")
        with open(availableSlotFilePath, 'r') as file:
            v.availableSlotJson = json.load(file)
    except FileNotFoundError as e:
        append_log("Error: " + str(e), "red")
        return False
    return True


def getConstraints():
    global maxPerDay, maxPerWeek
    maxPerDay = int(v.maxDayEnt.get())
    maxPerWeek = int(v.maxWeekEnt.get())
    print(maxPerDay)
    print(maxPerWeek)
    pass


def printOutput():
    for item in v.outputList:
        v.outputList.insert(tk.END, item)
    pass


def startProcess():
    if not getFiles(v.courseEnt.get(), v.hallEnt.get(), v.slotEnt.get()):
        append_log("Operation terminated", "red")
    getConstraints()


    pass
