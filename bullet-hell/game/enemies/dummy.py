from game.enemies.enemy import Enemy
from game.point import Point

class Dummy(Enemy):
    def __init__(self):
        super().__init__()

    def do_movement_pattern(self):
        self._velocity = Point(0, 0)
        self._is_dummy = True

    def is_dummy(self):
        return self._is_dummy
    # def roll_attack_chance_1(self):
    #     return super().roll_attack_chance_1()