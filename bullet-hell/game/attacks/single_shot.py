from game.attacks.attack import Attack
from game.actors.bullet import Bullet
from game.point import Point

class SingleShot(Attack):
    def __init__(self, hurt) -> None:
        super().__init__()

        self._hurt = hurt

    def spawn_attack(self, cast, attacker):
        """
        Creates a single-shot attack.

        Args:
            cast: dictionary of actors
            direction: direction of bullet being fired. Should not exceed (1, 1)
            speed: multiplied with direction vector
            position: current position of firing entity
            hurt: "p" "e" "pe"
        """
        # bullets = cast["bullets"]

        shot = Bullet(self._hurt)
        shot.set_position(attacker.get_center_position())
        
        shot.vect_to_target(attacker.get_target(), attacker.get_bullet_speed())
        # shot.home_to_target(attacker.get_target(), attacker.get_bullet_speed())

        # offset_pos = Point((position.get_x() + (direction.get_x() * 2)), (position.get_x() + (direction.get_y() * 2)))
        

        cast["bullets"].append(shot)
