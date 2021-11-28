from game.actors.actor import Actor
from game.point import Point
from game import game_balance as gb
from game import constants
from game.attacks.single_shot import SingleShot

class Person(Actor):
    def __init__(self):
        super().__init__()

        self._target = Point(0, 0) #this typically refers to what the *PERSON* is targetING
        self._is_attacking_1 = False
        self._attack_1 = SingleShot("pe")
        self._bullet_speed = gb.PLAYER_BULLET_SPEED
        self._health = 0


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
    
    def get_bullet_speed(self):
        return self._bullet_speed

    def set_bullet_speed(self, bullet_speed):
        self._bullet_speed = bullet_speed

    def get_target(self):
        return self._target

    def set_target(self, target):
        self._target = target
    