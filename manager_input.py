from input_keyboard import *
from input_controller import *

# stores information the input

class PlayerInput:
    def __init__(self, controllerNumber, inputNumber, type, threshold):
        self.controllerNumber = controllerNumber
        self.inputNumber = inputNumber
        self.type = type
        self.threshold = threshold

# stores input from the player keyboard/controller
class InputManager:
    def __init__(self):
        self.keyboard = Keyboard()
        pygame.joystick.init()
        self.controllers = [Controller(i) for i in range(4)]

    def updateInput(self):
        self.keyboard.updateInput()
        for c in self.controllers:
            c.updateInput()

    def numOfControllers(self):
        return pygame.joystick.get_count()

    def isDown(self, player_input):
        if player_input is None:
            return False
        if player_input.type == 'button':
            return self.controllers[player_input.controllerNumber].isButtonDown(player_input)
        if player_input.type == 'hat':
            return self.controllers[player_input.controllerNumber].isHatDown(player_input)
        if player_input.type == 'axis':
            return self.controllers[player_input.controllerNumber].isAxisDown(player_input)
        if player_input.type == 'key':
            return self.keyboard.isKeyDown(player_input.inputNumber)

    def isPressed(self, player_input):
        if player_input is None:
            return False
        if player_input.type == 'button':
            return self.controllers[player_input.controllerNumber].isButtonPressed(player_input)
        if player_input.type == 'hat':
            return self.controllers[player_input.controllerNumber].isHatPressed(player_input)
        if player_input.type == 'axis':
            return self.controllers[player_input.controllerNumber].isAxisPressed(player_input)
        if player_input.type == 'key':
            return self.keyboard.isKeyPressed(player_input.inputNumber)

    def isReleased(self, player_input):
        if player_input is None:
            return False
        if player_input.type == 'button':
            return self.controllers[player_input.controllerNumber].isButtonReleased(player_input)
        if player_input.type == 'hat':
            return self.controllers[player_input.controllerNumber].isHatReleased(player_input)
        if player_input.type == 'axis':
            return self.controllers[player_input.controllerNumber].isAxisReleased(player_input)
        if player_input.type == 'key':
            return self.keyboard.isKeyReleased(player_input.inputNumber)

# inputs

class KeyInput:
    def __init__(self):
        self.enter = PlayerInput(0, pygame.K_RETURN, 'key', 1)
        self.esc = PlayerInput(0, pygame.K_ESCAPE, 'key', 1)

        self.up = PlayerInput(0,pygame.K_UP,'key',1)
        self.down = PlayerInput(0,pygame.K_DOWN,'key',1)
        self.left = PlayerInput(0,pygame.K_LEFT,'key',1)
        self.right = PlayerInput(0,pygame.K_RIGHT,'key',1)

        self.a = PlayerInput(0, pygame.K_a, 'key', 1)
        self.b = PlayerInput(0, pygame.K_b, 'key', 1)
        self.c = PlayerInput(0, pygame.K_c, 'key', 1)
        self.d = PlayerInput(0, pygame.K_d, 'key', 1)
        self.e = PlayerInput(0, pygame.K_e, 'key', 1)
        self.f = PlayerInput(0, pygame.K_f, 'key', 1)
        self.g = PlayerInput(0, pygame.K_g, 'key', 1)
        self.h = PlayerInput(0, pygame.K_h, 'key', 1)
        self.i = PlayerInput(0, pygame.K_i, 'key', 1)
        self.j = PlayerInput(0, pygame.K_j, 'key', 1)
        self.k = PlayerInput(0, pygame.K_k, 'key', 1)
        self.l = PlayerInput(0, pygame.K_l, 'key', 1)
        self.m = PlayerInput(0, pygame.K_m, 'key', 1)
        self.n = PlayerInput(0, pygame.K_n, 'key', 1)
        self.o = PlayerInput(0, pygame.K_o, 'key', 1)
        self.p = PlayerInput(0, pygame.K_p, 'key', 1)
        self.q = PlayerInput(0, pygame.K_q, 'key', 1)
        self.r = PlayerInput(0, pygame.K_r, 'key', 1)
        self.s = PlayerInput(0, pygame.K_s, 'key', 1)
        self.t = PlayerInput(0, pygame.K_t, 'key', 1)
        self.u = PlayerInput(0, pygame.K_u, 'key', 1)
        self.v = PlayerInput(0, pygame.K_v, 'key', 1)
        self.w = PlayerInput(0, pygame.K_w, 'key', 1)
        self.x = PlayerInput(0, pygame.K_x, 'key', 1)
        self.y = PlayerInput(0, pygame.K_y, 'key', 1)
        self.z = PlayerInput(0, pygame.K_z, 'key', 1)

        self.n0 = PlayerInput(0, pygame.K_0, 'key', 1)
        self.n1 = PlayerInput(0, pygame.K_1, 'key', 1)
        self.n2 = PlayerInput(0, pygame.K_2, 'key', 1)
        self.n3 = PlayerInput(0, pygame.K_3, 'key', 1)
        self.n4 = PlayerInput(0, pygame.K_4, 'key', 1)
        self.n5 = PlayerInput(0, pygame.K_5, 'key', 1)
        self.n6 = PlayerInput(0, pygame.K_6, 'key', 1)
        self.n7 = PlayerInput(0, pygame.K_7, 'key', 1)
        self.n8 = PlayerInput(0, pygame.K_8, 'key', 1)
        self.n9 = PlayerInput(0, pygame.K_9, 'key', 1)

keys = KeyInput()

class ControllerInput:
    def __init__(self, number):

        self.a = PlayerInput(number, 0, 'button', 1)
        self.b = PlayerInput(number, 1, 'button', 1)
        self.x = PlayerInput(number, 2, 'button', 1)
        self.y = PlayerInput(number, 3, 'button', 1)

        self.L1 = PlayerInput(number, 4, 'button', 1)
        self.R1 = PlayerInput(number, 5, 'button', 1)

        self.select = PlayerInput(number, 6, 'button', 1)
        self.start = PlayerInput(number, 7, 'button', 1)

        self.L2 = PlayerInput(number, 2, 'axis', 0.1)
        self.L2 = PlayerInput(number, 5, 'axis', 0.1)

        self.dpad_left = PlayerInput(number, (0, 0), 'hat', -1)
        self.dpad_right = PlayerInput(number, (0, 0), 'hat', 1)
        self.dpad_up = PlayerInput(number, (0, 1), 'hat', 1)
        self.dpad_down = PlayerInput(number, (0, 1), 'hat', -1)

        self.lstick_left = PlayerInput(number, 0, 'axis', -0.2)
        self.lstick_right = PlayerInput(number, 0, 'axis', 0.2)
        self.lstick_up = PlayerInput(number, 1, 'axis', -0.2)
        self.lstick_down = PlayerInput(number, 1, 'axis', 0.2)

        self.rstick_left = PlayerInput(number, 3, 'axis', -0.2)
        self.rstick_right = PlayerInput(number, 3, 'axis', 0.2)
        self.rstick_up = PlayerInput(number, 4, 'axis', -0.2)
        self.rstick_down = PlayerInput(number, 4, 'axis', 0.2)

controller = [ControllerInput(i) for i in range(4)]