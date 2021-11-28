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
from game.lives import Lives
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_off_screen_action import HandleOffScreenAction
from game.move_actors_action import MoveActorsAction
from game.handle_level_action import HandleLevelAction

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    cast["player"] = []
    players = []

    player = Player()
    player.set_height(player.get_height())
    player.set_width(player.get_width())
    player.set_image(player.get_image())

    x = player.get_position().get_x()
    y = player.get_position().get_y()
    player.set_position(Point(x, y))
    players.append(player)

    cast["player"] = players


    cast["platforms"] = []
    # TODO: Create a ball here and add it to the list


    cast["crystals"] = []


    cast["enemies"] = []
    
    

    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    handle_off_screen_action = HandleOffScreenAction(audio_service)
    control_actors_action = ControlActorsAction(input_service)
    handle_collisions_action = HandleCollisionsAction(physics_service, audio_service)
    handle_level_action = HandleLevelAction(output_service)

    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_off_screen_action, handle_collisions_action, handle_level_action]
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Crystal")
    audio_service.start_audio()
    #audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    #audio_service.stop_audio()

if __name__ == "__main__":
    main()