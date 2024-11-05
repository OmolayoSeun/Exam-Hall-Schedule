# This class contains variables that will be used across various modules of the software
from enum import Enum

current_frame = None

app = None

courseListJson = dict
hallListJson = dict
availableSlotJson = dict

x = 1100
y = 700

frames = {}

class SCREEN(Enum):
    FIRST_SCREEN = 1
    SECOND_SCREEN = 2
