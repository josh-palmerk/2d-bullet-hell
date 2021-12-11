from game.enemies.enemy import Enemy
from game.point import Point
from game import constants

class Dummy(Enemy):
    def __init__(self):
        super().__init__()

    def do_movement_pattern(self):
        self._velocity = Point(0, 0)
        self._color = constants.DUMMY_COLOR
