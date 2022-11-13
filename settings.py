# game settings
import math

RES = WIDTH, HEIGHT = 1920, 1080
FPS = 0

PLAYER_POS = 1.5, 5  # THIS IS THE MINI MAP
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002

# Ray Casting Settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS  # Delta Angle is the change in the rays, or the difference between the two rays,
# the space between the two rays
MAX_DEPTH = 20  # Maximum Draw Distance for the Rays
