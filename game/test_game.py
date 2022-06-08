import main

from scene_play import PlayScene
from game.entity_player import Player
from main import resourceManager

# resources
resourceManager.addTexture('tileset_grass')
resourceManager.addTexture('anim1')
resourceManager.addTexture('backg')
resourceManager.addTexture('backg2')
resourceManager.addTexture('backg3')

# scenes
mainScene = PlayScene()
mainScene.init(map_index=1)
player = Player(x=0, y=0, width=8, height=8)
mainScene.addEntity(player)
main.sceneManager.storeScene('main', mainScene)

# start the game
main.run()