from game import game_balance as gb
from game import constants
from game.attacks.single_shot import SingleShot
from game.actors.person import Person
from random import randint
from game.attacks.sawed_off_shot import SawedOffShot


class Enemy(Person):
    def __init__(self):
        super().__init__()

        self._height = constants.ENEMY_HEIGHT
        self._width = constants.ENEMY_WIDTH

        self._health = gb.ENEMY_HEALTH

        self._color = constants.ENEMY_COLOR

        self._movement_speed = gb.ENEMY_MOVE_SPEED

        self._attack_1 = SawedOffShot("p")
        self._attack_chance = gb.ENEMY_ATTACK_CHANCE
        self._bullet_speed = gb.ENEMY_BULLET_SPEED


    def roll_attack_chance_1(self):
        if randint(0, self._attack_chance) == 0:
            self._is_attacking_1 = True

    def do_movement_pattern(self):
        self._velocity = self.vect_to_target(self._target, self._movement_speed)


# TODO add abstract do_attack_pattern and do_movement_pattern