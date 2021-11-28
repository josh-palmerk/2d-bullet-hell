from game import game_balance as gb
from game import constants
from game.attacks.single_shot import SingleShot
from game.actors.person import Person

class Enemy(Person):
    def __init__(self):
        super().__init__()

        self._height = constants.ENEMY_HEIGHT
        self._width = constants.ENEMY_WIDTH

        self._health = gb.ENEMY_HEALTH

        self._color = constants.ENEMY_COLOR

        self._attack_1 = SingleShot("p")

# TODO add abstract do_attack_pattern and do_movement_pattern