from enum import Enum
from collections import namedtuple 

class Direction(Enum):
    NORTH = 1
    EAST  = 2
    SOUTH = -1
    WEST  = -2

Point = namedtuple('Point', 'x, y')
