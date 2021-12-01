from game.attacks.motion import Motion
from game import constants

class DodgeRoll(Motion):
    def __init__(self, player):
        super().__init__()
        self._timer = 90
        self._player = player

    def update(self):
        """ update the dodge roll """
        if self._timer == 90:
            self._player.set_color(constants.DEFAULT_ACTOR_COLOR)
            #print("90 case")

        #print(self._timer)

        if self._timer == 0:
            self._player.set_color(constants.PLAYER_COLOR)
            #print("0 case")

        if self._timer > 0:
            self.decrement_timer()
            
        
        else:
            self._player.set_is_motioning_1(False)
            #print("set false")
            self.decrement_timer()

        if self._timer < 0:
            self.set_timer(90)

