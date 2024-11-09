from Debug import *

msg = DebugMSG()


# Expected data
# Name: CSC312
# info: [80, 3, 'None']
class Variable:
    def __init__(self, name: str, info: list):
        self.name = name
        self.info = info
        pass


# Expected data
# dictionary of the hall
class Hall:
    name = []
    capacity = []

    def __init__(self, hall: dict):
        for key, value in hall.items():
            self.name.append(key)
            self.capacity.append(value)
        self.count = len(self.name)
        pass


# Expected data
# Dictionary of the slots
class Allocation:
    def __init__(self, allocation: dict):
        self.dayCount = allocation['Days']
        self.slotCount = allocation['Slot Per Day']
        pass


# Expected data
# Allocation and Hall
class Domain:
    def __init__(self, allocation: Allocation, hall: Hall):
        self.dayCount = allocation.dayCount
        self.slotCount = allocation.slotCount
        self.hallCount = hall.count
        self.hallName = hall.name
        self.hallCapacity = hall.capacity
        pass


# Expected data
""""
@:param maxPerDay - number of unit student can take per day
@:param maxPerWeek - number of unit student can take per week
@:param levelExams - exams unique to student level
@:param deptExams - exam unique to the department
@:param alaisExam - exams that are general of have an alias name
"""


class Constraints:
    def __init__(self, maxPerDay: int, maxPerWeek: int, levelExams: list, deptExams: list, alaisExam):
        self.maxPerDay = maxPerDay
        self.maxPerWeek = maxPerWeek
        self.levelExams = levelExams
        self.deptExams = deptExams
        self.alaisExam = alaisExam
        pass

    def __checkCapacity__(self):

        pass

    def __checkMaxPerWeek__(self):
        pass

    def __checkMaxPerDay__(self):
        pass

    def __checkAlias__(self):
        pass

    def __checkDept__(self):
        pass

    def __checkLevel__(self, name, solutions, dayIndex, slotIndex):
        ls = []
        for lvlLst in self.levelExams:
            if name in lvlLst:
                ls = lvlLst
                break

        for a in ls:
            for b in solutions:
                if a == b[0] and b[1] == dayIndex and b[2] == slotIndex:
                    return False
        return True

    @staticmethod
    def __noRepeatedCourse__(name, item):
        return name in item

    def isSatisfied(self, var: Variable, domain: Domain, solution: list, dayIndex: int, slotIndex: int, hallIndex: int):
        item = []
        for ls in solution:
            item.append(ls[0])
        if self.__noRepeatedCourse__(var.name, item):
            return False

        return True


"""
@:param variables - receive a list of the variable class
@:param domain - receive the domain class variable
@:param constraint - the constraint class variable
"""


class CSP:
    solution = []

    def __init__(self, variables: list, domain: Domain, constraint: Constraints):
        self.const = constraint
        self.domain = domain
        self.variables = variables

    def __allResolved__(self):
        item = []
        for ls in self.solution:
            item.append(ls[0])
        # msg.msg("Item", item)
        # msg.msg("ls", self.solution)

        for var in self.variables:
            if var.name not in item:
                return False
            pass
        return True

    def __backtrack__(self):
        pass

    # @staticmethod
    def getSolution(self):
        resolvedCourse = False
        for i in range(1):
            for var in self.variables:
                #   loop through the domain slots
                for dayIndex in range(self.domain.dayCount):
                    for slotIndex in range(self.domain.slotCount):
                        for hallIndex in range(self.domain.hallCount):
                            print([var.name, dayIndex, slotIndex, self.domain.hallName[hallIndex]])
                            resolvedCourse = self.const.isSatisfied(var, self.domain, self.solution, dayIndex, slotIndex, hallIndex)
                            if resolvedCourse:
                                self.solution.append([var.name, dayIndex, slotIndex, self.domain.hallName[hallIndex]])
                                # E.g [Mth111, 2, 0, TLH1]
                                print("APPROVED: ", [var.name, dayIndex, slotIndex, self.domain.hallName[hallIndex]])
                                break
                            pass
                        if resolvedCourse:
                            break
                    if resolvedCourse:
                        break

            if self.__allResolved__():
                print("==========ALL RESOLED++++++++++")
                break
        return self.solution
