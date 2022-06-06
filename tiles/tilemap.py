from tiles.tile import Tile

class TileMap:
    def __init__(self, width, height, tiles_data, tileset = None):
        self.width = width
        self.height = height
        self.tiles_data = tiles_data
        self.tileset = tileset

        self.textures = {}
        self.map = [None] * (self.width * self.height)

    # draws every tile
    def draw(self, surface):
        for tile in self.map:
            if tile is not None:
                tile.draw(surface)

    # define texture for each index in the tilemap
    def defineTexture(self, index, source_rect):
        self.textures[index] = self.tileset.subsurface(source_rect)

    # set each tile for the map
    def generateMap(self):

        for x in range(self.width):
            for y in range(self.height):

                cur_tile_data = self.tiles_data[x + (y*self.width)]

                # skips empty tiles
                if cur_tile_data == 0:
                    continue

                # adds tiles to map list
                position = (x * Tile.SIZE, y * Tile.SIZE)
                texture = self.textures[cur_tile_data]

                self.map[x + (y * self.width)] = Tile(position, texture)