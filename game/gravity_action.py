import raylibpy
from game.action import Action
from game import constants
from game.point import Point

class GravityAction(Action):
    """Code for applying gravity to the player and jumping
    
    Stereotype:
        Controller

    """
    def __init__(self):
        super().__init__()
        

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        player = cast["player"][0]
        self._handle_gravity(player)
                

    def _handle_gravity(self, actor):
        """Moves the given actor to its next position according to its 
        velocity. Will wrap the position from one side of the screen to the 
        other when it reaches the edge in either direction.
        
        Args:
            actor (Actor): The actor to move.
        """

        position = actor.get_position()
        velocity = actor.get_velocity()

        x = position.get_x()
        y = position.get_y()
        
        dx = velocity.get_x()
        dy = velocity.get_y()

        dy = dy + 2
        #print(dy)        
        y = (y + dy) % constants.MAX_Y
        position = Point(x, y)
        actor.set_position(position)


    def jump(self, cast):
        """
        Moves the selected cast member up when jump is pressed

        Arg (cast): The cast used
        """
        player = cast["player"][0]

        jump = False
        jump_timer = 100

        position = player.get_position()
        velocity = player.get_velocity()
        x = position.get_x()
        y = position.get_y()
        dx = velocity.get_x()
        dy = velocity.get_y()
        is_key_down = raylibpy.is_key_down(raylibpy.KEY_UP)

        while is_key_down:         
            jump = True
            jump_height = 15
            if jump is True and jump_timer > 0:
                dy = dy + jump_height
                y = (y - dy) % constants.MAX_Y
                position = Point(x,y)
                player.set_position(position)
                jump_timer -= 1
                jump_height = jump_height **2
                #print(jump_timer)
            
            else: 
                jump = False
                is_key_down = False


    # def _handle_gravity(self, actor):
    #     position = actor.get_position()
    #     velocity = actor.get_velocity()

    #     x = position.get_x()
    #     y = position.get_y()
    #     dx = velocity.get_x()
    #     dy = velocity.get_y()
    #     dy = dy *-3 + 1            

    #     x = (x + dx) % constants.MAX_X
    #     y = (y + dy) % constants.MAX_Y
        
    #     position = Point(x, y)
    #     actor.set_position(position)


"""
Property to actor isaffectedbygravity: True/False
Go throguh action - if actor is afffected by gravity, change velocity
when space pressed, add to velocity

Could add a friction class, take velocity and take 90% of velocity, 90% of that, etc

"""