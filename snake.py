class Snake:
    def __init__(self, coords):
        self.body = [coords]
        self.direction = 'east'

    def move(self):
        if len(self.body) == 1:
             # import code; code.interact(local=dict(globals(), **locals()))
            (x, y) = self.body.pop()
            self.body.append((x + TILE_WIDTH, y))
        else:
            # need to pop_left here
            _, *rest = self.body
            (x, y) = rest[-1]
            self.body.append(x + TILE_WIDTH, y)
