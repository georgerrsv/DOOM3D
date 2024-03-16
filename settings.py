import math

# GAME SETTINGS

RESOLUTION = WIDTH, HEIGHT = 1600, 900
FPS = 60
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

# PLAYER SETTINGS

playerPosition = 1.5, 5
playerAngle = 0
playerSpeed = 0.004
playerRotationSpeed = 0.002
playerSizeScale = 60

# MOUSE SETTINGS

mouseSensitivity = 0.0003
mouseMaxRel = 40
mouseBorderLeft = 100
mouseBorderRight = WIDTH - mouseBorderLeft

# FLOOR SETTINGS

floorColor = (30, 30, 30)


# RAYCASTING SETTINGS

fieldOfView = math.pi / 3
halfFieldOfView = fieldOfView / 2
numRays = WIDTH // 2
halfNumRays = numRays // 2
deltaAngle = fieldOfView / numRays
maxDepth = 20

screenDistance = HALF_WIDTH / math.tan(halfFieldOfView)
scale = WIDTH // numRays


# TEXTURES SETTINGS

textureSize = 256
halfTextureSize = textureSize // 2