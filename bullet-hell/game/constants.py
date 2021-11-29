import os
import raylibpy

MAX_X = 1920
MAX_Y = 1080
FRAME_RATE = 60

""" Arrow Keys """
# MOVE_LEFT = raylibpy.KEY_LEFT
# MOVE_RIGHT = raylibpy.KEY_RIGHT
# MOVE_UP = raylibpy.KEY_UP
# MOVE_DOWN = raylibpy.KEY_DOWN

""" WASD controls """
MOVE_LEFT = raylibpy.KEY_A
MOVE_RIGHT = raylibpy.KEY_D
MOVE_UP = raylibpy.KEY_W
MOVE_DOWN = raylibpy.KEY_S

""" Other Controls """
ATK1_KEY = raylibpy.MOUSE_LEFT_BUTTON
ATK2_KEY = raylibpy.MOUSE_RIGHT_BUTTON
PAUSE_KEY = raylibpy.KEY_ESCAPE

""" Scale & Size Settings """
BULLET_HEIGHT = 8
BULLET_WIDTH = 8

PLAYER_HEIGHT = 20
PLAYER_WIDTH = 20
PLAYER_COLOR = raylibpy.BLUE

ENEMY_HEIGHT = 20
ENEMY_WIDTH = 20
ENEMY_COLOR = raylibpy.RED


# MAX_BULLET_SPEED = 10
# PLAYER_BULLET_SPEED = 20
# ENEMY_BULLET_SPEED = 10

BULLET_COLOR = raylibpy.BLACK
DEFAULT_ACTOR_COLOR = raylibpy.GREEN


DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

# IMAGE_BRICK_1 = os.path.join(os.getcwd(), "./batter/assets/brick-3.png")
# IMAGE_BRICK_2 = os.path.join(os.getcwd(), "./batter/assets/brick-4.png")


# IMAGE_PADDLE = os.path.join(os.getcwd(), "./batter/assets/bat.png")
# IMAGE_BALL = os.path.join(os.getcwd(), "./batter/assets/ball.png")

# SOUND_START = os.path.join(os.getcwd(), "./batter/assets/start.wav")
# SOUND_BOUNCE = os.path.join(os.getcwd(), "./batter/assets/boing.wav")
# SOUND_OVER = os.path.join(os.getcwd(), "./batter/assets/over.wav")

BALL_X = MAX_X / 2
BALL_Y = MAX_Y - 125

BALL_DX = 8
BALL_DY = BALL_DX * -1

PADDLE_X = MAX_X / 2
PADDLE_Y = MAX_Y - 25

BRICK_WIDTH = 48
BRICK_HEIGHT = 24

BRICK_SPACE = 5

PADDLE_SPEED = 15

PADDLE_WIDTH = 96
PADDLE_HEIGHT = 24

BALL_WIDTH = 24
BALL_HEIGHT = 24

BONUS_BRICK_CHANCE = 8
