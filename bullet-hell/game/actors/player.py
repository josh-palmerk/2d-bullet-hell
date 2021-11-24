from game.actors.actor import Actor
from game import game_balance as gb
from game import constants
from game.attacks.single_shot import SingleShot
from game.point import Point

class Player(Actor):
    def __init__(self):
        super().__init__()

        self._width = constants.PLAYER_WIDTH
        self._height = constants.PLAYER_HEIGHT

        self._health = gb.PLAYER_HEALTH
        self._color = constants.PLAYER_COLOR
        
        self._is_attacking_1 = False
        self._attack_1 = SingleShot("e")
        self._target = Point(0, 0)
        self._bullet_speed = gb.PLAYER_BULLET_SPEED

    def get_target(self):
        return self._target

    def set_target(self, target):
        self._target = target
    
    def get_bullet_speed(self):
        return self._bullet_speed

    def set_bullet_speed(self, bullet_speed):
        self._bullet_speed = bullet_speed

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
    