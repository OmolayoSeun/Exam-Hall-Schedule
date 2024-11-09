from resources import Variables as v
from csp import *

listOfCourse = []
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
            "CHM213": [80, 3, "General"],
            "CHM214": [80, 3, "None"],
            "CHM219": [80, 3, "None"],
            "PHY211": [80, 3, "None"],
            "MTH211": [80, 3, "None"],
            "MTH213": [80, 3, "None"],
            "GSE211": [80, 3, "General"],
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
            "GSE311": [80, 3, "General"]
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
            "CHM213": [80, 3, "General"],
            "GSE211": [80, 3, "General"],
            "GSE111": [80, 3, "General"],
            "GSE112": [80, 3, "General"]
        },
        "300 level": {
            "GLY331": [80, 3, "None"],
            "GLY312": [80, 3, "None"],
            "GLY313": [80, 3, "None"],
            "GLY314": [80, 3, "None"],
            "GLY315": [80, 3, "None"],
            "GLY316": [80, 3, "None"],
            "GPH314": [80, 3, "EVS212"],
            "GSE311": [80, 3, "General"]
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
    "Days": 20,
    "Slot Per Day": 3
}
courseMakeList = {'CHM112': [80, 3, 'General'], 'CHM111': [80, 3, 'None'], 'MTH112': [80, 3, 'None'],
                  'MTH111': [80, 3, 'General'], 'BIO111': [80, 3, 'General'], 'CSC111': [80, 3, 'General'],
                  'PHY111': [80, 3, 'General'], 'GSE111': [80, 3, 'General'], 'GSE112': [80, 3, 'General'],
                  'CHM211': [80, 3, 'None'], 'CHM212': [80, 3, 'None'], 'CHM213': [80, 3, 'General'],
                  'CHM214': [80, 3, 'None'], 'CHM219': [80, 3, 'None'], 'PHY211': [80, 3, 'None'],
                  'MTH211': [80, 3, 'None'], 'MTH213': [80, 3, 'None'], 'GSE211': [80, 3, 'General'],
                  'CSC211': [80, 3, 'None'], 'EVS212': [80, 3, 'None'], 'CHM310': [80, 3, 'None'],
                  'CHM311': [80, 3, 'None'], 'CHM312': [80, 3, 'None'], 'CHM313': [80, 3, 'None'],
                  'CHM316': [80, 3, 'None'], 'CHM318': [80, 3, 'None'], 'CHM319': [80, 3, 'None'],
                  'CHM330': [80, 3, 'None'], 'CHM334': [80, 3, 'None'], 'GSE311': [80, 3, 'General'],
                  'GLY111': [80, 3, 'None'], 'BIO111x': [80, 3, 'General'], 'CHM112x': [80, 3, 'General'],
                  'CHM119': [80, 3, 'None'], 'PHY111x': [80, 3, 'General'], 'MTH111x': [80, 3, 'General'],
                  'CSC111x': [80, 3, 'General'], 'GSE111x': [80, 3, 'General'], 'GSE112x': [80, 3, 'General'],
                  'GLY211': [80, 3, 'None'], 'GLY212': [80, 3, 'None'], 'GLY213': [80, 3, 'None'],
                  'GLY214': [80, 3, 'None'], 'GLY215': [80, 3, 'None'], 'GLY216': [80, 3, 'None'],
                  'CHM213x': [80, 3, 'General'], 'GSE211x': [80, 3, 'General'], 'GSE111xx': [80, 3, 'General'],
                  'GSE112xx': [80, 3, 'General'], 'GLY331': [80, 3, 'None'], 'GLY312': [80, 3, 'None'],
                  'GLY313': [80, 3, 'None'], 'GLY314': [80, 3, 'None'], 'GLY315': [80, 3, 'None'],
                  'GLY316': [80, 3, 'None'], 'GPH314': [80, 3, 'EVS212'], 'GSE311x': [80, 3, 'General']}

deptExams = [['CHM112', 'CHM111', 'MTH112', 'MTH111', 'BIO111',
              'CSC111', 'PHY111', 'GSE111', 'GSE112', 'CHM211',
              'CHM212', 'CHM213', 'CHM214', 'CHM219', 'PHY211',
              'MTH211', 'MTH213', 'GSE211', 'CSC211', 'EVS212',
              'CHM310', 'CHM311', 'CHM312', 'CHM313', 'CHM316',
              'CHM318', 'CHM319', 'CHM330', 'CHM334', 'GSE311'],
             ['GLY111', 'BIO111x', 'CHM112x', 'CHM119', 'PHY111x',
              'MTH111x', 'CSC111x', 'GSE111x', 'GSE112x', 'GLY211',
              'GLY212', 'GLY213', 'GLY214', 'GLY215', 'GLY216', 'CHM213x',
              'GSE211x', 'GSE111xx', 'GSE112xx', 'GLY331', 'GLY312', 'GLY313',
              'GLY314', 'GLY315', 'GLY316', 'GPH314', 'GSE311x']]
levelList = [['CHM112', 'CHM111', 'MTH112', 'MTH111', 'BIO111', 'CSC111',
              'PHY111', 'GSE111', 'GSE112'],
             ['CHM211', 'CHM212', 'CHM213', 'CHM214', 'CHM219', 'PHY211', 'MTH211',
              'MTH213', 'GSE211', 'CSC211', 'EVS212'],
             ['CHM310', 'CHM311', 'CHM312', 'CHM313', 'CHM316', 'CHM318', 'CHM319',
              'CHM330', 'CHM334', 'GSE311'],
             ['GLY111', 'BIO111x', 'CHM112x', 'CHM119', 'PHY111x', 'MTH111x',
              'CSC111x', 'GSE111x', 'GSE112x'],
             ['GLY211', 'GLY212', 'GLY213', 'GLY214', 'GLY215', 'GLY216', 'CHM213x',
              'GSE211x', 'GSE111xx', 'GSE112xx'],
             ['GLY331', 'GLY312', 'GLY313', 'GLY314', 'GLY315',
              'GLY316', 'GPH314', 'GSE311x']]

aliasList = [['CHM112', 'CHM112x'], ['MTH111', 'MTH111x'], ['BIO111', 'BIO111x'],
             ['CSC111', 'CSC111x'], ['PHY111', 'PHY111x'], ['GSE111', 'GSE111x', 'GSE111xx'],
             ['GSE112', 'GSE112x', 'GSE112xx'], ['CHM213', 'CHM213x'],
             ['GSE211', 'GSE211x'], ['GSE311', 'GSE311x'], ['EVS212', 'GPH314']]

for name, info in courseMakeList.items():
    listOfCourse.append(Variable(name, info))

hall = Hall(v.hallListJson)
allocation = Allocation(v.availableSlotJson)

domain = Domain(allocation, hall)
constraints = Constraints(5, 9, levelList, deptExams, aliasList)

cspSolution = CSP(listOfCourse, domain, constraints)
sol = cspSolution.getSolution()
print(sol)
