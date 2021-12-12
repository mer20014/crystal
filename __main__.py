import random
import os

import raylibpy
from game import constants
from game.director import Director
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService

from game.player import Player
from game.platform import Platform
from game.enemy import Enemy
from game.crystal import Crystal
from game.collision import Collision
from game.finish import Finish
from game.level import Level
from game.win import Win
from game.gravity_action import GravityAction
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_off_screen_action import HandleOffScreenAction
from game.move_actors_action import MoveActorsAction

def main():

    #Define the differences services used
    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()
    gravity_action = GravityAction()

    level = Level()
    current_level = level.get_level()

    # create the cast {key: tag, value: list}
    cast_1 = {}

    #Create and add the player
    cast_1["player"] = []
    players = []

    cast_1["crystals"] = []
    crystals = []

    cast_1["enemies"] = []
    enemies = []

    cast_1["finish"] = []
    finishes = []

    player = Player()
    players.append(player)
    player._velocity = Point(5,5)
    player._start_position = (Point(10,10))
    player._color = "blue"

    cast_1["player"] = players

    #Create and add platforms + collision walls for enemies
    cast_1["platforms"] = []
    platforms = []

    cast_1["collisions"] = []
    collisions = []

    #First platform and collisions

    finish = Finish()

    crystal_red = Crystal()
    crystal_blue = Crystal()

    enemy_red = Enemy()
    enemy_blue = Enemy()

    #First platform + collisions
    platform1 = Platform()
    collision1_1 = Collision()
    collision1_2 = Collision()

    platform1.set_position(Point(100,400))
    platforms.append(platform1)

    collision1_1.set_position_1(platform1)
    collisions.append(collision1_1)

    collision1_2.set_position_2(platform1)
    collisions.append(collision1_2)

    #Second platform + collisions
    platform2 = Platform()
    collision2_1 = Collision()
    collision2_2 = Collision()

    platform2.set_position(Point(500, 500))
    platforms.append(platform2)

    collision2_1.set_position_1(platform2)
    collisions.append(collision2_1)
    
    collision2_2.set_position_2(platform2)
    collisions.append(collision2_2)
    
    #Third platform + collisions
    platform3 = Platform()
    collision3_1 = Collision()
    collision3_2 = Collision()

    platform3.set_position(Point(0, 100))
    platforms.append(platform3)
    
    collision3_1.set_position_1(platform3)
    collisions.append(collision3_1)    
    
    collision3_2.set_position_2(platform3)
    collisions.append(collision3_2)

    #Fourth platform + collisions
    platform4 = Platform()
    collision4_1 = Collision()
    collision4_2 = Collision()

    platform4.set_position(Point(0, 100))
    platforms.append(platform4)

    collision4_1.set_position_1(platform4)
    collisions.append(collision4_1)

    collision4_2.set_position_2(platform4)
    collisions.append(collision4_2)

    platform5 = Platform()
    collision5_1 = Collision()
    collision5_2 = Collision()

    platform5.set_position(Point(0, 100))
    platforms.append(platform5)

    collision5_1.set_position_1(platform5)
    collisions.append(collision5_1)

    collision5_2.set_position_2(platform5)
    collisions.append(collision5_2)

    #Tall platforms - No collisions
    platform1_tall = Platform()
    platform1_tall.set_image(constants.IMAGE_PLATFORM_TALL)
    platform1_tall._height = constants.TALL_PLATFORM_HEIGHT
    platform1_tall._width = constants.TALL_PLATFORM_WIDTH
    platform1_tall.set_position(Point(400, 100))
    platforms.append(platform1_tall)

    cast_1["platforms"] = platforms
    cast_1["collisions"] = collisions

    #Create crystals
    crystal_red._position = Point(100,60)
    crystals.append(crystal_red)

    crystal_blue._image = constants.IMAGE_CRYSTAL_BLUE
    crystal_blue._position = Point(200, 360)
    crystal_blue._color = "blue"
    crystals.append(crystal_blue)

    cast_1["crystals"] = crystals

    enemy_red._position = Point(150, 360)
    enemy_red._velocity = Point(5, 0)
    enemy_red._direction = "right"
    enemies.append(enemy_red)

    enemy_blue._position = Point(550, 460)
    enemy_blue._velocity  = Point(-5, 0)
    enemy_blue._image = constants.IMAGE_ENEMY_BLUE
    enemy_blue._color = "blue"
    enemy_blue._direction = "left"
    enemies.append(enemy_blue)
    
    cast_1["enemies"] = enemies

    
    finish._position = Point(550, 460)
    finishes.append(finish)

    cast_1["finish"] = finishes

    wins = []
    win = Win()
    wins.append(win)
    cast_1["win"] = wins
    

    # print("level")

    # cast_2 = {}
    
    # cast_2["player"] = []
    # players = []

    # player = Player()
    # player._velocity = Point(5,5)
    # player._color = "red"

    # players.append(player)


    

    

            

    # Create the script {key: tag, value: list}
    script = {}

    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    handle_off_screen_action = HandleOffScreenAction(audio_service)
    control_actors_action = ControlActorsAction(input_service)
    handle_collisions_action = HandleCollisionsAction(physics_service, audio_service, gravity_action)
    
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_off_screen_action, handle_collisions_action]
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Crystal")
    audio_service.start_audio()
    #audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast_1, script)

    director.start_game()

    #audio_service.stop_audio()

if __name__ == "__main__":
    main()