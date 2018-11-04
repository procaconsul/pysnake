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
        if not self.direction.is_opposite(new_direction):
          self.direction = new_direction

    def move(self, grow=False):
        new_head = self.next_position()
        if not grow:
            self.body.popleft()
        self.body.append(new_head)

    def next_position(self):
        x, y = self.head
        dx, dy = DIRECTION_VECTOR[self.direction]
        return Point((x + dx) % self.env_width,
                     (y + dy) % self.env_width)

    @property
    def head(self):
        return self[-1]

    @property
    def tail(self):
        return self[:-1]
