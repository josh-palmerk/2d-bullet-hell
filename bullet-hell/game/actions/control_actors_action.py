from game.actions.action import Action
from game import constants
from game.point import Point
from game import game_balance as gb
import raylibpy

class ControlActorsAction(Action):
    """
    Child of Action that imposes player input onto the player's velocity and action states.
    """
    def __init__(self, input_service) -> None:
        super().__init__()
        self._input_service = input_service

    def execute(self, cast):
        player = cast["player"][0]
        camera = cast["camera"][0]

        if player.is_controllable():
            direction = self._input_service.get_direction()
            direction = direction.add(player.get_position())
            player.set_velocity(player.vect_to_target(direction, gb.PLAYER_SPEED))

            # if not player.is_attacking_1:
            player.set_is_attacking_1(self._input_service.get_mouse_1())
            player.set_target(self._input_service.get_mouse_position())

        if not player.is_motioning_1():
            player.set_is_motioning_1(self._input_service.is_dodge_pressed())


        # player_pos = player.get_center_position()
        # cam_target = raylibpy.Vector2(player_pos.get_x(), player_pos.get_y())
        # camera.target = cam_target
        # player_vel = player.get_velocity()
        # camera.offset.x = player_vel.get_x()
        # camera.offset.y = player_vel.get_y()

        # player_prev = player.get_previous_position()
        # player_diff = player.get_position().get_difference(player_prev)
        # camera.offset.x -= player_diff.get_x()
        # camera.offset.y -= player_diff.get_y()
    