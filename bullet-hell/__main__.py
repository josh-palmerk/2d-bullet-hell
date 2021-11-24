import os
os.environ['RAYLIB_BIN_PATH'] = "."
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


""" Services """
from game.services.input_service import InputService
from game.services.output_service import OutputService
from game.services.physics_service import PhysicsService
from game.services.audio_service import AudioService

""" Actions """
from game.actions.draw_actors_action import DrawActorsAction
from game.actions.control_actors_action import ControlActorsAction
from game.actions.handle_collisions_action import HandleCollisionsAction
# from game.actions.handle_off_screen_action import HandleOffScreenAction
from game.actions.move_actors_action import MoveActorsAction
from game.actions.do_attacks_action import DoAttacksAction

def main():

    # creates the cast {key: tag, value: list}
    cast = {}

    cast["player"] = []
    cast["player"].append(Player())

    cast["enemies"] = []

    cast["bullets"] = []
    test_bullet = Bullet("p")
    test_bullet.set_position(Point(100, 100))
    test_bullet.set_velocity(Point(1, 0))
    cast["bullets"].append(test_bullet)
    test_bullet2 = Bullet("p")
    test_bullet2.set_position(Point(200, 200))
    test_bullet2.set_velocity(Point(.5, 0))
    cast["bullets"].append(test_bullet2)
    test_bullet3 = Bullet("p")
    test_bullet3.set_position(Point(300, 300))
    test_bullet3.set_velocity(Point(.25, 0))
    cast["bullets"].append(test_bullet3)

    cast["UI"] = []
    health_board = Actor()
    health_board.set_text(str(cast["player"][0].get_health()))
    health_board.set_position(Point(300, 10))
    cast["UI"].append(health_board)

    # Create the script {key: tag, value: list}
    script = {}

    """ Instantiate services and actions """
    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    # handle_offscreen_action = HandleOffScreenAction()
    control_actors_action = ControlActorsAction(input_service)
    handle_collisions_action = HandleCollisionsAction(physics_service)
    do_attacks_action = DoAttacksAction()


    """ Define actions in each script piece """
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action, do_attacks_action]
    script["output"] = [draw_actors_action]


    """ Start game """
    output_service.open_window("Telestial Bullet");
    audio_service.start_audio()
    # audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()
