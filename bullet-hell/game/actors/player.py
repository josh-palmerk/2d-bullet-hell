from game.actors.actor import Actor
from game import game_balance as gb

class Player(Actor):
    def __init__(self):
        super().__init__()

        self._width = gb.PLAYER_WIDTH
        self._height = gb.PLAYER_HEIGHT