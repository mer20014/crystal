from game.actor import Actor
from game import constants
from game.point import Point

class Platform(Actor):
    def __init__(self):
        super().__init__()
        self._width = constants.PLATFORM_WIDTH
        self._height = constants.PLATFORM_HEIGHT
        self._image = constants.IMAGE_PLATFORM
        self._position = Point(0,0)