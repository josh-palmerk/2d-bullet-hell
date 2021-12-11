from game.enemies.enemy import Enemy
from game.point import Point
from game import constants
from game import game_balance as gb
from game.attacks.single_shot import SingleShot

class Grunt(Enemy):
    def __init__(self):
        super().__init__()
        self._attack_1 = SingleShot("p")
        self._health = gb.GRUNT_HEALTH

    # def do_movement_pattern(self):
