class Variable:
    def __init__(self, name: str, info: list):
        self.name = name
        self.info = info
        pass


class Hall:
    name = []
    capacity = []
    totalCapacity = 0

    def __init__(self, hall: dict):
        for key, value in hall.items():
            self.name.append(key)
            self.capacity.append(value)
            self.totalCapacity = self.totalCapacity + value
        self.count = len(self.name)
        pass


class Allocation:
    def __init__(self, allocation: dict):
        self.dayCount = allocation['Days']
        self.slotCount = allocation['Slot Per Day']
        pass


class Domain:
    def __init__(self, allocation: Allocation, hall: Hall):
        self.dayCount = allocation.dayCount
        self.slotCount = allocation.slotCount
        self.hallCount = hall.count
        self.hallName = hall.name
        self.hallCapacity = hall.capacity
        self.totalHallCap = hall.totalCapacity
        pass


class Constraints:
    def __init__(self, maxPerDay: int, maxPerWeek: int, levelExams: list, deptExams: list, alaisExam):
        self.maxPerDay = maxPerDay
        self.maxPerWeek = maxPerWeek
        self.levelExams = levelExams
        self.deptExams = deptExams
        self.alaisExam = alaisExam
        pass

    @staticmethod
    def __checkCapacity__(var: Variable, hallCap: int):
        if var.info[0] > hallCap:
            return True
        return False

    def __checkMaxPerWeek__(self):
        pass


    def __checkMaxPerDay__(self):
        pass

    def __checkDept__(self, name, solutions, dayIndex, slotIndex):
        if not solutions:
            return False
        ls = []
        for deptLst in self.deptExams:
            if name in deptLst:
                ls = deptLst
                break
        for a in ls:
            for b in solutions:
                if a == b[0] and b[1] == dayIndex and b[2] == slotIndex:
                    return True
        return False

    @staticmethod
    def __hallIsAvailable__(solution: list, dayIndex: int, slotIndex: int, hallName: str):
        for ls in solution:
            if dayIndex == ls[1] and slotIndex == ls[2] and hallName == ls[-1]:
                return True
        return False

    def __checkLevel__(self, name, solutions, dayIndex, slotIndex):
        if not solutions:
            return False
        ls = []
        for lvlLst in self.levelExams:
            if name in lvlLst:
                ls = lvlLst
                break

        for a in ls:
            for b in solutions:
                if a == b[0] and b[1] == dayIndex and b[2] == slotIndex:
                    return True
        return False

    @staticmethod
    def __noRepeatedCourse__(name, item):
        return name in item

    def isSatisfied(self, var: Variable, domain: Domain, solution: list, dayIndex: int, slotIndex: int, hallName: str, hallIndex: int):
        item = []
        for ls in solution:
            item.append(ls[0])
        if self.__noRepeatedCourse__(var.name, item):
            return False
        if self.__hallIsAvailable__(solution, dayIndex, slotIndex, hallName):
            return False
        if self.__checkLevel__(var.name, solution, dayIndex, slotIndex):
            return False
        if self.__checkDept__(var.name, solution, dayIndex, slotIndex):
            return False
        if self.__checkCapacity__(var, domain.hallCapacity[hallIndex]):
            return False

        return True


class CSP:
    solution = []

    def __init__(self, variables: list, domain: Domain, constraint: Constraints, makeList: dict):
        self.const = constraint
        self.domain = domain
        self.variables = variables
        self.makeList = makeList

    def __allResolved__(self):
        item = []
        for ls in self.solution:
            item.append(ls[0])

        for var in self.variables:
            if var.name not in item:
                return False
            pass
        return True

    def __backtrack__(self):
        pass

    # @staticmethod
    def getSolution(self):
        global increase
        resolvedCourse = False
        # fill alias course first
        for i in range(len(self.const.alaisExam)):
            size = 0
            for ls in self.const.alaisExam[i]:
                # print(self.makeList[ls])
                size = size + self.makeList[ls][0]
            hallSize = 0

            for j in range(self.domain.hallCount):
                hallSize = hallSize + self.domain.hallCapacity[j]
                if size <= hallSize:
                    increase = j
                    break
            for x in range(increase):
                try:
                    self.solution.append([self.const.alaisExam[i][x], i, 0, self.domain.hallName[x]])
                except:
                    self.solution.append([self.const.alaisExam[i][-1], i, 0, self.domain.hallName[x]])

                pass
            print(size)

        while True:
            for var in self.variables:
                #   loop through the domain slots
                for dayIndex in range(self.domain.dayCount):
                    for slotIndex in range(self.domain.slotCount):
                        for hallIndex in range(self.domain.hallCount):
                            # print([var.name, dayIndex, slotIndex, self.domain.hallName[hallIndex]])
                            resolvedCourse = self.const.isSatisfied(var, self.domain, self.solution, dayIndex,
                                                                    slotIndex, self.domain.hallName[hallIndex], hallIndex)
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

