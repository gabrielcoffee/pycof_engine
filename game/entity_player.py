import mymath
from entity import Entity
from main import inputManager
from manager_input import keys
from pygame import Surface, Vector2, Rect
from sprite_animated import AnimatedSprite
from main import resourceManager

class Player(Entity):

    def init(self):
        self.tag = 'player'
        self.max_speed = 2
        self.acceleration = 0.1
        self.velocity = Vector2(0, 0)
        self.animation = AnimatedSprite(
            spritesheet=resourceManager.getTexture('anim1'),
            start_rect=Rect(0, 0, 8, 8),
            total_frames=4,
            frames_persec=3,
            is_back_and_forth=True
        )

    def update(self):

        # gets keys
        key_right = inputManager.isDown(keys.right)
        key_left = inputManager.isDown(keys.left)
        key_up = inputManager.isDown(keys.up)
        key_down = inputManager.isDown(keys.down)

        # handle movement
        moveX = (1 if key_right else 0) - (1 if key_left else 0)
        moveY = (1 if key_down else 0) - (1 if key_up else 0)

        # update acceleration
        if moveX != 0:
            self.velocity.x += moveX * self.acceleration
        else:
            self.velocity.x = mymath.aproxNum(self.velocity.x, 0, self.acceleration)
        if moveY != 0:
            self.velocity.y += moveY * self.acceleration
        else:
            self.velocity.y = mymath.aproxNum(self.velocity.y, 0, self.acceleration)

        # clamp velocity
        if self.velocity.x > self.max_speed:
            self.velocity.x = self.max_speed
        elif self.velocity.x < - self.max_speed:
            self.velocity.x = -self.max_speed

        if self.velocity.y > self.max_speed:
            self.velocity.y = self.max_speed
        elif self.velocity.y < - self.max_speed:
            self.velocity.y = -self.max_speed

        # add to the position
        self.pos.x += self.velocity.x
        self.pos.y += self.velocity.y

        self.animation.update()

    def draw(self, screen, cam_offset):

        # PLACEHOLDER
        placeholder = Surface(self.dim)
        placeholder.fill('green')
        screen.blit(placeholder, self.pos - cam_offset)

        self.animation.draw(self.pos.x, self.pos.y, screen, cam_offset)
