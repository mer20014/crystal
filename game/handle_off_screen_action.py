from game.action import Action
from game.point import Point
from game import constants

class HandleOffScreenAction(Action):
    """A code template for handling collisions with the screen. The responsibility 
    of this class of objects is to update the game state when actors collide with the border.
    
    Stereotype:
        Controller
    """
    def __init__(self, sound_service):
        super().__init__()
        self._sound_service = sound_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        pass