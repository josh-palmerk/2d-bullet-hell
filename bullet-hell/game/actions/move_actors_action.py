from game import constants
from game.actions.action import Action
from game.point import Point
from game import game_balance as gb

class MoveActorsAction(Action):
    """
    Child of Action that handles movement for all moving actors in the game. Just need to call execute(cast).
    """
    def __init__(self):
        super().__init__()
    
    def execute(self, cast):

        for actor in cast["player"]:
            actor.set_previous_position(actor.get_position())
            actor.move_next()
        
        for actor in cast["bullets"]:
            actor.move_next()
            actor.decrement_range()

        for actor in cast["enemies"]:
            actor.move_next()

        cast["UI"][1].increment_counter(1)
        cast["UI"][1].set_text(str(cast["UI"][1].get_counter()))
