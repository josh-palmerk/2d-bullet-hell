from game.actors.actor import Actor
from game import game_balance as gb
from game import constants


class Enemy(Actor):
    def __init__(self):
        super().__init__()

        self._height = constants.ENEMY_HEIGHT
        self._width = constants.ENEMY_WIDTH

        self._health = gb.ENEMY_HEALTH

    def get_health(self):
        return self._health

    def set_health(self, health):
        self._health = health

    def add_health(self, health):
        self._health += health


# TODO add abstract do_attack_pattern and do_movement_pattern