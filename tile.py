from pygame import Rect


class Tile:
    SIZE = 8

    def __init__(self, position, texture):
        self.position = position
        self.surface = texture
        self.hitbox = Rect(position.x, position.y, self.SIZE, self.SIZE)

    def draw(self, surface):
        surface.blit(self.surface, self.position)