"""THE BELOW IS REQUIRED FOR PYGLET TO FUNCTION ON THE PI5"""

import os

os.environ["LIBGL_ALWAYS_SOFTWARE"] = "1"

"""THE ABOVE IS REQUIRED FOR PYGLET TO FUNCTION ON THE PI5"""

from pyglet.shapes import Rectangle

from gamekit import BaseGame

BACKGROUND_COLOR = (255, 255, 255)


class Game(BaseGame):
    def load_resources(self):
        self.background = Rectangle(
            0, 0, self.width, self.height, color=BACKGROUND_COLOR
        )

    def on_draw(self):
        self.clear()
        self.background.draw()

    def tick(self, dt):
        pass


Game.run()
