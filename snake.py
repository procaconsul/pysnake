import pdb
from collections import deque
from enum import Enum

class Direction(Enum):
    NORTH = 1
    EAST  = 2
    SOUTH = -1
    WEST  = -2


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
    
    def __len__(self):
        return len(self.body)

    def __getitem__(self, index):
        return self.body[index]

    def change_direction(self, new_direction):
        if new_direction.value + self.direction.value:
          self.direction = new_direction

    def move(self):
        tail = self.body.popleft()
        x, y = self.body[-1] if len(self.body) else tail
        d_x, d_y = DIRECTION_VECTOR[self.direction]
        self.body.append(((x + d_x) % self.env_width,
                          (y + d_y) % self.env_width))
