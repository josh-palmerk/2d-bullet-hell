from game.enemies.enemy import Enemy
from game.point import Point
from game import constants
from game import game_balance as gb
from game.attacks.gatling_gun import GatlingGun

class Gatler(Enemy):
    def __init__(self):
        super().__init__()
        self._attack_1 = GatlingGun("p")
        self._health = gb.GATLER_HEALTH
        self._movement_speed = gb.GATLER_MOVE_SPEED
        self._attack_chance = 5

    # def roll_attack_chance_1(self, player):
    #     if randint(0, self._attack_chance) == 0:
    #         self._is_attacking_1 = True