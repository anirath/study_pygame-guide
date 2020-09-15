# ==============
# Import Modules
# ==============
import pygame, sys
from pygame.locals import *
# =================
# Initialize PyGame
# =================
pygame.init()
# =================
# Setup Environment
# =================
# Configure FPS
# -------------
FPS = 60
fpsClock = pygame.time.Clock()
# ----------------
# Configure Window
# ----------------
DISPLAYSURF = pygame.display.set_mode((1280, 720), 0, 32)
pygame.display.set_caption('Kitty Cat Animation')
# --------------------------
# Declare Env-Vars & Objects
# --------------------------
BLACK = (  0,   0,   0)
catImg = pygame.image.load('../assets/img/cat.png')
catx = 10
caty = 10
direction = 'right'
directionToggle = 'one'
screenToggle = 'one'
# =================
# Process Game Loop
# =================
while True:
    # ------------
    # Style Screen
    # ------------
    # Fill the display surface with black.
    DISPLAYSURF.fill(BLACK)
    # --------------
    # Set Animations
    # --------------
    # Use the toggle variable to determine direction, and set the cat image to move around the screen.
    if directionToggle == 'one':
        if direction == 'right':
            catx += 10
            if catx == 1110:
                direction = 'down'
        elif direction == 'down':
            caty += 10
            if caty == 560:
                direction = 'left'
        elif direction == 'left':
            catx -= 10
            if catx == 10:
                direction = 'up'
        elif direction == 'up':
            caty -= 10
            if caty == 10:
                direction = 'down'
                directionToggle ='two'
    # When the toggle is set to `two` reverse the direction around the screen.
    elif directionToggle == 'two':
        if direction == 'down':
            caty += 10
            if caty == 560:
                direction = 'right'
        elif direction == 'right':
            catx += 10
            if catx == 1110:
                direction = 'up'
        elif direction == 'up':
            caty -= 10
            if caty == 10:
                direction = 'left'
        elif direction == 'left':
            catx -= 10
            if catx == 10:
                direction = 'right'
                directionToggle = 'one'
    # Blit the surface and image to animate according the previous settings.
    DISPLAYSURF.blit(catImg, (catx, caty))
    # -------------
    # Handle Events
    # -------------
    for event in pygame.event.get():
        # ~~~~~~~~~~~~
        # Program Quit
        # ~~~~~~~~~~~~
        # When the user quits make sure to use PyGame's quit function before the system function.
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # -----------------
    # Update Game State
    # -----------------
    # Update the Display and the FPS Clock then continue the main loop.
    pygame.display.update()
    fpsClock.tick(FPS)
