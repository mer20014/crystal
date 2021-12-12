from game.actor import Actor
from game.point import Point
from game import constants

class Win(Actor):
    """
    Number that tells the player how well they are doing

    Stereotype: Information Holder

    Attributes:
    _text (string): The default text
    _position (Point): The default position
    _velocity (Point): Default movement
    _score (int): The starting score value
    """

    def __init__(self):
        """The image that appears if the player wins
        
        Args:
            self (Actor): an instance of Actor.
        """
        super().__init__()

        self._image = ""
        self._position = Point(250,150)
        self._velocity = Point(0,0)
        self._score = 0

