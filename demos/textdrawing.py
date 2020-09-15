# =======
# Imports
# =======
import pygame, sys
from pygame.locals import *
# ====
# Init
# ====
pygame.init()
# ------
# Screen
# ------
DISPLAYSURF = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('Text Drawing')
# ------
# Colors
# ------
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
# ----
# Text
# ----
fontObj = pygame.font.Font('SPACEMONO_REGULAR.ttf', 32)
textSurfaceObj = fontObj.reder('This is a test!', True, GREEN, BLUE)

