from game.attacks.motion import Motion
from game import constants

class DodgeRoll(Motion):
    def __init__(self, player):
        super().__init__()
        self._timer = 70
        self._player = player

    def update(self):
        """ update the dodge roll """
        if self._timer == 70: # start dodge roll
            self._player.set_color(constants.DEFAULT_ACTOR_COLOR)
            self._player.set_invincibility(True)
            self._player.set_is_dodging(True)
            self._player.set_is_controllable(False)

        elif self._timer == 30: # dodge "hits ground" hence end invinc and half velocity
            self._player.set_invincibility(False)
            self._player.set_is_dodging(False)
            self._player.set_color(constants.COLOR_PURPLE)
            self._player.set_velocity(self._player.get_velocity().scale(0.5))
            #TODO scale down player velocity


        if self._timer > 0: # tick down the timer to 0
            self.decrement_timer()

        elif self._timer == 0: # end of roll cooldown state change
            self._player.set_color(constants.PLAYER_COLOR)
            self._player.set_is_controllable(True)
            self._player.set_is_motioning_1(False)
            self.decrement_timer()
     
        
        else: # reset on new roll
            self.set_timer(70)

