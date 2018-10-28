from collections import deque
from enum import Enum

class Direction(Enum):
    NORTH='north'
    EAST='east'
    SOUTH='south'
    WEST='west'

DIRECTION_VECTOR = {
    Direction.NORTH: (0, -1),
    Direction.SOUTH: (0, 1),
    Direction.EAST: (1, 0),
    Direction.WEST: (-1, 0),
}

class Snake:
    def __init__(self, coords, env_width):
        self.body = deque()
        self.body.append(coords)
        self.direction = Direction.EAST
        self.env_width = env_width

    def move(self):
        tail = self.body.popleft()
        x, y = self.body[-1] if len(self.body) else tail
        d_x, d_y = DIRECTION_VECTOR[self.direction]
        self.body.append(((x + d_x) % self.env_width,
                          (y + d_y) % self.env_width))
