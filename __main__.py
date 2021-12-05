import random
import os

import raylibpy
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService

# TODO: Add imports similar to the following when you create these classes
from game.player import Player
from game.platform import Platform
from game.enemy import Enemy
from game.crystal import Crystal
from game.collision import Collision
from game.finish import Finish
from game.level import Level
from game.gravity_action import GravityAction
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_off_screen_action import HandleOffScreenAction
from game.move_actors_action import MoveActorsAction
from game.handle_level_action import HandleLevelAction

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

    finish = Finish()

    player = Player()
    players.append(player)
    player._velocity = Point(5,5)
    player._color = "blue"

    cast_1["player"] = players

    #Create and add platforms + collision walls for enemies
    cast_1["platforms"] = []
    platforms = []

    cast_1["collisions"] = []
    collisions = []

    #First platform and collisions
    platform1 = Platform()
    platform1.set_height(platform1._height)
    platform1.set_width(platform1._width)
    platform1.set_image(platform1._image)

    platform1.set_position(Point(100,400))
    platforms.append(platform1)

    collision1_1 = Collision()
    collision1_1._position = Point(platform1.get_position().get_x(), platform1.get_position().get_y() - constants.COLLISION_HEIGHT)
    collisions.append(collision1_1)

    collision1_2 = Collision()
    collision1_2._position = Point(platform1.get_position().get_x() + constants.PLATFORM_WIDTH, platform1.get_position().get_y() - constants.COLLISION_HEIGHT)
    collisions.append(collision1_2)

    #Second platform + collisions
    platform2 = Platform()
    platform2.set_image(platform2.get_image())
    platform2.set_position(Point(500, 500))
    platforms.append(platform2)

    collision2_1 = Collision()
    collision2_1._position = Point(platform2.get_position().get_x(), platform2.get_position().get_y() - constants.COLLISION_HEIGHT)
    collisions.append(collision2_1)

    collision2_2 = Collision()
    collision2_2._position = Point(platform2.get_position().get_x() + constants.PLATFORM_WIDTH, platform2.get_position().get_y() - constants.COLLISION_HEIGHT)
    collisions.append(collision2_2)

    platform3 = Platform()
    platform3.set_position(Point(0, 100))
    platforms.append(platform3)

    collision3_1 = Collision()
    collision3_1._position = Point(platform3.get_position().get_x(), platform3.get_position().get_y() - constants.COLLISION_HEIGHT)
    collisions.append(collision3_1)

    collision3_2 = Collision()
    collision3_2._position = Point(platform3.get_position().get_x() + constants.PLATFORM_WIDTH, platform3.get_position().get_y() - constants.COLLISION_HEIGHT)
    collisions.append(collision3_2)

    cast_1["platforms"] = platforms
    cast_1["collisions"] = collisions

    #Create crystals

    crystal_red = Crystal()
    crystal_red._position = Point(100,80)
    crystals.append(crystal_red)

    crystal_blue = Crystal()
    crystal_blue._image = constants.IMAGE_CRYSTAL_BLUE
    crystal_blue._position = Point(200, 380)
    crystal_blue._color = "blue"
    crystals.append(crystal_blue)

    cast_1["crystals"] = crystals

    enemy_red = Enemy()
    enemy_red._position = Point(150, 370)
    enemy_red._velocity = Point(5, 0)
    enemy_red._direction = "right"
    enemies.append(enemy_red)

    enemy_blue = Enemy()
    enemy_blue._position = Point(550, 470)
    enemy_blue._velocity  = Point(-5, 0)
    enemy_blue._image = constants.IMAGE_ENEMY_BLUE
    enemy_blue._color = "blue"
    enemy_blue._direction = "left"
    enemies.append(enemy_blue)
    
    cast_1["enemies"] = enemies

    
    finish._position = Point(600, 400)
    finishes.append(finish)

    cast_1["finish"] = finishes

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
    handle_level_action = HandleLevelAction(physics_service)

    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_off_screen_action, handle_collisions_action, handle_level_action]
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