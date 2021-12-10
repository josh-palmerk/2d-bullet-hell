from raylibpy import is_mouse_button_pressed
from game.actors.actor import Actor
from game import game_balance as gb
from game import constants
from game.point import Point

class Bullet(Actor):
    def __init__(self, hurts="pe"):
        super().__init__()

        if hurts == "p":
            self._hurts_player = True
            self._hurts_enemies = False
        elif hurts == "e":
            self._hurts_player = False
            self._hurts_enemies = True 
        elif hurts == "pe":
            self._hurts_player = True
            self._hurts_enemies = True
        else:
            self._hurts_player = False
            self._hurts_enemies = False
        

        self._height = constants.BULLET_HEIGHT
        self._width = constants.BULLET_WIDTH
        self._damage = gb.DEFAULT_BULLET_DAMAGE
        self._color = constants.BULLET_COLOR
        self._velocity = Point(0, 0)
        self._range = 100

    def get_range(self):
        return self._range

    def set_range(self, value):
        self._range = value

    def decrement_range(self):
        """ just -= 1 """
        self._range -= 1

    def hurts_player(self):
        return self._hurts_player

    def hurts_enemies(self):
        return self._hurts_enemies
    
    def get_damage(self):
        return self._damage

    def set_hurts_player(self, tf):
        self._hurts_player = tf

    def set_hurts_enemies(self, tf):
        self._hurts_enemies = tf
    
    def set_damage(self, damage):
        self._damage = damage
