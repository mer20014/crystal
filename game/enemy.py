from game.actor import Actor
from game import constants
from game.point import Point

class Enemy(Actor):
    """The enemies. Monsters moving back and forth along platforms. 
    If colliding with player, player is put at the beginning of the level
    
    Args:
        self (Actor): an instance of Actor.
    """
    def __init__(self):
        super().__init__()
        self._width = 10
        self._height = 30
        self._image = constants.IMAGE_ENEMY_RED
        self._position = (Point(0,0))
        self._velocity = (Point(0,0))
        self._direction = "right"
        self._color = "red"