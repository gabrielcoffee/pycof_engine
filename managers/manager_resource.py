import pygame

class ResourceManager:
    def __init__(self):
        # resources are stored in dicts
        self.textures = {}
        self.fonts = {}

    # for textures

    def addTexture(self, key):
        self.textures[key] = pygame.image.load('Assets/Images/' + key + '.png').convert_alpha()

    def getTexture(self, key):
        if key not in self.textures.keys():
            print('============ERROR============')
            print('Image "' + key + '" not found')
            return None
        return self.textures[key]

    # for fonts

    def addFont(self, key, size):
        self.fonts[key] = pygame.font.Font('Assets/Fonts/' + key, size)

    def getFont(self, key):
        if key not in self.fonts.keys:
            print('Font "' + key + '" not found')
            return None
        return self.fonts[key]
