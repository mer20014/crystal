import raylibpy
from game.action import Action
from game import constants
from game.point import Point

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """
    def __init__(self, input_service):
        super().__init__() 
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        jump_timer = 0
        direction = self._input_service.get_direction()
        player = cast["player"][0]

        # x = player.get_velocity().get_x()
        # y = player.get_velocity().get_y()
        # jump = False

        # if self._input_service.is_up_pressed():
        #     jump = True
        #     jump_timer += 1
        #     dy = y + -3
        #     player.set_velocity(Point(x, dy))
        #     print(jump_timer)
        #     if jump_timer > 80 and jump is True:
        #         player.set_velocity(Point(x,y))
        #         jump = False

        player.set_velocity(direction.scale(constants.PLAYER_SPEED))