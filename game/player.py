from game.actor import Actor
from game import constants
from game.point import Point

class Player(Actor):
    def __init__(self):
        super().__init__()
        self._width = constants.PLAYER_WIDTH
        self._height = constants.PLAYER_HEIGHT
        self._image = constants.IMAGE_PLAYER_BLUE
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
        self._color = ""
        # self._is_gravity_affected = True

    # def change_color(self):
    #     if self._color == "red":
    #         self.set_image = constants.IMAGE_PLAYER_RED

    #     elif self._color == "blue":
    #         self.set_image = constants.IMAGE_PLAYER_BLUE