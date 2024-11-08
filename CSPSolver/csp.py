class Variable:
    def __init__(self, name: str, info: list):
        self.name = name
        self.info = info
        pass


class Hall:
    name = []
    capacity = []

    def __init__(self, hall: dict):
        for key, value in hall.items():
            self.name.append(key)
            self.capacity.append(value)
        self.count = len(self.name)
        pass


class Allocation:
    def __init__(self, allocation: dict):
        self.dayCount = allocation['Days']
        self.slotCount = allocation['Slot Per Day']
        pass


class Domain:
    def __init__(self, allocation: Allocation, hall: Hall):
        self.dayCount = allocation.slotCount
        self.slotCount = allocation.slotCount
        self.hallCount = hall.count
        self.hallName = hall.name
        self.hallCapacity = hall.capacity
        pass


class Constraints:
    def __init__(self, maxPerWeek: int, maxPerDay: int, levelExams: list, deptExams: list, alaisExam):
        self.maxPerWeek = maxPerWeek
        self.maxPerDay = maxPerDay
        self.levelExams = levelExams
        self.deptExams = deptExams
        self.alaisExam = alaisExam
        pass

    def __checkMaxPerWeek__(self):
        pass
    def __checkMaxPerDay__(self):
        pass
    def __checkAlias__(self):
        pass
    def __checkDept__(self):
        pass
    def __checkLevel__(self):
        pass
    def isSatisfied(self):
        pass

class CSP:
    def __init__(self, variables, domain, constraint):
        self.constraint = constraint
        self.domain = domain
        self.variables = variables



    def __backtrack__(self):
        pass

    def getSolution(self):
        pass
