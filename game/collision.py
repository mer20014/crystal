from game.actor import Actor
from game import constants
from game.point import Point

class Collision(Actor):
    """Invisible walls for tracking collisions w/ the enemies and edge of platforms
    
    Args:
        self (Actor): an instance of Actor.
    """
        
    def __init__(self):
        super().__init__()
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
        self._width = constants.COLLISION_WIDTH
        self._height = constants.COLLISION_HEIGHT
        self._image = constants.IMAGE_COLLISION

    def set_position_1(self,platform):
        self._position = Point(platform.get_position().get_x(), platform.get_position().get_y() - constants.COLLISION_HEIGHT-20)

    def set_position_2(self, platform):
        self._position = Point(platform.get_position().get_x() + constants.PLATFORM_WIDTH, platform.get_position().get_y() - constants.COLLISION_HEIGHT-20)