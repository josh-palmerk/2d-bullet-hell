from game.enemies.enemy import Enemy
from game.point import Point
from game import constants
from game import game_balance as gb
from game.attacks.burst_fire import BurstFire

class Captain(Enemy):
    def __init__(self):
        super().__init__()
        self._attack_1 = BurstFire("p")
        self._health = gb.CAPTAIN_HEALTH
