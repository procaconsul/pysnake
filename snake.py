from collections import deque

class Snake:
    def __init__(self, coords):
        self.body = deque()
        self.body.append(coords)
        self.direction = 'east'

    def move(self):
        tail = self.body.popleft()
        x, y = self.body[-1] if len(self.body) else tail
        self.body.append((x + 1, y))
