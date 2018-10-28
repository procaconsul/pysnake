import tkinter as tk
from random import randint

from snake import Snake
from utils import Direction, Point

SCREEN_WIDTH = 500
FRAME_RATE = 150
TILE_WIDTH = 25
GAME_OVER_MSG='GAME OVER'
ENV_WIDTH = SCREEN_WIDTH / TILE_WIDTH
KEY_MAPPINGS = {
    'Up': Direction.NORTH,
    'Down': Direction.SOUTH,
    'Left': Direction.WEST,
    'Right': Direction.EAST,
}

root = tk.Tk()
canvas = tk.Canvas(root, width=SCREEN_WIDTH, height=SCREEN_WIDTH)
score_var = tk.StringVar()
score_var.set("Score: 0")
score_label = tk.Label(root,
                       padx=15, pady=10,
                       textvariable=score_var,
                       font='courier 20 bold')
canvas.pack()
score_label.pack(side='right')

def random_point():
    return Point(randint(0, ENV_WIDTH - 1), randint(0, ENV_WIDTH - 1))

def food_location(snake):
    food = random_point()
    while food in snake:
        food = random_point()
    return food

snake = Snake(Point(ENV_WIDTH / 2, ENV_WIDTH / 2), ENV_WIDTH)
food = food_location(snake)
score = 0
frame_updated = False

def increment_score():
    global score
    score += 1
    score_var.set(f"Score: {score}")

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
    render_point(snake[-1], 'blue')
    for point in snake.tail:
        render_point(point, 'black')

def game_loop():
    global frame_updated, food

    if food in snake:
      food = food_location(snake)
      snake.move(grow=True)
      increment_score()
    else:
        snake.move()

    if snake[-1] in snake.tail:
        text = canvas.create_text(SCREEN_WIDTH/2, SCREEN_WIDTH/2,
                                  fill='black',font='courier 80 bold', 
                                  text=GAME_OVER_MSG)
        text_frame = canvas.create_rectangle(canvas.bbox(text), 
                                             fill='white', 
                                             outline='white')
        canvas.tag_lower(text_frame, text)

    else:
        canvas.delete('all')
        render_food(food)
        render_snake(snake)
        frame_updated = False
        root.after(FRAME_RATE, game_loop)

def change_direction(event):
    global frame_updated
    if event.keysym in KEY_MAPPINGS.keys() and not frame_updated:
        snake.change_direction(KEY_MAPPINGS[event.keysym])
        frame_updated = True

root.bind('<Key>', change_direction)

root.after(FRAME_RATE, game_loop)
root.mainloop()
