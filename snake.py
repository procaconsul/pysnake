import pdb
import tkinter as tk



from collections import deque

root = tk.Tk()

WIDTH, HEIGHT = 500, 500

FRAME_RATE = 250
TILE_WIDTH = 25

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.create_rectangle(250, 250, 275, 275, outline="black")
canvas.pack()


# Logic
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


the_snake = Snake((WIDTH/2, HEIGHT/2))

def render_snake(the_snake):
    for x, y in the_snake.body:
        canvas.create_rectangle(x, y, x + TILE_WIDTH, y + TILE_WIDTH)

def game_loop():
    # pdb.set_trace()
    the_snake.move()
    canvas.delete("all")
    render_snake(the_snake)
    root.after(FRAME_RATE, game_loop)

root.after(FRAME_RATE, game_loop)
root.mainloop()



