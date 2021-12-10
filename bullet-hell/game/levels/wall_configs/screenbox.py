from game.levels.wall_configs.wall_config import WallConfig
from game.actors.wall import Wall
from game.point import Point

class ScreenBox(WallConfig):
    def __init__(self) -> None:
        super().__init__()

    def create_walls(self, cast):

        wall_n = Wall() # north wall
        wall_n.set_position(Point(-50, -50))
        wall_n.set_width(2020)
        wall_n.set_height(50)
        cast["walls"].append(wall_n)

        wall_s = Wall() # south wall
        wall_s.set_position(Point(-50, 1080))
        wall_s.set_width(2020)
        wall_s.set_height(50)
        cast["walls"].append(wall_s)

        wall_e = Wall() # east wall
        wall_e.set_position(Point(1920, -50))
        wall_e.set_width(50)
        wall_e.set_height(1130)
        cast["walls"].append(wall_e)

        wall_w = Wall() # west wall
        wall_w.set_position(Point(-50, -50))
        wall_w.set_width(50)
        wall_w.set_height(1130)
        cast["walls"].append(wall_w)
