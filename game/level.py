from game.actor import Actor

class Level(Actor):
    def __init__(self):
        super().__init__()
        self._level = 1