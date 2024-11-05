from resources import Variables as v
from constraint import *

# def open_file():
#     with open("", "r") as file:
#         v.courseListJson = json.load(file)

v.courseListJson = {
    "Chemistry": {
        "100 level": {
            "CHM112": [80, 3, "General"],
            "CHM111": [80, 3, "None"],
            "MTH112": [80, 3, "None"],
            "MTH111": [80, 3, "General"],
            "BIO111": [80, 3, "General"],
            "CSC111": [80, 3, "General"],
            "PHY111": [80, 3, "General"],
            "GSE111": [80, 3, "General"],
            "GSE112": [80, 3, "General"]
        },
        "200 level": {
            "CHM211": [80, 3, "None"],
            "CHM212": [80, 3, "None"],
            "CHM213": [80, 3, "None"],
            "CHM214": [80, 3, "None"],
            "CHM219": [80, 3, "None"],
            "PHY211": [80, 3, "None"],
            "MTH211": [80, 3, "None"],
            "MTH213": [80, 3, "None"],
            "GSE211": [80, 3, "None"],
            "CSC211": [80, 3, "None"],
            "EVS212": [80, 3, "None"]
        },
        "300 level": {
            "CHM310": [80, 3, "None"],
            "CHM311": [80, 3, "None"],
            "CHM312": [80, 3, "None"],
            "CHM313": [80, 3, "None"],
            "CHM316": [80, 3, "None"],
            "CHM318": [80, 3, "None"],
            "CHM319": [80, 3, "None"],
            "CHM330": [80, 3, "None"],
            "CHM334": [80, 3, "None"],
            "GSE311": [80, 3, "None"]
        }
    },
    "Geology": {
        "100 level": {
            "GLY111": [80, 3, "None"],
            "BIO111": [80, 3, "General"],
            "CHM112": [80, 3, "General"],
            "CHM119": [80, 3, "None"],
            "PHY111": [80, 3, "General"],
            "MTH111": [80, 3, "General"],
            "CSC111": [80, 3, "General"],
            "GSE111": [80, 3, "General"],
            "GSE112": [80, 3, "General"]
        },
        "200 level": {
            "GLY211": [80, 3, "None"],
            "GLY212": [80, 3, "None"],
            "GLY213": [80, 3, "None"],
            "GLY214": [80, 3, "None"],
            "GLY215": [80, 3, "None"],
            "GLY216": [80, 3, "None"],
            "CHM213": [80, 3, "None"],
            "GSE211": [80, 3, "None"],
            "GSE111": [80, 3, "None"],
            "GSE112": [80, 3, "None"]
        },
        "300 level": {
            "GLY331": [80, 3, "None"],
            "GLY312": [80, 3, "None"],
            "GLY313": [80, 3, "None"],
            "GLY314": [80, 3, "None"],
            "GLY315": [80, 3, "None"],
            "GLY316": [80, 3, "None"],
            "GPH314": [80, 3, "EVS212"],
            "GSE311": [80, 3, "None"]
        }
    }
}
v.hallListJson = {
    "TLH1": 50,
    "TLH2": 50,
    "TLH3": 50,
    "TLH4": 50,
    "TLH5": 50,
    "TLH6": 50,
    "TLH7": 50,
    "TLH8": 50,
    "TLH9": 50,
    "LT1": 250,
    "LT2": 75,
    "LT3": 75,
    "200LT": 100,
    "500LT1": 250,
    "Twin1": 100,
    "Twin2": 100
}
v.availableSlotJson = {
    "day1": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day2": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day3": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day4": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day5": [
        "8:00 - 10:30",
        "2:30 - 5:00"
    ],
    "day6": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day7": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day8": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day9": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day10": [
        "8:00 - 10:30",
        "2:30 - 5:00"
    ],
    "day11": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day12": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day13": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day14": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day15": [
        "8:00 - 10:30",
        "2:30 - 5:00"
    ],
    "day16": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day17": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day18": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day19": [
        "8:00 - 10:30",
        "11:15 - 2:00",
        "2:30 - 5:00"
    ],
    "day20": [
        "8:00 - 10:30",
        "2:30 - 5:00"
    ]
}
exams = []
examsStudentSize = []

deptExams = []
levelExams = []
levelExamCourseUnit = []
aliasExams = []

examDomain = []

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
    for level in v.courseListJson.values():
        deptList = []
        for courses in level.values():
            lvlList = []
            lvlListUnit = []
            for courseCode, courseInfo in courses.items():
                if courseInfo[2] == "General":
                    result = checkForAlias(aliasExams, courseCode)
                    if result[0]:
                        aliasExams[result[1]].append(aliasExams[result[1]][-1] + 'x')
                    else:
                        aliasExams.append([courseCode])
                elif courseInfo[2] != "None":
                    result = checkForAlias(aliasExams, courseInfo[2])
                    if result[0]:
                        aliasExams[result[1]].append(courseCode)
                    else:
                        aliasExams.append([courseInfo[2], courseCode])
                exams.append(courseCode)
                deptList.append(courseCode)
                lvlList.append(courseCode)
                examsStudentSize.append(courseInfo[0])
                lvlListUnit.append(courseInfo[1])

            levelExams.append(lvlList)
            levelExamCourseUnit.append(lvlListUnit)
        deptExams.append(deptList)

    # print(exams, "\n\n")
    # print(examsStudentSize, "\n\n")
    # print(deptExams, "\n\n")
    # print(levelExams, "\n\n")
    # print(levelExamCourseUnit, "\n\n")
    # print(aliasExams, "\n\n")

    hallName = []
    hallCap = []
    days = []
    time = []
    for name, capacity in v.hallListJson.items():
        hallName.append(name)
        hallCap.append(capacity)

    for day, slot in v.availableSlotJson.items():
        days.append(day)
        time.append(slot)
    for n in range(len(hallName)):
        timeSlot = [(i, j) for i in hallName for j in time[n]]
    examDomain = [(d, ts) for d in days for ts in timeSlot]
    print(examDomain)

    # print(hallName, "\n\n")
    # print(hallCap, "\n\n")
    # print(days, "\n\n")
    # print(time, "\n\n")
    return True


def solveCSPProblem():
    problem = Problem()

    return True




refineData()
