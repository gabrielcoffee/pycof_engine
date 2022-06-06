from pygame import Vector2

class BackgroundSprite():
    def __init__(self, backg_surface, percent_speed, axis):
        self.surface = backg_surface
        self.percent_speed = percent_speed
        self.axis = axis

        self.width = backg_surface.get_width()
        self.height = backg_surface.get_height()
        self.pos1 = Vector2()
        self.pos2 = Vector2()

    def update(self, offset):

        if self.axis == 'x':
            xOffsets = offset.x // self.width
            self.pos1 = Vector2(-offset.x + (self.width * xOffsets), offset.y)
            self.pos2 = Vector2(-offset.x + (self.width * (xOffsets + 1 )), offset.y)

        elif self.axis == 'y':
            yOffsets = offset.y // self.height
            self.pos1 = Vector2(-offset.x, offset.y + (self.height * yOffsets))
            self.pos2 = Vector2(-offset.x, offset.y + (self.height * (yOffsets + 1)))

    def draw(self, surface):
        surface.blit(self.surface, self.pos1)
        surface.blit(self.surface, self.pos2)