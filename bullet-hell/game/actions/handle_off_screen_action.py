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

    # def bounce_horizontal(self, point):
    #     """ Returns Point() with x velocity flipped """
    #     new = Point((point.get_x() * -1), point.get_y())
    #     return new

    # def bounce_vertical(self, point):
    #     """ Returns Point() with y velocity flipped """
    #     new = Point(point.get_x(), (point.get_y() * -1))
    #     return new