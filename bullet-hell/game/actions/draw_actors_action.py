import raylibpy
from game.actions.action import Action

class DrawActorsAction(Action):
    """A code template for drawing actors. The responsibility of this class of
    objects is use an output service to draw all actors on the screen.
    
    Stereotype:
        Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """

    def __init__(self, output_service):
        """The class constructor.
        
        Args:
            output_service (OutputService): An instance of OutputService.
        """
        self._output_service = output_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._output_service.clear_screen()
        #raylibpy.begin_mode2d(cast["camera"][0])

        for actor in (cast["player"], cast["enemies"], cast["bullets"], cast["walls"]):
            self._output_service.draw_actors(actor)

        #raylibpy.end_mode2d()

        # player = cast["player"][0]
        # camera = cast["camera"][0]
        # if not player.get_is_colliding_wall():
        #     player_pos = player.get_center_position()
        #     cam_target = raylibpy.Vector2(player_pos.get_x(), player_pos.get_y())
        #     camera.target = cam_target
        #     player_vel = player.get_velocity()
        #     camera.offset.x -= player_vel.get_x()
        #     camera.offset.y -= player_vel.get_y()

        self._output_service.flush_buffer()
