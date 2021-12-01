from game.actors.person import Person
from game import game_balance as gb
from game import constants
from game.attacks.single_shot import SingleShot
# from game.point import Point
from game.attacks.dodge_roll import DodgeRoll

class Player(Person):
    def __init__(self):
        super().__init__()

        self._width = constants.PLAYER_WIDTH
        self._height = constants.PLAYER_HEIGHT

        self._health = gb.PLAYER_HEALTH
        self._color = constants.PLAYER_COLOR
        
        self._attack_1 = SingleShot("e")
        self._bullet_speed = gb.PLAYER_BULLET_SPEED
        self._motion_1 = DodgeRoll(self)
        self._is_dodging = False
        self._is_controllable = True

    def is_controllable(self):
        return self._is_controllable

    def set_is_controllable(self, tf):
        self._is_controllable = tf

    def is_dodging(self):
        return self._is_dodging

    def set_is_dodging(self, tf):
        self._is_dodging = tf
