from game.actor import Actor
from game.point import Point
from game import constants

class Finish(Actor):
    def __init__(self):
        super().__init__()
        self._width = constants.FINISH_WIDTH
        self._height = constants.FINISH_HEIGHT
        self._image = constants.IMAGE_FINISH
        self._level = 0