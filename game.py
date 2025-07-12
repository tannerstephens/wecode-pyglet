"""THE BELOW IS REQUIRED FOR PYGLET TO FUNCTION ON THE PI5"""

import os

os.environ["LIBGL_ALWAYS_SOFTWARE"] = "1"

"""THE ABOVE IS REQUIRED FOR PYGLET TO FUNCTION ON THE PI5"""

from pyglet.shapes import Rectangle
from pyglet import font, shapes, text
from pyglet.window import key

from gamekit import BaseGame

ARROW_SPEED = 10


class Game(BaseGame):
    def load_resources(self):
        self.grass = shapes.Rectangle(0, 0, self.width, 150, color=(0, 128, 64))
        self.sky = shapes.Rectangle(
            0, 150, self.width, self.height - 150, color=(83, 185, 239)
        )

        self.target_base = shapes.Triangle(
            600, 50, 680, 50, 640, 250, color=(114, 72, 0)
        )
        self.target1 = shapes.Circle(640, 250, 150, color=(0, 0, 255))
        self.target2 = shapes.Circle(640, 250, 100, color=(255, 0, 0))
        self.target3 = shapes.Circle(640, 250, 50, color=(255, 255, 0))

        self.arrow = shapes.Circle(400, 250, 10, color=(114, 72, 0))
        self.move_right = True

        self.score = 0

        font.add_file("./gamekit/fonts/roboto.ttf")

        self.scoreboard = text.Label(
            f"{self.score}", 0, 650, font_size=64, font_name="Roboto", color=(0, 0, 0)
        )

    def draw_background(self):
        self.grass.draw()
        self.sky.draw()

    def draw_target(self):
        self.target_base.draw()
        self.target1.draw()
        self.target2.draw()
        self.target3.draw()

    def on_draw(self):
        self.clear()

        self.draw_background()
        self.draw_target()

        self.arrow.draw()
        self.scoreboard.draw()

    def tick(self, dt):
        if self.move_right:
            self.arrow.x += ARROW_SPEED

            if self.arrow.x >= 880:
                self.arrow.x = 880
                self.move_right = False

        else:
            self.arrow.x -= ARROW_SPEED

            if self.arrow.x <= 400:
                self.arrow.x = 400
                self.move_right = True

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            coords = (self.arrow.x, self.arrow.y)

            if coords in self.target3:
                self.score += 5
            elif coords in self.target2:
                self.score += 3
            elif coords in self.target1:
                self.score += 1
            else:
                self.score -= 1

            self.scoreboard.text = str(self.score)


Game.run()
