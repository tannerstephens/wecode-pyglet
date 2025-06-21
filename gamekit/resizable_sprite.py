from pyglet.sprite import Sprite


class ResizableSprite(Sprite):
    def __init__(self, *args, width=None, height=None, **kwargs):
        super().__init__(*args, subpixel=True, **kwargs)

        if width is not None:
            self.width = width

        if height is not None:
            self.height = height

    @property
    def width(self):
        return self.image.width * self.scale_x

    @width.setter
    def width(self, value):
        self.scale_x = value / self.image.width

    @property
    def height(self):
        return self.image.width * self.scale_x

    @height.setter
    def height(self, value):
        self.scale_y = value / self.image.height
