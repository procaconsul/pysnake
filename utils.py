from enum import Enum
from collections import namedtuple 

class Direction(Enum):
    NORTH = 0
    EAST  = 1
    SOUTH = 2
    WEST  = 3

    def is_opposite(self, other):
        return self.value + other.value % 2 == 0

Point = namedtuple('Point', 'x, y')
