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
            actor.move_next()
        
        for actor in cast["bullets"]:
            # if actor.get_velocity().get_x() > constants.MAX_BULLET_SPEED or actor.get_velocity().get_y() > constants.MAX_BULLET_SPEED:
            #     vel = actor.get_velocity()
            #     new_vel = vel.scale((1 / max(abs(vel.get_x()), abs(vel.get_y()))))
            #     new_vel.scale(gb.PLAYER_BULLET_SPEED)
            #     actor.set_velocity(new_vel)
            actor.move_next()

        for actor in cast["enemies"]:
            actor.move_next()

        cast["UI"][1].increment_counter(1)
        cast["UI"][1].set_text(str(cast["UI"][1].get_counter()))
        
