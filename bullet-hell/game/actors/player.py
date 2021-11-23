from game.actors.actor import Actor
from game import game_balance as gb
from game import constants

class Player(Actor):
    def __init__(self):
        super().__init__()

        self._width = constants.PLAYER_WIDTH
        self._height = constants.PLAYER_HEIGHT

        self._health = gb.PLAYER_HEALTH
    #     self._attack_1 = ""

    # def set_attack_1(self, attack):
    #     self._attack_1 = attack

    # def execute_attack_1(self, cast):
    #     self._attack_1.execute(cast)

    def get_health(self):
        return self._health

    def set_health(self, health):
        self._health = health

    def add_health(self, health):
        self._health += health
    