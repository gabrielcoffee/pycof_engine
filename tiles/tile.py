import pygame

class Tile:
    SIZE = 8

    def __init__(self, position, texture):
        self.position = position
        self.surface = texture

    def draw(self, surface):
        surface.blit(self.surface, self.position)