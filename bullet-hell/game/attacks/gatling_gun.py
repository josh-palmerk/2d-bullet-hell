from game.attacks.attack import Attack
from game.actors.bullet import Bullet
# from game.point import Point
from game import game_balance as gb
from random import randint

class GatlingGun(Attack):
    def __init__(self, hurt) -> None:
        super().__init__()
        self._shot_cooldown = gb.GATLING_GUN_COOLDOWN
        self._hurt = hurt


    def update(self, cast, attacker):
        if self._timer == self._shot_cooldown:
            self.spawn_attack(cast, attacker) #TODO params
            #self.decrement_timer(cast, attacker)


        if self._timer > 0:
            self.decrement_timer()
            #return True

        elif self._timer == 0:
            self.decrement_timer()
            #return False

        if self._timer < 0 and attacker.is_attacking_1():
            self.set_timer(self._shot_cooldown)
            attacker.set_is_attacking_1(False)

    def spawn_attack(self, cast, attacker):
        """
        Creates a single-shot attack.

        Args:
            cast: dictionary of actors
            attacker: instance of the attacking entity

            direction: direction of bullet being fired
            speed: multiplied with direction vector
            position: current position of firing entity
            hurt: "p" "e" "pe"
        """
        shot = Bullet(self._hurt)
        shot.set_position(attacker.get_center_position())
        shot.set_range(gb.SINGLE_SHOT_RANGE)
        shot_vel = shot.vect_to_target(attacker.get_target(), attacker.get_bullet_speed())
        if not attacker.get_velocity().is_zero():
            spread = randint(-10, 10)
        else:
            spread = randint(-4, 4)
        shot_vel = shot.adjust_vector(shot_vel, spread, attacker.get_bullet_speed())
        shot.set_velocity(shot_vel)    
        cast["bullets"].append(shot)

        # attacker.set_is_attacking_1(False)

