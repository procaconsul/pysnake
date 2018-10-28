import pdb
import tkinter as tk
from random import randint

from snake import Snake
from utils import Direction, Point

root = tk.Tk()

SCREEN_WIDTH = 500

FRAME_RATE = 250
TILE_WIDTH = 25

ENV_WIDTH = SCREEN_WIDTH / TILE_WIDTH

KEY_MAPPINGS = {
    'Up': Direction.NORTH,
    'Down': Direction.SOUTH,
    'Left': Direction.WEST,
    'Right': Direction.EAST,
}

canvas = tk.Canvas(root, width=SCREEN_WIDTH, height=SCREEN_WIDTH)
canvas.pack()

def random_point():
    return Point(randint(0, ENV_WIDTH - 1), randint(0, ENV_WIDTH - 1))

def food_location(snake):
    food = random_point()
    while food in snake:
        food = random_point()
    return food

snake = Snake(Point(ENV_WIDTH / 2, ENV_WIDTH / 2), ENV_WIDTH)
food = food_location(snake)

def render_point(point, color):
  coord_x, coord_y = point.x * TILE_WIDTH, point.y * TILE_WIDTH
  canvas.create_rectangle(coord_x, coord_y,
                          coord_x + TILE_WIDTH,
                          coord_y + TILE_WIDTH,
                          fill=color,
                          outline='white')

def render_food(food):
    render_point(food, 'red')
    
def render_snake(snake):
    for point in snake:
        render_point(point, 'black')

def game_loop():
    global food 
    if food in snake:
      food = food_location(snake)
      snake.move(grow=True)
    else:
        snake.move()
    canvas.delete('all')
    render_food(food)
    render_snake(snake)
    root.after(FRAME_RATE, game_loop)

def change_direction(event):
    if event.keysym in KEY_MAPPINGS.keys():
        snake.change_direction(KEY_MAPPINGS[event.keysym])

root.bind('<Key>', change_direction)

root.after(FRAME_RATE, game_loop)
root.mainloop()
