import sys
from game.point import Point
import raylibpy
from game import constants

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
    """

    #TODO: add more input checkers

    def __init__(self):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        pass
        
    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            Point: The selected direction.
        """
        dx = 0
        dy = 0

        if self.is_left_pressed():
            dx += -1
        if self.is_right_pressed():
            dx += 1
        # if self.is_left_pressed() and self.is_right_pressed():
        #     dx = 0

        if self.is_up_pressed():
            dy += -1
        if self.is_down_pressed():
            dy += 1
        # if self.is_up_pressed() and self.is_down_pressed():
        #     dy = 0

        direction = Point(dx, dy)
        return direction

    def is_left_pressed(self):
        return raylibpy.is_key_down(constants.MOVE_LEFT)

    def is_right_pressed(self):
        return raylibpy.is_key_down(constants.MOVE_RIGHT)

    def is_up_pressed(self):
        return raylibpy.is_key_down(constants.MOVE_UP)

    def is_down_pressed(self):
        return raylibpy.is_key_down(constants.MOVE_DOWN)

    def is_pause_pressed(self):
        return raylibpy.is_key_down(constants.PAUSE_KEY)

    def is_dodge_pressed(self):
        return raylibpy.is_key_down(constants.DODGE_KEY)


    def get_mouse_position(self):
        pos = raylibpy.get_mouse_position()
        return Point(pos.x, pos.y)

    def get_mouse_1(self):
        return raylibpy.is_mouse_button_down(constants.ATK1_KEY)

    def get_mouse_2(self):
        return raylibpy.is_mouse_button_down(constants.ATK2_KEY)

    def window_should_close(self):
        return raylibpy.window_should_close()
