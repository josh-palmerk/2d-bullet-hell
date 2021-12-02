from game.attacks.attack import Attack
from game.actors.bullet import Bullet
# from game.point import Point

class SingleShot(Attack):
    def __init__(self, hurt) -> None:
        super().__init__()

        self._hurt = hurt

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
        shot.set_velocity(shot.vect_to_target(attacker.get_target(), attacker.get_bullet_speed()))    
        cast["bullets"].append(shot)

        # attacker.set_is_attacking_1(False)

