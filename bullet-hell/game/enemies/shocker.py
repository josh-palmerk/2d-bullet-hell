from game.enemies.enemy import Enemy
from game.point import Point
from game import constants
from game import game_balance as gb
from game.attacks.sawed_off_shot import SawedOffShot

class Shocker(Enemy):
    def __init__(self):
        super().__init__()
        self._attack_1 = SawedOffShot("p")
        self._health = gb.SHOCKER_HEALTH
        self._movement_speed = gb.SHOCKER_MOVE_SPEED
