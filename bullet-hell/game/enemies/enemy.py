from game.actors.actor import Actor
from game import game_balance as gb
from game import constants
from game.attacks.single_shot import SingleShot

class Enemy(Actor):
    def __init__(self):
        super().__init__()

        self._height = constants.ENEMY_HEIGHT
        self._width = constants.ENEMY_WIDTH

        self._health = gb.ENEMY_HEALTH

        self._color = constants.ENEMY_COLOR

        self._attack_1 = SingleShot("p")
        self._is_attacking_1 = False

    def is_attacking_1(self):
        return self._is_attacking_1

    def set_is_attacking_1(self, tf):
        self._is_attacking_1 = tf

    def set_attack_1(self, attack):
        self._attack_1 = attack

    def get_attack_1(self):
        return self._attack_1

    def get_health(self):
        return self._health

    def set_health(self, health):
        self._health = health

    def add_health(self, health):
        self._health += health


# TODO add abstract do_attack_pattern and do_movement_pattern