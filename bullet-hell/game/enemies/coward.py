from game.enemies.enemy import Enemy
from game.point import Point
from game import constants
from game import game_balance as gb
from game.attacks.single_shot import SingleShot

class Coward(Enemy):
    def __init__(self):
        super().__init__()
        self._attack_1 = SingleShot("p")
        self._health = gb.COWARD_HEALTH

    def do_movement_pattern(self):
        vel = self.vect_to_target(self._movement_target, self._movement_speed)
        self._velocity = vel.reverse()