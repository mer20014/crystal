from time import sleep

import raylibpy
from game import constants
from game.point import Point
from game.audio_service import AudioService

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
    """

    def __init__(self, cast, script):
        """The class constructor.
        
        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
        """
        self._cast = cast
        self._script = script
        self.audio_service = AudioService()
        self._keep_playing = True
        
    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        while self._keep_playing:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")
            is_continue = self.game_over()
            is_win = self.win()
            # TODO: Add some logic like the following to handle game over conditions
                        
            if is_continue == False or is_win == True:
                self._cast == {}
                self.audio_service.play_sound(constants.SOUND_OVER)
                sleep(3)
                self._keep_playing = False

            if raylibpy.window_should_close():
                self._keep_playing = False


    def game_over(self):
        """
        Determines if the game is over. 
        
        Returns boolean
        """
        pass
        
    def win(self):
        """
        Determines if the game is won

        Return boolean
        """
        pass


    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)