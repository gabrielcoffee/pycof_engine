from pygame import Vector2, Rect

class Entity:

    def __init__(self, x, y, width, height):
        self.tag = ''
        self.pos = Vector2(x, y)
        self.dim = Vector2(width, height)
        self.init()

    def init(self):
        pass

    def _update(self):
        self.hitbox = Rect(
            self.pos.x,
            self.pos.y,
            self.dim.x,
            self.dim.y
        )
        self.update()

    def update(self):
        pass

    def draw(self, screen, cam_offset):
        pass

    def onAddedToScene(self):
        pass

    def onRemovedFromScene(self):
        pass

