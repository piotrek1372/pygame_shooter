import pygame

pygame.init()

RESOLUTION = pygame.display.get_desktop_sizes()[0]
SCREEN = pygame.display.set_mode(RESOLUTION)
FPS = 60
BG_COLOUR = (50, 50, 50)
PLAYER_COLOUR = (250, 255, 250)
ENEMY_COLOUR = (100, 250, 150)
