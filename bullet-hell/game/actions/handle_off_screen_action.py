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
        balls = cast["balls"]

        for ball in balls:
            pos = ball.get_position()
            vel = ball.get_velocity()
            if pos.get_x() <= 0 or pos.get_x() >= (constants.MAX_X - constants.BALL_WIDTH):
               vel = self.bounce_horizontal(vel)
            if pos.get_y() <= 0: # or pos.get_y() >= (constants.MAX_Y - constants.BALL_HEIGHT):
                vel = self.bounce_vertical(vel)
            ball.set_velocity(vel)

        #return super().execute(cast)

    def bounce_horizontal(self, point):
        """ Returns Point() with x velocity flipped """
        new = Point((point.get_x() * -1), point.get_y())
        return new

    def bounce_vertical(self, point):
        """ Returns Point() with y velocity flipped """
        new = Point(point.get_x(), (point.get_y() * -1))
        return new