from game.actor import Actor

class Level(Actor):
    def __init__(self):
        """Tracks what level the player is on currently
        
        Args:
            self (Actor): an instance of Actor.
        """
        super().__init__()
        self._level = 0