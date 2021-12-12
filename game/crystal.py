from game.actor import Actor
from game import constants
from game.point import Point

class Crystal(Actor):
    def __init__(self):
        """The crystals. They change the color status of the player on collision
        
        Args:
            self (Actor): an instance of Actor.
        """
        super().__init__()
        self._width = constants.CRYSTAL_WIDTH
        self._height = constants.CRYSTAL_HEIGHT
        self._image = constants.IMAGE_CRYSTAL_RED
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
        self._color = "red"
    