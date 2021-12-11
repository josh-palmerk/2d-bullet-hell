from game.levels.wall_configs.wall_config import WallConfig
from game.levels.wall_configs.screenbox import ScreenBox
from game.actors.wall import Wall
from game.point import Point

class SandboxWallConfig(WallConfig):
    def __init__(self) -> None:
        super().__init__()
        self._screenbox = ScreenBox()

    def create_walls(self, cast):
        self._screenbox.create_walls(cast)

        wall_1 = Wall()
        wall_1.set_position(Point(100, 100))
        wall_1.set_width(100)
        wall_1.set_height(150)
        cast["walls"].append(wall_1)

        wall_2 = Wall()
        wall_2.set_position(Point(100, 500))
        wall_2.set_width(100)
        wall_2.set_height(50)
        cast["walls"].append(wall_2)

        wall_3 = Wall()
        wall_3.set_position(Point(100, 700))
        wall_3.set_width(100)
        wall_3.set_height(50)
        cast["walls"].append(wall_3)

        wall_4 = Wall()
        wall_4.set_position(Point(500, 150))
        wall_4.set_width(150)
        wall_4.set_height(150)
        cast["walls"].append(wall_4)

        wall_5 = Wall()
        wall_5.set_position(Point(400, 400))
        wall_5.set_width(200)
        wall_5.set_height(80)
        cast["walls"].append(wall_5)

        wall_6 = Wall()
        wall_6.set_position(Point(600, 800))
        wall_6.set_width(100)
        wall_6.set_height(100)
        cast["walls"].append(wall_6)

        wall_7 = Wall()
        wall_7.set_position(Point(1000, 100))
        wall_7.set_width(500)
        wall_7.set_height(80)
        cast["walls"].append(wall_7)

        wall_8 = Wall()
        wall_8.set_position(Point(1500, 400))
        wall_8.set_width(150)
        wall_8.set_height(120)
        cast["walls"].append(wall_8)

        wall_9 = Wall()
        wall_9.set_position(Point(900, 500))
        wall_9.set_width(200)
        wall_9.set_height(200)
        cast["walls"].append(wall_9)

        wall_10 = Wall()
        wall_10.set_position(Point(1000, 550))
        wall_10.set_width(500)
        wall_10.set_height(100)
        cast["walls"].append(wall_10)

        wall_11 = Wall()
        wall_11.set_position(Point(1400, 550))
        wall_11.set_width(150)
        wall_11.set_height(250)
        cast["walls"].append(wall_11)
