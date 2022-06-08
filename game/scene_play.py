from sprite_background import BackgroundSprite
from scene import Scene
from tile_levels import WorldLevels
from main import resourceManager, RESOLUTION
from pygame import Vector2
from tile import Tile

class PlayScene(Scene):
    def init(self, map_index):
        self.world_levels = WorldLevels()
        self.world_levels.addTileset(1, resourceManager.getTexture('tileset_grass'))
        self.world_levels.setupLevels('map' + str(map_index) + '.ldtk')

        # Level backgrounds
        self.backgrounds = []
        self.backgrounds.append(BackgroundSprite(resourceManager.getTexture('backg'), 30, 'x'))
        self.backgrounds.append(BackgroundSprite(resourceManager.getTexture('backg3'), 45, 'x'))
        self.backgrounds.append(BackgroundSprite(resourceManager.getTexture('backg2'), 60, 'x'))

    def update(self):

        player = self.getEntityByTag('player')
        cur_level = self.world_levels.getLevelByPosition(player.pos)
        self.cam_offset = self.getCameraOffset(entity_target=player, cur_level=cur_level)

        if cur_level is not None:
            for backg in self.backgrounds:
                backg.update(self.cam_offset)

    def draw(self, screen):

        screen.fill('lightblue')

        for backg in self.backgrounds:
            backg.draw(screen)

        self.world_levels.drawLayer('background', screen, self.cam_offset)

        for entity in self.entities:
            entity.draw(screen, self.cam_offset)

        self.world_levels.drawLayer('solids', screen, self.cam_offset)

    def getCameraOffset(self, entity_target, cur_level):

        # if no level is found
        if cur_level is None:
            return Vector2(entity_target.pos.x - RESOLUTION[0]//2 , entity_target.pos.y - RESOLUTION[1]//2)

        # entity_target position with DIM offset
        entity_target_x = entity_target.pos.x + entity_target.dim.x // 2
        entity_target_y = entity_target.pos.y + entity_target.dim.y // 2

        # screen width and height
        width = RESOLUTION[0]
        height = RESOLUTION[1]
        level_width = cur_level.cWidth * Tile.SIZE
        level_height = cur_level.cHeight * Tile.SIZE

        left_limit = cur_level.world_pos.x
        right_limit = cur_level.world_pos.x + level_width
        up_limit = cur_level.world_pos.y
        down_limit = cur_level.world_pos.y + level_height - Tile.SIZE//2

        # LEFT AND RIGHT
        if entity_target_x < left_limit + width // 2:
            x_offset = left_limit
        elif entity_target_x > right_limit - width // 2:
            x_offset = right_limit - width
        else:
            x_offset = entity_target_x - width // 2

        # LEFT AND UP LIMIT
        if entity_target_y < up_limit + height // 2:
            y_offset = up_limit
        elif entity_target_y > down_limit - height // 2:
            y_offset = down_limit - height
        else:
            y_offset = entity_target_y - height // 2

        return Vector2(x_offset, y_offset)