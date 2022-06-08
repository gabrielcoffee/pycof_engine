class SceneManager:
    def __init__(self):
        self.scenes = {}
        self.curScene = ''

    def storeScene(self, key, scene):
        self.scenes[key] = scene

        if len(self.scenes.values()) == 1:
            self.setCurrentScene(key)

    def setCurrentScene(self, key):
        if key in self.scenes.keys():
            self.curScene = key

    def update(self):
        self.scenes[self.curScene]._update()

    def draw(self, screen):
        self.scenes[self.curScene]._draw(screen)