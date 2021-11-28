from game.actor import Actor
from game import constants
from game.point import Point

class Player(Actor):
    def __init__(self):
        super().__init__()
        self._width = constants.PLAYER_WIDTH
        self._height = constants.PLAYER_HEIGHT
        self._image = constants.IMAGE_PLAYER_BLUE
        self._position = Point(100, 200)
