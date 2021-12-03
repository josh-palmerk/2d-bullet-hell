from game.attacks.motion import Motion
from game import constants
from game import game_balance as gb

class DodgeRoll(Motion):
    def __init__(self, player):
        super().__init__()
        self._roll_length = gb.DODGE_ROLL_DODGE_TIME + gb.DODGE_ROLL_COOLDOWN_TIME
        self._timer = -1
        self._player = player

    def update(self):
        """ update the dodge roll """
        if self._timer == self._roll_length: # start dodge roll
            self._player.set_color(constants.DODGE_DODGING_COLOR)
            self._player.set_invincibility(True)
            self._player.set_is_dodging(True)
            self._player.set_is_controllable(False)
            self._player.set_velocity(self._player.get_velocity().scale(gb.DODGE_ROLL_SPEED_FACTOR))


        elif self._timer == self._roll_length - gb.DODGE_ROLL_DODGE_TIME: # dodge "hits ground" hence end invinc and half velocity
            self._player.set_invincibility(False)
            self._player.set_is_dodging(False)
            self._player.set_color(constants.DODGE_COOLDOWN_COLOR)
            self._player.set_velocity(self._player.get_velocity().scale(gb.DODGE_ROLL_SLOW_FACTOR))

        if self._timer > 0: # tick down the timer to 0
            self.decrement_timer()

        elif self._timer == 0: # end of roll cooldown state change
            self._player.set_color(constants.PLAYER_COLOR)
            self._player.set_is_controllable(True)
            self._player.set_is_motioning_1(False)
            self.decrement_timer()
     

        else: # reset on new roll
            self.set_timer(self._roll_length)
