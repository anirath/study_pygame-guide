# ==============================================================================================================================================================
# Title ..... : Text Drawing Demo
# Author .... : Anirath
# Created ... : 2020.09.14
# Modified .. : 2020.09.14
# Revision .. : 01
# Usage ..... : ./textdrawing.py
# Description : A python program that draws some text using pygame, and is just a demo belonging to the study project for learning about python and pygame.
# ------------:-------------------------------------------------------------------------------------------------------------------------------------------------
# Project ... : PyGame Guide Study Project
# Version ... : N/A
# More Info . : ../README.md
# ==============================================================================================================================================================
# Import Modules & Functions
# ==========================
import pygame, sys
from pygame.locals import *
#====================
#=[Init-Environment]=
#====================
pygame.init()
#------------
#--(Screen)--
#------------
DISPLAYSURF = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('Text Drawing')
#------------
#--(Colors)--
#------------
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
#-----------------
#--(Text_&_Font)--
#-----------------
fontObj = pygame.font.Font('../assets/fonts/SpaceMonoFamily/SpaceMono-Regular.ttf', 32)
textSurfaceObj = fontObj.reder('This is a test!', True, GREEN, BLUE)

