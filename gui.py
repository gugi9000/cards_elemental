import arcade
import random


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Welcome to Cards Elemental"
RADIUS = 100

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.set_background_color(arcade.color.BLACK)

arcade.start_render()


class Ball:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f"Ball at {self.x}, {self.y}"

    def props(self):
        return self.x, self.y, RADIUS, self.color

    def move(self):
        direction = random.randint(-20, 20)
        self.x = self.x + direction
        self.y = self.y + direction


balls = [(250, 400, arcade.color.RED_BROWN),
         (350, 400, arcade.color.BLUE_BELL),
         (350, 500, arcade.color.ANDROID_GREEN),
         (250, 500, arcade.color.YELLOW_ORANGE),
         ]
while True:
    my_balls = [Ball(x, y, color[0]) for x, y, *color in balls]

    for ball in my_balls:
        arcade.draw_circle_filled(*ball.props())

    arcade.draw_text("Cards Elemental", 30, 700,  arcade.color.WHITE_SMOKE, 64)

    arcade.finish_render()

    for ball in my_balls:
        ball.move()
        print(ball)

# Display everything
arcade.run()
