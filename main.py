import pdb
import tkinter as tk

from snake import Snake

root = tk.Tk()

WIDTH, HEIGHT = 500, 500

FRAME_RATE = 250
TILE_WIDTH = 25

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

snake = Snake((WIDTH/TILE_WIDTH/2, HEIGHT/TILE_WIDTH/2))

def render_snake(snake):
    for x, y in snake.body:
        coord_x, coord_y = x * TILE_WIDTH, y * TILE_WIDTH
        canvas.create_rectangle(coord_x, coord_y,
                                coord_x + TILE_WIDTH,
                                coord_y + TILE_WIDTH,
                                fill="black",
                                outline="white")

def game_loop():
    # pdb.set_trace()
    snake.move()
    canvas.delete("all")
    render_snake(snake)
    root.after(FRAME_RATE, game_loop)

root.after(FRAME_RATE, game_loop)
root.mainloop()
