import math

# GAME SETTINGS

RESOLUTION = WIDTH, HEIGHT = 1600, 900
FPS = 60

# PLAYER SETTINGS

playerPosition = 1.5, 5
playerAngle = 0
playerSpeed = 0.004
playerRotationSpeed = 0.002


# RAYCASTING SETTINGS

fieldOfView = math.pi / 3
halfFieldOfView = fieldOfView / 2
numRays = WIDTH // 2
halfNumRays = numRays // 2
deltaAngle = fieldOfView / numRays
maxDepth = 20