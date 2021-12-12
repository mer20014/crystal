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
        player = cast["player"][0]
        x = player.get_position().get_x()
        y = player.get_position().get_y()
        dx = player.get_velocity().get_x()
        dy = player.get_velocity().get_y()

        if x >= constants.MAX_X - 20:
            #collide on right side of screen
            x = x + (x - (dx))
            player.set_position(Point(x, y))

        elif x <= 1:
            #Collide on left side of screen
            x = x - (x + (dx))
            player.set_position(Point(x, y))
            print("hit")

        elif y >= constants.MAX_Y - 20:
            #collides w/ bottom of screen
            player.set_position(player._start_position)
            