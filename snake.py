from collections import deque

from utils import Direction, Point

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
        return list(self.body)[index]

    def change_direction(self, new_direction):
        if new_direction.value + self.direction.value:
          self.direction = new_direction

    def move(self, grow=False):
        tail = self.body[0] if grow else self.body.popleft()
        x, y = self.body[-1] if len(self.body) else tail
        d_x, d_y = DIRECTION_VECTOR[self.direction]
        self.body.append(Point((x + d_x) % self.env_width,
                          (y + d_y) % self.env_width))


    @property
    def tail(self):
        return self[:-1]
