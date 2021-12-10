from game.actions.action import Action
from game.point import Point
from game import constants

class HandleOffScreenAction(Action):
    """
    Child of Action that handles bouncing the balls off the edges of the screen.
    """
    def __init__(self):
        super().__init__()
    
    def execute(self, cast):
        bullets = cast["bullets"]
        player = cast["player"][0]
        q = 0
        for bullet in bullets:
            pos = bullet.get_position()
            if pos.get_x() <= 0 or pos.get_x() >= constants.MAX_X:
                cast["bullets"].pop(q)
                q -= 1
            elif pos.get_y() <= 0 or pos.get_y() >= constants.MAX_Y:
                cast["bullets"].pop(q)
                q -= 1
            q += 1
        origin = Point(0, 0)
        if origin.get_quadrant(player.get_position()) != 1:
            player.set_position(origin)

