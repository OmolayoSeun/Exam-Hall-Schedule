from collections import defaultdict

class ExamSchedulerCSP:
    def __init__(self, course_list, hall_list, time_slots, max_unit_per_day, max_unit_per_week):
        self.course_list = course_list
        self.hall_list = hall_list
        self.time_slots = time_slots
        self.max_unit_per_day = max_unit_per_day
        self.max_unit_per_week = max_unit_per_week
        self.schedule = defaultdict(lambda: defaultdict(list))
        self.assigned_exams = set()  # Track scheduled exams by (dept, level, course_code)

    def check_capacity(self, course_code, hall):
        course_info = self.get_course_info(course_code)
        return course_info[0] <= self.hall_list[hall]

    def get_course_info(self, course_code):
        for dept, levels in self.course_list.items():
            for level, courses in levels.items():
                if course_code in courses:
                    return courses[course_code]
        return None

    def is_compatible(self, dept, level, day, slot, course_code):
        # Check that the course is not already assigned to this dept and level
        if (dept, level, course_code) in self.assigned_exams:
            return False
        for scheduled_exam in self.schedule[day][slot]:
            if scheduled_exam[0] == dept:
                return False
        return True

    def check_alias_general_constraint(self, day, slot, course_code):
        # Enforces alias and general course constraints
        for dept, levels in self.course_list.items():
            for level, courses in levels.items():
                if course_code in courses:
                    self.schedule[day][slot].append((dept, level, course_code))
                    self.assigned_exams.add((dept, level, course_code))

    def check_units(self, dept, level, day):
        daily_units = 0
        weekly_units = 0
        for slot in self.schedule[day].values():
            for exam in slot:
                if exam[0] == dept and exam[1] == level:
                    course_info = self.get_course_info(exam[2])
                    daily_units += course_info[1]
                    if daily_units > self.max_unit_per_day:
                        return False
        for week_day in range(day - day % 7, day - day % 7 + 7):
            if week_day in self.schedule:
                for slot in self.schedule[week_day].values():
                    for exam in slot:
                        if exam[0] == dept and exam[1] == level:
                            course_info = self.get_course_info(exam[2])
                            weekly_units += course_info[1]
                            if weekly_units > self.max_unit_per_week:
                                return False
        return True

    def assign_exam(self, day, slot, dept, level, course_code):
        course_info = self.get_course_info(course_code)
        if not course_info:
            return False

        if (self.check_capacity(course_code, "LT1") and
            self.is_compatible(dept, level, day, slot, course_code) and
            self.check_units(dept, level, day)):
            self.check_alias_general_constraint(day, slot, course_code)
            self.schedule[day][slot].append((dept, level, course_code))
            self.assigned_exams.add((dept, level, course_code))  # Mark this exam as assigned
            return True
        return False

    def backtrack(self, day=0, slot=0):
        if day >= self.time_slots['Days']:
            return True
        if slot >= self.time_slots['Slot Per Day']:
            return self.backtrack(day + 1, 0)

        for dept, levels in self.course_list.items():
            for level, courses in levels.items():
                for course_code in courses:
                    if (dept, level, course_code) not in self.assigned_exams:  # Only assign unassigned exams
                        if self.assign_exam(day, slot, dept, level, course_code):
                            if self.backtrack(day, slot + 1):
                                return True
                            self.schedule[day][slot].remove((dept, level, course_code))
                            self.assigned_exams.remove((dept, level, course_code))  # Unmark the exam
        return False

    def solve(self):
        if self.backtrack():
            return self.schedule
        else:
            return None



course_list = {
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

hall_list = {
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

time_slots = {
    "Days": 20,
    "Slot Per Day": 3
}

max_unit_per_day = 6
max_unit_per_week = 18

scheduler = ExamSchedulerCSP(course_list, hall_list, time_slots, max_unit_per_day, max_unit_per_week)
solution = scheduler.solve()

if solution:
    print("Exam schedule found:")
    print(solution)
else:
    print("No valid schedule could be created.")
