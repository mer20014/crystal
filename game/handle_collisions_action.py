import raylibpy
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
        self._level = 1

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
        finish = cast["finish"][0]
        win = cast["win"][0]

        for platform in platforms:
            if self._physics_service.is_collision(platform, player):
                x = player.get_position().get_x()
                y = player.get_position().get_y()
                px = platform.get_position().get_x()
                py = platform.get_position().get_y()
                dx = player.get_velocity().get_x()
                dy = player.get_velocity().get_y()
                # self._audio_service.start_audio()
                # self._audio_service.play_sound(constants.SOUND_PLATFORM)

                if x < px and y > py: 
                    # #If on left side of platform
                    x = x + (x - (px+5))
                    player.set_position(Point(x, y))
                    

                elif x > px + 1 + constants.PLATFORM_WIDTH and y > py:
                    #If on right
                    x = x - (x - px)
                    player.set_position(Point(x,y))

                elif y > py:
                    # #If underneath
                    # print(f"Before {y}")
                    player.set_position(Point(x, py + constants.PLATFORM_HEIGHT))
                    # player.set_position(Point(x, y))
                    # print(y)
                    
                
                elif py > y + constants.PLAYER_HEIGHT:
                    #On top
                    dy *= -5
                    player.set_velocity(Point(dx, dy))
                    # player.set_position(Point(x, y))
                    
                    self._gravity_action.jump(cast)

                else:
                    #if inside platform
                    player.set_position(Point(x, py - constants.PLAYER_HEIGHT))
                    
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
                    player.set_position(player._start_position)
                    print("death")

            for collision in collisions:
                if self._physics_service.is_collision(enemy, collision):
                    dx = enemy.get_velocity().get_x()
                    dx = dx * -1
                    enemy.set_velocity(Point(dx, 0))
                    # raylibpy.image_flip_horizontal(enemy._image)
                    #print("collision")

        if self._physics_service.is_collision(player, finish):
            self._level += 1
            if self._level == 2:
                player.set_position(Point(650,550))
                player._color = "red"
                player._image = constants.IMAGE_PLAYER_RED
                player._start_position = (Point(650,500))

                #Platform 1 position
                platforms[0].set_position(Point(600,540))
                collisions[0].set_position_1(platforms[0])
                collisions[1].set_position_2(platforms[0])

                #Platform 2 position
                platforms[1].set_position(Point(100,225))
                collisions[2].set_position_1(platforms[1])
                collisions[3].set_position_2(platforms[1])

                #platform 3 position
                platforms[2].set_position(Point(370, 450))
                collisions[4].set_position_1(platforms[2])
                collisions[5].set_position_2(platforms[2])

                #platform 4 position
                platforms[3].set_position(Point(170, 350))
                collisions[6].set_position_1(platforms[3])
                collisions[7].set_position_2(platforms[3])

                #platform 5 position
                platforms[4].set_position(Point(440,225))
                collisions[8].set_position_1(platforms[4])
                collisions[9].set_position_2(platforms[4])

                #tall platform
                platforms[5].set_position(Point(0,0))
                platforms[5]._image = constants.IMAGE_COLLISION

                finish.set_position(Point(600,185))

                #Red enemy
                enemies[0].set_position(Point(300, 310))

                #Blue enemy
                enemies[1].set_position(Point(500, 185))

                #Red crystal
                crystals[0].set_position(Point(610, 500))

                #Blue crystal
                crystals[1].set_position(Point(400,410))

            elif self._level == 3:
                player.set_position(Point(300,300))
                player._color = "blue"
                player._image = constants.IMAGE_PLAYER_BLUE
                player._start_position = (Point(300,300))

                #Platform 1 position
                platforms[0].set_position(Point(230,300))
                collisions[0].set_position_1(platforms[0])
                collisions[1].set_position_2(platforms[0])

                #Platform 2 position
                platforms[1].set_position(Point(100,475))
                collisions[2].set_position_1(platforms[1])
                collisions[3].set_position_2(platforms[1])

                #platform 3 position
                platforms[2].set_position(Point(350, 475))
                collisions[4].set_position_1(platforms[2])
                collisions[5].set_position_2(platforms[2])

                #platform 4 position
                platforms[3].set_position(Point(500, 380))
                collisions[6].set_position_1(platforms[3])
                collisions[7].set_position_2(platforms[3])

                # #platform 5 position
                platforms[4].set_position(Point(500,380))
                collisions[8].set_position_1(platforms[4])
                collisions[9].set_position_2(platforms[4])

                #tall platform
                platforms[5].set_position(Point(350, 100))
                platforms[5]._image = constants.IMAGE_PLATFORM_TALL

                finish.set_position(Point(380,260))

                #Red enemy
                enemies[0].set_position(Point(120, 435))

                #Blue enemy
                enemies[1]._image = constants.IMAGE_COLLISION
                enemies[1].set_position(Point(0, 0))

                #Blue crystal
                crystals[1].set_position(Point(240, 260))

                #Red crystal
                crystals[0].set_position(Point(320,260))
                print(self._level)

            elif self._level == 4:
                win._image = constants.IMAGE_WIN
                
