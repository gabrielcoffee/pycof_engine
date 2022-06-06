import pygame

# stores information about keys being pressed

class Keyboard:
    def __init__(self):
        self.currentKeyboard = None
        self.previousKeyboard = None

    def updateInput(self):
        self.previousKeyboard = self.currentKeyboard
        self.currentKeyboard = pygame.key.get_pressed()

    # key states

    def isKeyDown(self, keyCode):
        if self.currentKeyboard is None or self.previousKeyboard is None:
            return False
        return self.currentKeyboard[keyCode] == True

    def isKeyPressed(self, keyCode):
        if self.currentKeyboard is None or self.previousKeyboard is None:
            return False
        return self.currentKeyboard[keyCode] == True and self.previousKeyboard[keyCode] == False

    def isKeyReleased(self, keyCode):
        if self.currentKeyboard is None or self.previousKeyboard is None:
            return False
        return self.currentKeyboard[keyCode] == False and self.previousKeyboard[keyCode] == True