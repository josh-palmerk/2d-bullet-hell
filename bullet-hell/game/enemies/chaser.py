from game.enemies.enemy import Enemy
from game.point import Point
from game import constants
from game import game_balance as gb

class Chaser(Enemy):
    def __init__(self):
        super().__init__()
        self._movement_speed = gb.CHASER_MOVE_SPEED
        self._health = gb.CHASER_HEALTH

    def roll_attack_chance_1(self, player):
        return False #chaser just does contact damage
