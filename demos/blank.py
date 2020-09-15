# ==============================================================================================================================================================
# Title ..... : Blank Window Demo
# Author .... : Anirath
# Created ... : 2020.09.13
# Modified .. : 2020.09.13
# Revision .. : 01
# Usage ..... : ./blank.py
# Description : The very first demo program for the parent study project. Just creates a blank window that stays until the user closes it to show how to start
# ~~~~~~~~~~~ : a pygame project.
# ------------:------------------------------------------------------------------------------------------------------------------------------------------------
# Project ... : PyGame Guide Study Project
# Version ... : N/A
# More Info . : ../README.md
# ==============================================================================================================================================================
import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Hello World!')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
