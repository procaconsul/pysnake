class SnakeRenderer:
    def __init__(self, canvas, snake):
        self.canvas = canvas
        self.snake = snake

    def render(self):
        self.render_head()

        for point in self.snake.tail:
            render_point(self.canvas, point, 'black')


    def render_head(self):
        if self.snake.next_position() == food or self.snake.head == food:
            x, y = self.snake.head
            x, y = x * TILE_WIDTH, y * TILE_WIDTH
            midpoint = [x + (TILE_WIDTH / 2), y + (TILE_WIDTH / 2)]

            bbox = [[x, y],
                    [x + TILE_WIDTH, y],
                    [x + TILE_WIDTH, y + TILE_WIDTH],
                    [x, y + TILE_WIDTH]]

            bbox.insert(self.snake.direction.value + 1, midpoint)

            bbox = [coord for point in bbox for coord in point]

            self.canvas.create_polygon(bbox, fill="blue", outline="white")
        else:
            render_point(self.canvas, self.snake.head, "blue")

def render_point(canvas, point, color, square=True):
    coord_x, coord_y = point.x * TILE_WIDTH, point.y * TILE_WIDTH
    renderer = canvas.create_rectangle if square else canvas.create_oval
    return renderer(coord_x, coord_y,
                    coord_x + TILE_WIDTH,
                    coord_y + TILE_WIDTH,
                    fill=color,
                    outline='white')
