from pyglet import resource
from pyglet.math import Vec2
from pyglet.shapes import Rectangle
from pyglet.window import key

from gamekit import BaseGame, ResizableSprite

SPEED = 500


class Game(BaseGame):
    def load_resources(self):
        self.background = Rectangle(0, 0, self.width, self.height, color=(128, 255, 0))

        player_image = resource.image("man.png")
        player_image.anchor_x = player_image.width // 2
        player_image.anchor_y = player_image.height // 2

        self.player = ResizableSprite(player_image, 200, 200, width=64, height=64)

    def on_draw(self):
        self.clear()
        self.background.draw()
        self.player.draw()

    def tick(self, dt):
        dx = dy = 0
        boost = 1

        if self.keys[key.UP]:
            dy += 1
        if self.keys[key.DOWN]:
            dy -= 1
        if self.keys[key.LEFT]:
            dx -= 1
        if self.keys[key.RIGHT]:
            dx += 1

        if self.keys[key.LSHIFT] or self.keys[key.RSHIFT]:
            boost = 2

        movement_vector = Vec2(dx, dy).normalize()

        self.player.x += movement_vector.x * SPEED * boost * dt
        self.player.y += movement_vector.y * SPEED * boost * dt


Game.run()
