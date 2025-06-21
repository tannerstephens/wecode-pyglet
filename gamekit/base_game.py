from pathlib import Path

import pyglet.app
from pyglet import clock, resource
from pyglet.window import Window
from pyglet.window.key import KeyStateHandler

RESOURCES = Path(__file__).parent.parent.resolve() / "resources"


class BaseGame(Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.keys = KeyStateHandler()
        self.push_handlers(self.keys)

        clock.schedule_interval(self.tick, 1 / 60)

        resource.path = [str(RESOURCES)]
        self.load_resources()

    def load_resources(self):
        pass

    def tick(self, dt):
        """Called 60 times per second"""
        pass

    @classmethod
    def run(cls, width=1280, height=720):
        window = cls(width, height)

        pyglet.app.run()
