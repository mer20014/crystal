import os
import raylibpy

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 30

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_PLAYER_RED = os.path.join(os.getcwd(), "./assets/player_red.png")
IMAGE_PLAYER_BLUE = os.path.join(os.getcwd(), "./assets/player_blue.png")

PLAYER_X = MAX_X / 2
PLAYER_Y = MAX_Y - 125

PLAYER_DX = 8
PLAYER_DY = PLAYER_DX * -1

PLAYER_WIDTH = 10
PLAYER_HEIGHT = 30

PLAYER_SPEED = 10

GRAVITY_SPEED = 3

IMAGE_PLATFORM = os.path.join(os.getcwd(), "./assets/platform.png")
PLATFORM_HEIGHT = 30
PLATFORM_WIDTH = 200

IMAGE_PLATFORM_TALL = os.path.join(os.getcwd(), "./assets/platform_tall.png")
TALL_PLATFORM_HEIGHT = 200
TALL_PLATFORM_WIDTH = 30  

IMAGE_ENEMY_RED = os.path.join(os.getcwd(), "./assets/enemy_red.png")
IMAGE_ENEMY_BLUE = os.path.join(os.getcwd(), "./assets/enemy_blue.png")
ENEMY_HEIGHT = 30
ENEMY_WIDTH = 10

COLLISION_HEIGHT = 2
COLLISION_WIDTH = 2
IMAGE_COLLISION = os.path.join(os.getcwd(), "./assets/collision.png")

IMAGE_CRYSTAL_RED = os.path.join(os.getcwd(), "./assets/crystal_red.png")
IMAGE_CRYSTAL_BLUE = os.path.join(os.getcwd(), "./assets/crystal_blue.png")

CRYSTAL_HEIGHT = 40
CRYSTAL_WIDTH = 20

FINISH_HEIGHT = 20
FINISH_WIDTH = 10
IMAGE_FINISH = os.path.join(os.getcwd(), "./assets/finish.png")

SOUND_PLATFORM = os.path.join(os.getcwd(), "./batter/assets/platform_hit.wav")
SOUND_COLOR_CHANGE = os.path.join(os.getcwd(), "./batter/assets/color_change.wav")

IMAGE_WIN = os.path.join(os.getcwd(), "./assets/win.png")