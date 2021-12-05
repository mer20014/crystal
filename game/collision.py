from game.actor import Actor
from game import constants
from game.point import Point

class Collision(Actor):
    def __init__(self):
        super().__init__()
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
        self._width = constants.COLLISION_WIDTH
        self._height = constants.COLLISION_HEIGHT
        self._image = constants.IMAGE_COLLISION