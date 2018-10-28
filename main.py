import pdb
import tkinter as tk

from snake import Snake

root = tk.Tk()

WIDTH, HEIGHT = 500, 500

FRAME_RATE = 250
TILE_WIDTH = 25

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.create_rectangle(250, 250, 275, 275, outline="black")
canvas.pack()

the_snake = Snake((WIDTH/2, HEIGHT/2))

def render_snake(the_snake):
    for x, y in the_snake.body:
        coord_x, coord_y = x * TILE_WIDTH, y * TILE_WIDTH
        canvas.create_rectangle(coord_x, coord_y,
                                coord_x + TILE_WIDTH,
                                coord_y + TILE_WIDTH)

def game_loop():
    # pdb.set_trace()
    the_snake.move()
    canvas.delete("all")
    render_snake(the_snake)
    root.after(FRAME_RATE, game_loop)

root.after(FRAME_RATE, game_loop)
root.mainloop()
