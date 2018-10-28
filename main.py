import pdb
import tkinter as tk

from snake import Snake

root = tk.Tk()

SCREEN_WIDTH = 500

FRAME_RATE = 250
TILE_WIDTH = 25

ENV_WIDTH = SCREEN_WIDTH / TILE_WIDTH

canvas = tk.Canvas(root, width=SCREEN_WIDTH, height=SCREEN_WIDTH)
canvas.pack()

snake = Snake((ENV_WIDTH / 2, ENV_WIDTH / 2), ENV_WIDTH)

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
