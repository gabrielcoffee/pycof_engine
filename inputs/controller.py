import pygame

# stores information about input for controllers

class Controller:

    def __init__(self, number):
        self.number = number
        self.joystick = None
        if number <= pygame.joystick.get_count() - 1:
            self.joystick = pygame.joystick.Joystick(number)
            self.joystick.init()
            self.name = self.joystick.get_name()

        self.previousButtons = None
        self.currentButtons = None

        self.previousAxes = None
        self.currentAxes = None

        self.previousHats = None
        self.currentHats = None

    def updateInput(self):
        if self.joystick is None:
            return

        # handle buttons

        self.previousButtons = self.currentButtons
        self.currentButtons = []
        for b in range(self.joystick.get_numbuttons()):
            self.currentButtons.append(self.joystick.get_button(b))

        self.previousAxes = self.currentAxes
        self.currentAxes = []
        for a in range(self.joystick.get_numaxes()):
            self.currentAxes.append(self.joystick.get_axis(a))

        self.previousHats = self.currentHats
        self.currentHats = []
        for h in range(self.joystick.get_numhats()):
            self.currentHats.append(self.joystick.get_hat(h))

    def isButtonDown(self, controllerInput):
        if self.currentButtons is None:
            return False
        if len(self.currentButtons) <= controllerInput.inputNumber:
            return False
        return self.currentButtons[controllerInput.inputNumber] >= controllerInput.threshold

    def isButtonPressed(self, controllerInput):
        if self.currentButtons is None or self.previousButtons is None:
            return False
        if len(self.currentButtons) <= controllerInput.inputNumber:
            return False
        return self.currentButtons[controllerInput.inputNumber] >= controllerInput.threshold and self.previousButtons[
            controllerInput.inputNumber] < controllerInput.threshold

    def isButtonReleased(self, controllerInput):
        if len(self.currentButtons) <= controllerInput.inputNumber:
            return False
        if self.currentButtons is None or self.previousButtons is None:
            return False
        return self.currentButtons[controllerInput.inputNumber] <= controllerInput.threshold and self.previousButtons[
            controllerInput.inputNumber] > controllerInput.threshold

    def isHatDown(self, controllerInput):
        if self.currentHats is None:
            return False
        if len(self.currentHats) <= controllerInput.inputNumber[0]:
            return False
        if controllerInput.threshold > 0:
            return self.currentHats[controllerInput.inputNumber[0]][
                       controllerInput.inputNumber[1]] >= controllerInput.threshold
        else:
            return self.currentHats[controllerInput.inputNumber[0]][
                       controllerInput.inputNumber[1]] <= controllerInput.threshold

    def isHatPressed(self, controllerInput):
        if self.currentHats is None or self.previousHats is None:
            return False
        if len(self.currentHats) <= controllerInput.inputNumber[0]:
            return False
        if controllerInput.threshold > 0:
            return self.currentHats[controllerInput.inputNumber[0]][
                       controllerInput.inputNumber[1]] >= controllerInput.threshold and \
                   self.previousHats[controllerInput.inputNumber[0]][
                       controllerInput.inputNumber[1]] < controllerInput.threshold
        else:
            return self.currentHats[controllerInput.inputNumber[0]][
                       controllerInput.inputNumber[1]] <= controllerInput.threshold and \
                   self.previousHats[controllerInput.inputNumber[0]][
                       controllerInput.inputNumber[1]] > controllerInput.threshold

    def isHatReleased(self, controllerInput):
        if self.currentHats is None or self.previousHats is None:
            return False
        if len(self.currentHats) <= controllerInput.inputNumber[0]:
            return False
        if controllerInput.threshold > 0:
            return self.currentHats[controllerInput.inputNumber[0]][
                       controllerInput.inputNumber[1]] < controllerInput.threshold and \
                   self.previousHats[controllerInput.inputNumber[0]][
                       controllerInput.inputNumber[1]] >= controllerInput.threshold
        else:
            return self.currentHats[controllerInput.inputNumber[0]][
                       controllerInput.inputNumber[1]] > controllerInput.threshold and \
                   self.previousHats[controllerInput.inputNumber[0]][
                       controllerInput.inputNumber[1]] <= controllerInput.threshold

    def isAxisDown(self, controllerInput):
        if self.currentAxes is None:
            return False
        if len(self.currentAxes) <= controllerInput.inputNumber:
            return False
        if controllerInput.threshold > 0:
            return self.currentAxes[controllerInput.inputNumber] >= controllerInput.threshold
        else:
            return self.currentAxes[controllerInput.inputNumber] <= controllerInput.threshold

    def isAxisPressed(self, controllerInput):
        if self.currentAxes is None or self.previousAxes is None:
            return False
        if len(self.currentAxes) <= controllerInput.inputNumber:
            return False
        if controllerInput.threshold > 0:
            return self.currentAxes[controllerInput.inputNumber] >= controllerInput.threshold and self.previousAxes[
                controllerInput.inputNumber] < controllerInput.threshold
        else:
            return self.currentAxes[controllerInput.inputNumber] <= controllerInput.threshold and self.previousAxes[
                controllerInput.inputNumber] > controllerInput.threshold

    def isAxisReleased(self, controllerInput):
        if self.currentAxes is None or self.previousAxes is None:
            return False
        if len(self.currentAxes) <= controllerInput.inputNumber:
            return False
        if controllerInput.threshold > 0:
            return self.currentAxes[controllerInput.inputNumber] < controllerInput.threshold and self.previousAxes[
                controllerInput.inputNumber] >= controllerInput.threshold
        else:
            return self.currentAxes[controllerInput.inputNumber] > controllerInput.threshold and self.previousAxes[
                controllerInput.inputNumber] <= controllerInput.threshold