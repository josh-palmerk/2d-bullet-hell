import os
os.environ['RAYLIB_BIN_PATH'] = "."
import raylibpy

from random import randint

""" Game """
from game import constants
from game.director import Director
from game import game_balance as gb
from game.point import Point

""" Actors """
from game.actors.actor import Actor
from game.actors.player import Player
from game.actors.bullet import Bullet
from game.enemies.enemy import Enemy
from game.enemies.dummy import Dummy
from game.enemies.chaser import Chaser
from game.actors.wall import Wall

""" Services """
from game.services.input_service import InputService
from game.services.output_service import OutputService
from game.services.physics_service import PhysicsService
from game.services.audio_service import AudioService

""" Actions """
from game.actions.draw_actors_action import DrawActorsAction
from game.actions.control_actors_action import ControlActorsAction
from game.actions.handle_collisions_action import HandleCollisionsAction
from game.actions.handle_off_screen_action import HandleOffScreenAction
from game.actions.move_actors_action import MoveActorsAction
from game.actions.do_attacks_action import DoAttacksAction
from game.actions.update_movements_action import UpdateMovementsAction
from game.actions.handle_walls_action import HandleWallsAction
from game.actions.game_events_action import GameEventsAction

""" Levels """
from game.levels.wall_configs.screenbox import ScreenBox
from game.levels.wall_configs.sandbox_wallconfig import SandboxWallConfig


def main():

    # creates the cast {key: tag, value: list}
    cast = {}

    cast["player"] = []
    cast["enemies"] = []
    cast["bullets"] = []
    cast["walls"] = []
    cast["UI"] = []
    cast["camera"] = []



    player = Player()
    player.set_position(Point(50, 50))
    cast["player"].append(player)

    # player_pos = player.get_center_position()

    # camera = raylibpy.Camera2D()
    # cam_target = raylibpy.Vector2(player_pos.get_x(), player_pos.get_y())
    # camera.target = cam_target
    # camera.zoom = 1.5
    # camera.offset = raylibpy.Vector2((constants.MAX_X / 2), (constants.MAX_Y / 2))
    # cast["camera"].append(camera)

    enemy1 = Enemy()
    enemy1.set_position(Point(500, 500))
    #cast["enemies"].append(enemy1)

    enemy2 = Enemy()
    enemy2.set_position(Point(1200, 750))
    cast["enemies"].append(enemy2)

    enemy3 = Enemy()
    enemy3.set_position(Point(1800, 500))
    cast["enemies"].append(enemy3)

    dummy1 = Dummy()
    dummy1.set_position(Point(300, 700))
    cast["enemies"].append(dummy1)

    chaser1 = Chaser()
    chaser1.set_position(Point(1920, 1080))
    cast["enemies"].append(chaser1)


    # screenbox = ScreenBox()
    # screenbox.create_walls(cast)
    sandbox = SandboxWallConfig()
    sandbox.create_walls(cast)

    health_board = Actor()
    health_board.set_text(str(cast["player"][0].get_health()))
    health_board.set_position(Point(300, 10))
    cast["UI"].append(health_board)

    timer = Actor()
    timer.set_text(str(0))
    timer.set_position(Point(500, 10))
    cast["UI"].append(timer)



    # Create the script {key: tag, value: list}
    script = {}

    """ Instantiate services and actions """
    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    handle_offscreen_action = HandleOffScreenAction()
    control_actors_action = ControlActorsAction(input_service)
    handle_collisions_action = HandleCollisionsAction(physics_service)
    do_attacks_action = DoAttacksAction()
    update_movements_action = UpdateMovementsAction()
    handle_walls_action = HandleWallsAction(physics_service)
    game_events_action = GameEventsAction()

    """ Define actions in each script piece """
    script["input"] = [control_actors_action]
    script["update"] = [do_attacks_action, handle_collisions_action, update_movements_action, handle_walls_action, move_actors_action, game_events_action]
    script["output"] = [draw_actors_action]


    """ Start game """
    output_service.open_window("Telestial Bullet");
    audio_service.start_audio()
    # audio_service.play_sound(constants.SOUND_START)
    
    cast["keep_playing"] = [] #this keeps gameloop running until set false
    kp = Actor()
    kp.set_counter(1)
    cast["keep_playing"].append(kp)

    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()
