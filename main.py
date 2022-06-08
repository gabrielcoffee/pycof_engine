import pygame
from manager_scene import SceneManager
from manager_input import InputManager
from manager_resource import ResourceManager

pygame.init()

# constants
RESOLUTION = (320, 180)
SCREEN = pygame.display.set_mode(RESOLUTION, flags=pygame.SCALED)
CAPTION = 'MY ECS PYGAME'
SCALE = 1 # doesn't work yet
FPS = 60

# managers
sceneManager = SceneManager()
resourceManager = ResourceManager()
inputManager = InputManager()

def run():

    # create clock and caption for the game
    CLOCK = pygame.time.Clock()
    pygame.display.set_caption(CAPTION)

    # game loop
    running = True
    while running:

        # Handling events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        SCREEN.fill((15, 15, 15))

        inputManager.updateInput()

        sceneManager.update()
        sceneManager.draw(SCREEN)

        pygame.display.update()
        CLOCK.tick(FPS)

    # quit game
    pygame.quit()