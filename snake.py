from collections import deque

class Snake:
    def __init__(self, coords):
        self.body = deque()
        self.body.append(coords)
        self.direction = 'east'

    def move(self):
        if len(self.body) == 1:
             # import code; code.interact(local=dict(globals(), **locals()))
            (x, y) = self.body.pop()
            self.body.append((x + 1, y))
        else:
            self.body.popleft()
            (x, y) = self.body[-1]
            self.body.append(x + 1, y)
