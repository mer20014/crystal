from game.action import Action
import raylibpy

class HandleLevelAction(Action):
    """A code template for handling levels. The responsibility of this class of objects is to update the score when bricks are destroyed
    
    Stereotype:
        Controller
    """
    def __init__(self, output_service):
        super().__init__()
        self._output_service = output_service


    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        pass