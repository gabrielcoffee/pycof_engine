from pygame import Rect, Vector2

from tile import Tile

class TilemapCollider:
    def __init__(self, width, height, tilemap):
        self.width = width
        self.height = height
        self.tilemap = tilemap

    def isCollidingTiles(self, X, Y):
        rect_center = Vector2(X + self.width // 2, Y + self.height // 2)

        for tile in self.tilemap:
            tile_center = Vector2(tile.position.x + Tile.SIZE//2, tile.position.Y + Tile.SIZE//2)

            # if distance between centers are smaller than the width or height it can check collision with the tile
            if abs(tile_center.x - rect_center.x) < self.width and abs(tile_center.y - rect_center.y) < self.height:
                if Rect(X, Y, self.width, self.height).contains(tile.hitbox):
                    return True

        # not colliding with anything
        return False