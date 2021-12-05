from game.action import Action
from game.level import Level
import raylibpy

class HandleLevelAction(Action):
    """A code template for handling levels. The responsibility of this class of objects is to update the score when bricks are destroyed
    
    Stereotype:
        Controller
    """
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service
        self.level = Level()

    def execute(self,cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        player = cast["player"][0]
        finish = cast["finish"][0]
        
        if self._physics_service.is_collision(player, finish):
            
            self.level.set_level(self.level._level + 1)
            print(self.level._level)