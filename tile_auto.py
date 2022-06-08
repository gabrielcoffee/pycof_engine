from tile import Tile
import pygame

class AutoTile(Tile):

    def __init__(self, pos, world_pos, tileset, map, map_width, map_height):
        index = self.getIndexValue(int(pos.x), int(pos.y), map, map_width, map_height)
        source_rect = self.source_rects[index]

        self.pos = (world_pos.x + pos.x * Tile.SIZE, world_pos.y + pos.y * Tile.SIZE)
        self.texture = tileset.subsurface(source_rect)

    def draw(self, screen : pygame.Surface, cam_offset):
        screen.blit(self.texture, self.pos - cam_offset)

    def getIndexValue(self, x, y, map, map_width, map_height):

        nw, n, ne, w, e, sw, s, se = 0, 0, 0, 0, 0, 0, 0, 0
        addX, addY, remX, remY = 1, 1, 1, 1

        # remove offset from borders
        if x == 0:
            remX = 0
        if x == map_width-1:
            addX = 0
        if y == 0:
            remY = 0
        if y == map_height-1:
            addY = 0

        # CARDINAL TILES (NORTH, WEST, EAST, SOUTH)
        if map[x + (y - remY) * map_width] != 0: n = 1
        if map[(x - remX) + y * map_width] != 0: w = 1
        if map[(x + addX) + y * map_width] != 0: e = 1
        if map[x + (y + addY) * map_width] != 0: s = 1

        # MAP BORDERS
        if x == 0:
            w = 1
        elif x == map_width-1:
            e = 1
        if y == 0:
            n = 1
        elif y == map_height-1:
            s = 1

        # CORNER TILES NORTH
        if map[(x - remX) + (y - remY) * map_width] != 0 and n == 1 and w == 1:
            nw = 1
        if map[(x + addX) + (y - remY) * map_width] != 0 and n == 1 and e == 1:
            ne = 1

        # CORNER TILES SOUTH
        if map[(x - remX) + (y + addY) * map_width] != 0 and s == 1 and w == 1:
            sw = 1
        if map[(x + addX) + (y + addY) * map_width] != 0 and s == 1 and e == 1:
            se = 1

        value_sum = (nw * 1) + (n * 2) + (ne * 4) + (w * 8) + (e * 16) + (sw * 32) + (s * 64) + (se * 128)

        # removing redundancies
        if value_sum in self.index_dict.keys():
            value_sum = self.index_dict[value_sum]

        return value_sum

    index_dict = {
        2 : 1, 8 : 2, 10 : 3, 11 : 4, 16 : 5, 18 : 6, 22 : 7, 24 : 8,
        26 : 9, 27 : 10, 30 : 11, 31 : 12, 64 : 13, 66 : 14, 72 : 15,
        74 : 16, 75 : 17, 80 : 18, 82 : 19, 86 : 20, 88 : 21, 90 : 22,
        91 : 23, 94 : 24, 95 : 25, 104 : 26, 106 : 27, 107 : 28,
        120 : 29, 122 : 30, 123 : 31, 126 : 32, 127 : 33, 208 : 34,
        210 : 35, 214 : 36, 216 : 37, 218 : 38, 219 : 39, 222 : 40,
        223 : 41, 248 : 42, 250 : 43, 251 : 44, 254 : 45, 255 : 46, 0 : 47
    }

    source_rects = {}
    for x in range(8):
        for y in range(6):
            source_rects[x + (y * 8)] = pygame.Rect(
                x * Tile.SIZE,
                y * Tile.SIZE,
                Tile.SIZE,
                Tile.SIZE
            )
