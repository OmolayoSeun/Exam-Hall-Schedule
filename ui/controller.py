import copy
import json
import tkinter as tk
from pathlib import Path

from resources import Variables as v

courseListJson = {}
hallListJson = {}
availableSlotJson = {}
maxPerDay = 0
maxPerWeek = 0

listOfCourse = []
deptExams = []
levelExams = []
levelExamCourseUnit = []
aliasExams = []

examDomain = []
examSolution = {}

makeDict = {}


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
            availableSlotJson = json.load(file)
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
    fileList = list(Path("").glob("*.docx"))
    print(fileList)

    count = 0
    for item in fileList:
        v.outputList.insert(count, item)
        count = count + 1
    pass

def checkForAlias(a, b):
    if a is None:
        return [False, 0]
    else:
        for i in range(len(a)):
            if b in a[i]:
                return [True, i]
        else:
            return [False, 0]


def refineData():
    global courseListJson

    for level in courseListJson.values():
        deptList = []
        for courses in level.values():
            lvlList = []
            lvlListUnit = []
            for courseCode, courseInfo in courses.items():
                if courseInfo[2] == "General":
                    result = checkForAlias(aliasExams, courseCode)
                    if result[0]:
                        courseCode = copy.deepcopy(aliasExams[result[1]][-1] + 'x')
                        aliasExams[result[1]].append(courseCode)

                    else:
                        aliasExams.append([courseCode])
                elif courseInfo[2] != "None":
                    result = checkForAlias(aliasExams, courseInfo[2])
                    if result[0]:
                        aliasExams[result[1]].append(courseCode)
                    else:
                        aliasExams.append([courseInfo[2], courseCode])
                deptList.append(courseCode)
                lvlList.append(courseCode)
                lvlListUnit.append(courseInfo[1])
                makeDict[courseCode] = courseInfo

            levelExams.append(lvlList)
            levelExamCourseUnit.append(lvlListUnit)
        deptExams.append(deptList)


def startProcess():
    printOutput()
    return
    global hallListJson, availableSlotJson
    if not getFiles(v.courseEnt.get(), v.hallEnt.get(), v.slotEnt.get()):
        append_log("Operation terminated", "red")
        return
    getConstraints()

    append_log("Refining data...", "black")
    refineData()

    append_log("Initializing CSP solver...", "black")

    import CSPSolver.csp as c

    for name, info in makeDict.items():
        listOfCourse.append(c.Variable(name, info))

    hall = c.Hall(hallListJson)
    allocation = c.Allocation(availableSlotJson)

    domain = c.Domain(allocation, hall)
    constraints = c.Constraints(5, 9, levelExams, deptExams, aliasExams)

    cspSolution = c.CSP(listOfCourse, domain, constraints, makeDict)

    append_log("CSP Operation started...", "black")
    sol = cspSolution.getSolution()

    import CSPSolver.createDoc as create
    if sol:
        append_log("Creating docx file...", "black")
        doc = create.CreateDocument(sol, domain.dayCount, domain.slotCount)
        doc.create()
        append_log("Successful", "green")
        printOutput()

    else:
        append_log("Operation terminated, No feasible solution", "red")

    pass
