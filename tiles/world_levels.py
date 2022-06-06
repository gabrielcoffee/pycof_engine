import json
from tiles.tile_auto import AutoTile
from tiles.tile import Tile
from pygame import Vector2, Rect

class WorldLevels:
    def __init__(self):
        self.cur_level = 0
        self.levels = []
        self.tilesets = {}

    def drawLayer(self, layer, screen, cam_offset):

        if layer == 'solids':
            for level in self.levels:
                level.drawSolidTiles(screen, cam_offset)
        elif layer == 'background':
            for level in self.levels:
                level.drawSolidTiles(screen, cam_offset)

    def addTileset(self, index, texture):
        self.tilesets[index] = texture

    def getLevelByPosition(self, position : Vector2):
        for level in self.levels:
            if level.level_rect.contains(Rect(position.x, position.y, 1, 1)):
                return level

    def setupLevels(self, map_url):
        # get map data by url
        with open('Assets/WorldMaps/' + map_url, 'r') as data:
            map_data = json.load(data)

        # get levels data
        for level in map_data['levels']:
            level_id = int(level['identifier'].replace('Level_', ''))
            world_pos = Vector2(level['worldX'], level['worldY'])
            cWidth = level['layerInstances'][0]['__cWid']
            cHeight = level['layerInstances'][0]['__cHei']

            # tiles data map
            solid_map = level['layerInstances'][0]['intGridCsv']
            backg_map = level['layerInstances'][1]['intGridCsv']

            # actual tiles list
            solid_tiles = [None] * (cWidth * cHeight)
            backg_tiles = [None] * (cWidth * cHeight)

            for x in range(cWidth):
                for y in range(cHeight):
                    # get current tile
                    cur_solid_data = solid_map[x + (y * cWidth)]
                    cur_backg_data = backg_map[x + (y * cWidth)]

                    # define AUTOTILES for each layer

                    if cur_solid_data != 0:
                        solid_tiles[x + (y * cWidth)] = AutoTile(
                            pos = Vector2(x, y), world_pos = world_pos,
                            tileset = self.tilesets[cur_solid_data],
                            map = solid_map, map_width = cWidth, map_height = cHeight
                        )

                    if cur_backg_data != 0:
                        backg_tiles[x + (y * cWidth)] = AutoTile(
                            pos = Vector2(x, y), world_pos = world_pos,
                            tileset = self.tilesets[cur_backg_data],
                            map = backg_map, map_width = cWidth, map_height = cHeight)

            # add level to list of levels
            self.levels.append(
                Level(
                    level_id,
                    world_pos,
                    solid_tiles,
                    backg_tiles,
                    cWidth,
                    cHeight))

class Level:
    def __init__(self, level_id, world_pos, solid_tiles, backg_tiles, cWidth, cHeight):
        self.level_id = level_id
        self.world_pos = world_pos
        self.solid_tiles = solid_tiles
        self.backg_tiles = backg_tiles
        self.cWidth = cWidth
        self.cHeight = cHeight
        self.level_rect = Rect(world_pos.x, world_pos.y, cWidth * Tile.SIZE, cHeight * Tile.SIZE)

    def drawSolidTiles(self, screen, cam_offset):
        for tile in self.solid_tiles:
            if tile != None:
                tile.draw(screen, cam_offset)

    def drawBackgTiles(self, screen, cam_offset):
        for tile in self.backg_tiles:
            if tile != None:
                tile.draw(screen, cam_offset)

