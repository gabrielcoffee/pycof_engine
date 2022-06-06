import pygame
# base scene class
class Scene:
    def __init__(self):
        self.entities = []
        self.frame = 0

    def _update(self):
        self.frame += 1
        for entity in self.entities:
            entity.update()
        self.update()

    def _draw(self, screen):
        self.draw(screen)

    def update(self):
        pass

    def draw(self, screen):
        pass

    def addEntity(self, entity):
        self.entities.append(entity)
        entity.onAddedToScene()

    def deleteEntity(self, entity):
        entity.onRemovedFromScene()
        self.entities.remove(entity)

    def addTilemap(self, tilemap):
        self.tilemaps.append(tilemap)

    def deleteTilemap(self, tilemap):
        self.tilemaps.pop(tilemap)

    def getEntityByTag(self, tag):
        for e in self.entities:
            if e.tag == tag:
                return e
            else:
                return None
