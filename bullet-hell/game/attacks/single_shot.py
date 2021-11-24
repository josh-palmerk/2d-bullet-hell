from game.attacks.attack import Attack
from game.actors.bullet import Bullet
from game.point import Point

class SingleShot(Attack):
    def __init__(self, hurt) -> None:
        super().__init__()

        self._hurt = hurt

    def spawn_attack(self, cast, target, speed, position):
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

        shot.home_to_target(target, speed)

        # offset_pos = Point((position.get_x() + (direction.get_x() * 2)), (position.get_x() + (direction.get_y() * 2)))
        shot.set_position(position)

        cast["bullets"].append(shot)
