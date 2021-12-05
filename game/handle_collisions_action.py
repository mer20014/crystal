from game.action import Action
from game import collision, constants, physics_service
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self, physics_service, audio_service, gravity_action):
        super().__init__()
        self._physics_service = physics_service
        self._audio_service = audio_service
        self._gravity_action = gravity_action

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        player = cast["player"][0]
        platforms = cast["platforms"]
        crystals = cast["crystals"]
        enemies = cast["enemies"]
        collisions = cast["collisions"]

        for platform in platforms:
            if self._physics_service.is_collision(platform, player):
                x = player.get_position().get_x()
                y = player.get_position().get_y()
                px = platform.get_position().get_x()
                py = platform.get_position().get_y()
                dx = player.get_velocity().get_x()
                dy = player.get_velocity().get_y()

                if x < px and y > py: 
                    # #If on left side of platform
                    x = x + (x - (px+5))
                    player.set_position(Point(x, y))
                    

                # elif x > px + constants.PLATFORM_WIDTH and y > py:
                #     x = x - (x - px)
                #     player.set_position(Point(x,y))

                elif y > py:
                    # #If underneath
                    # print(f"Before {y}")
                    # y = y + (y - py)
                    # player.set_position(Point(x, y))
                    # print(y)
                    pass

                
                else:
                    #On top
                    dy *= -5
                    player.set_velocity(Point(dx, dy))
                    player.set_position(Point(x, y -4))
                    #print(y-2)
                    
                    self._gravity_action.jump(cast)

            elif not self._physics_service.is_collision(player, platform):
                self._gravity_action.execute(cast)

            

        for crystal in crystals:
            if self._physics_service.is_collision(crystal, player):
                if crystal._color == "red" and player._color == "blue":
                    player._color = "red"
                    player._image = constants.IMAGE_PLAYER_RED
                    #print("red")

                elif crystal._color == "blue" and player._color == "red":
                    player._color = "blue"
                    player._image = constants.IMAGE_PLAYER_BLUE
                    #print("blue")

        for enemy in enemies:
            if self._physics_service.is_collision(enemy, player):
                if enemy._color == "red" and player._color == "blue" or enemy._color == "blue" and player._color == "red":
                    player.set_position(Point(0,0))
                    #print("death")

            for collision in collisions:
                if self._physics_service.is_collision(enemy, collision):
                    dx = enemy.get_velocity().get_x()
                    dx = dx * -1
                    enemy.set_velocity(Point(dx, 0))
                    #print("collision")