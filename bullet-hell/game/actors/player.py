from game.actors.person import Person
from game import game_balance as gb
from game import constants
from game.attacks.single_shot import SingleShot
from game.point import Point
from game.attacks.dodge_roll import DodgeRoll
from game.attacks.sawed_off_shot import SawedOffShot
from game.attacks.circle_shot import CircleShot
from game.attacks.sniper_shot import SniperShot
from game.attacks.gatling_gun import GatlingGun
from game.attacks.burst_fire import BurstFire

class Player(Person):
    def __init__(self):
        super().__init__()

        self._width = constants.PLAYER_WIDTH
        self._height = constants.PLAYER_HEIGHT

        self._health = gb.PLAYER_HEALTH
        self._color = constants.PLAYER_COLOR
        
        #self._attack_1 = SingleShot("e")
        #self._attack_1 = SawedOffShot("e")
        #self._attack_1 = CircleShot("e")
        #self._attack_1 = SniperShot("e")
        #self._attack_1 = GatlingGun("e")
        self._attack_1 = BurstFire("e")

        self._bullet_speed = gb.PLAYER_BULLET_SPEED
        self._motion_1 = DodgeRoll(self)
        self._is_dodging = False
        self._is_controllable = True
        # self._target = Point(0, 0)
        self._previous_position = self._position
        self._is_colliding_wall = False

    def set_is_colliding_wall(self, tf):
        self._is_colliding_wall = tf

    def get_is_colliding_wall(self):
        return self._is_colliding_wall

    def get_previous_position(self):
        return self._previous_position

    def set_previous_position(self, point):
        self._previous_position = point

    def is_controllable(self):
        return self._is_controllable

    def set_is_controllable(self, tf):
        self._is_controllable = tf

    def is_dodging(self):
        return self._is_dodging

    def set_is_dodging(self, tf):
        self._is_dodging = tf
